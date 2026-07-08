from __future__ import annotations

import csv
import os
import statistics
import sys
import time
import types
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from datasets import Dataset
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

# RAGAS 0.4.3 imports an old optional LangChain Vertex module. The eval below
# does not use Vertex AI, so this small shim keeps the installed package usable.
fake_vertex = types.ModuleType("langchain_community.chat_models.vertexai")
class ChatVertexAI:  # pragma: no cover - compatibility shim only
    pass
fake_vertex.ChatVertexAI = ChatVertexAI
sys.modules.setdefault("langchain_community.chat_models.vertexai", fake_vertex)

from ragas import evaluate
from ragas.embeddings import LangchainEmbeddingsWrapper
from ragas.llms import LangchainLLMWrapper
from ragas.metrics._answer_relevance import answer_relevancy
from ragas.metrics._context_precision import context_precision
from ragas.metrics._context_recall import context_recall
from ragas.metrics._faithfulness import faithfulness

FIREWORKS_BASE_URL = "https://api.fireworks.ai/inference/v1"
DATA_PATH = Path("data/cat-health-guide.pdf")
RESULTS_CSV = Path("activity_1_results.csv")
REPORT_MD = Path("activity_1_report.md")

QUESTIONS = [
    {
        "question": "What is the title of the cat health guideline document?",
        "reference": "The document is titled the 2021 AAHA/AAFP Feline Life Stage Guidelines.",
    },
    {
        "question": "Why should the most invasive parts of a cat exam happen near the end?",
        "reference": "The most invasive parts, such as dental examination, temperature assessment, nail trimming, sample collection, and imaging, should be saved until the end to reduce patient stress and improve the cat, owner, and practice team experience.",
    },
]

@dataclass
class ProviderConfig:
    name: str
    chat_model: str
    embedding_model: str
    api_key: str
    base_url: str | None
    embedding_dimensions: int | None = None


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def load_chunks() -> list[Document]:
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Missing PDF: {DATA_PATH}")
    docs = PyMuPDFLoader(str(DATA_PATH)).load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=900, chunk_overlap=120)
    return splitter.split_documents(docs)


def make_embeddings(config: ProviderConfig):
    kwargs: dict[str, Any] = {
        "model": config.embedding_model,
        "api_key": config.api_key,
        "check_embedding_ctx_length": False,
    }
    if config.base_url:
        kwargs["base_url"] = config.base_url
    if config.embedding_dimensions:
        kwargs["dimensions"] = config.embedding_dimensions
    return OpenAIEmbeddings(**kwargs)


def make_llm(config: ProviderConfig, temperature: float = 0, max_tokens: int = 300):
    kwargs: dict[str, Any] = {
        "model": config.chat_model,
        "api_key": config.api_key,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "timeout": 90,
        "max_retries": 1,
    }
    if config.base_url:
        kwargs["base_url"] = config.base_url
    return ChatOpenAI(**kwargs)


def token_counts(message: Any) -> tuple[int, int, int]:
    usage = getattr(message, "usage_metadata", None) or {}
    if usage:
        prompt = int(usage.get("input_tokens") or 0)
        completion = int(usage.get("output_tokens") or 0)
        return prompt, completion, prompt + completion

    metadata = getattr(message, "response_metadata", None) or {}
    token_usage = metadata.get("token_usage") or metadata.get("usage") or {}
    prompt = int(token_usage.get("prompt_tokens") or token_usage.get("input_tokens") or 0)
    completion = int(token_usage.get("completion_tokens") or token_usage.get("output_tokens") or 0)
    total = int(token_usage.get("total_tokens") or prompt + completion)
    return prompt, completion, total


def estimate_cost(provider: str, prompt_tokens: int, completion_tokens: int) -> float:
    # Update these with LangSmith dashboard/provider pricing if your account shows exact rates.
    # Fireworks serverless prices vary by model/account; this conservative placeholder keeps
    # the report reproducible while LangSmith provides the authoritative trace cost.
    prices_per_million = {
        "fireworks": {"input": 0.10, "output": 0.50},
        "openai": {"input": 0.40, "output": 1.60},  # gpt-4.1-mini public pricing ballpark
    }
    key = "fireworks" if provider.lower().startswith("fireworks") else "openai"
    price = prices_per_million[key]
    return (prompt_tokens / 1_000_000 * price["input"]) + (completion_tokens / 1_000_000 * price["output"])


def run_provider(config: ProviderConfig, chunks: list[Document]) -> list[dict[str, Any]]:
    print(f"\nBuilding {config.name} vector store...", flush=True)
    embeddings = make_embeddings(config)
    vectorstore = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        location=":memory:",
        collection_name=f"activity_1_{config.name.lower()}",
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
    llm = make_llm(config)
    prompt = ChatPromptTemplate.from_messages([
        (
            "human",
            "Use only the context to answer. If the answer is not in the context, say you don't know.\n\nContext:\n{context}\n\nQuestion: {question}",
        )
    ])

    rows: list[dict[str, Any]] = []
    for item in QUESTIONS:
        question = item["question"]
        started = time.perf_counter()
        docs = retriever.invoke(question)
        contexts = [doc.page_content for doc in docs]
        context_text = "\n\n".join(contexts)
        message = llm.invoke(prompt.format_messages(context=context_text, question=question))
        latency = time.perf_counter() - started
        prompt_tokens, completion_tokens, total_tokens = token_counts(message)
        answer = str(message.content)
        row = {
            "provider": config.name,
            "user_input": question,
            "response": answer,
            "retrieved_contexts": contexts,
            "reference": item["reference"],
            "latency_seconds": round(latency, 3),
            "prompt_tokens": prompt_tokens,
            "completion_tokens": completion_tokens,
            "total_tokens": total_tokens,
            "estimated_cost_usd": round(estimate_cost(config.name, prompt_tokens, completion_tokens), 8),
        }
        print(f"{config.name}: {question[:52]}... {latency:.2f}s, {total_tokens} tokens", flush=True)
        rows.append(row)
    return rows


def run_ragas(rows: list[dict[str, Any]]):
    judge_llm = make_llm(
        ProviderConfig(
            name="openai_judge",
            chat_model=os.environ.get("OPENAI_CHAT_MODEL", "gpt-4.1-mini"),
            embedding_model=os.environ.get("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
            api_key=require_env("OPENAI_API_KEY"),
            base_url=None,
        ),
        max_tokens=900,
    )
    judge_embeddings = make_embeddings(
        ProviderConfig(
            name="openai_judge",
            chat_model=os.environ.get("OPENAI_CHAT_MODEL", "gpt-4.1-mini"),
            embedding_model=os.environ.get("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
            api_key=require_env("OPENAI_API_KEY"),
            base_url=None,
        )
    )
    dataset = Dataset.from_list([
        {
            "user_input": row["user_input"],
            "response": row["response"],
            "retrieved_contexts": row["retrieved_contexts"],
            "reference": row["reference"],
        }
        for row in rows
    ])
    result = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
        llm=LangchainLLMWrapper(judge_llm),
        embeddings=LangchainEmbeddingsWrapper(judge_embeddings),
        raise_exceptions=False,
    )
    scores_df = result.to_pandas()
    score_records = scores_df.to_dict(orient="records")
    for row, scores in zip(rows, score_records):
        for key in ["faithfulness", "answer_relevancy", "context_precision", "context_recall"]:
            row[key] = scores.get(key)
    return rows


def write_outputs(rows: list[dict[str, Any]]) -> None:
    csv_fields = [
        "provider",
        "user_input",
        "reference",
        "response",
        "faithfulness",
        "answer_relevancy",
        "context_precision",
        "context_recall",
        "latency_seconds",
        "prompt_tokens",
        "completion_tokens",
        "total_tokens",
        "estimated_cost_usd",
    ]
    with RESULTS_CSV.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k) for k in csv_fields})

    providers = sorted({row["provider"] for row in rows})
    lines = ["# Activity 1: RAGAS Evaluation with Cost Analysis", ""]
    lines.append("This evaluates the same cat-health RAG questions against a Fireworks-powered pipeline and an OpenAI `gpt-4.1-mini` equivalent. LangSmith tracing was enabled from `.env` so the detailed token/cost traces can be reviewed in LangSmith.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Provider | Faithfulness | Answer relevancy | Context precision | Context recall | Avg latency | Total tokens | Est. cost |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
    for provider in providers:
        subset = [row for row in rows if row["provider"] == provider]
        def avg(key: str) -> str:
            vals = [float(row[key]) for row in subset if row.get(key) is not None]
            return f"{statistics.mean(vals):.3f}" if vals else "n/a"
        avg_latency = statistics.mean(float(row["latency_seconds"]) for row in subset)
        total_tokens = sum(int(row["total_tokens"] or 0) for row in subset)
        total_cost = sum(float(row["estimated_cost_usd"] or 0) for row in subset)
        lines.append(
            f"| {provider} | {avg('faithfulness')} | {avg('answer_relevancy')} | {avg('context_precision')} | {avg('context_recall')} | {avg_latency:.2f}s | {total_tokens} | ${total_cost:.6f} |"
        )

    lines.extend([
        "",
        "## Analysis",
        "",
        "- Fireworks tests the open-source hosted endpoint path required by the assignment.",
        "- OpenAI `gpt-4.1-mini` is the comparison baseline for answer quality and cost.",
        "- RAGAS scores show whether each answer is grounded in retrieved context, relevant to the question, and supported by useful retrieved chunks.",
        "- The estimated cost column is a local approximation. For the final Loom, use the LangSmith project dashboard as the source of truth for exact trace cost.",
        "",
        "## Per-question Results",
        "",
    ])
    for row in rows:
        lines.extend([
            f"### {row['provider']}: {row['user_input']}",
            "",
            f"Answer: {row['response']}",
            "",
            f"Scores: faithfulness={row.get('faithfulness')}, answer_relevancy={row.get('answer_relevancy')}, context_precision={row.get('context_precision')}, context_recall={row.get('context_recall')}",
            f"Latency: {row['latency_seconds']}s; tokens: {row['total_tokens']}; estimated cost: ${row['estimated_cost_usd']}",
            "",
        ])
    REPORT_MD.write_text("\n".join(lines))


def main() -> None:
    os.environ.setdefault("LANGSMITH_TRACING", "true")
    os.environ.setdefault("LANGSMITH_PROJECT", "AIEC Session 10 Activity 1")

    chunks = load_chunks()
    providers = [
        ProviderConfig(
            name="Fireworks",
            chat_model=os.environ.get("FIREWORKS_CHAT_MODEL", "accounts/fireworks/models/gpt-oss-20b"),
            embedding_model=os.environ.get("FIREWORKS_EMBEDDING_MODEL", "accounts/fireworks/models/qwen3-embedding-8b"),
            api_key=require_env("FIREWORKS_API_KEY"),
            base_url=FIREWORKS_BASE_URL,
            embedding_dimensions=4096,
        ),
        ProviderConfig(
            name="OpenAI",
            chat_model="gpt-4.1-mini",
            embedding_model=os.environ.get("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small"),
            api_key=require_env("OPENAI_API_KEY"),
            base_url=None,
        ),
    ]
    rows: list[dict[str, Any]] = []
    for provider in providers:
        rows.extend(run_provider(provider, chunks))
    rows = run_ragas(rows)
    write_outputs(rows)
    print(f"\nWrote {RESULTS_CSV} and {REPORT_MD}")


if __name__ == "__main__":
    main()
