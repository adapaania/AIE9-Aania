FROM python:3.13-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PORT=7860

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
COPY langgraph.json ./
COPY app ./app
COPY data ./data

RUN uv sync --frozen

CMD sh -c 'printf "OPENAI_API_KEY=%s\nTAVILY_API_KEY=%s\nLANGSMITH_API_KEY=%s\nLANGSMITH_TRACING=%s\nOPENAI_CHAT_MODEL=%s\nOPENAI_EMBEDDING_MODEL=%s\nRAG_DATA_DIR=data\n" "$OPENAI_API_KEY" "$TAVILY_API_KEY" "$LANGSMITH_API_KEY" "${LANGSMITH_TRACING:-true}" "${OPENAI_CHAT_MODEL:-gpt-4o-mini}" "${OPENAI_EMBEDDING_MODEL:-text-embedding-3-small}" > .env && uv run langgraph dev --host 0.0.0.0 --port ${PORT}'
