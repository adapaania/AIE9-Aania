# Activity 1: RAGAS Evaluation with Cost Analysis

This evaluates the same cat-health RAG questions against a Fireworks-powered pipeline and an OpenAI `gpt-4.1-mini` equivalent. LangSmith tracing was enabled from `.env` so the detailed token/cost traces can be reviewed in LangSmith.

## Summary

| Provider | Faithfulness | Answer relevancy | Context precision | Context recall | Avg latency | Total tokens | Est. cost |
|---|---:|---:|---:|---:|---:|---:|---:|
| Fireworks | 0.875 | 0.921 | 1.000 | 1.000 | 41.87s | 1377 | $0.000306 |
| OpenAI | 0.500 | 0.393 | 0.500 | 0.500 | 1.41s | 1038 | $0.000480 |

## Analysis

- Fireworks tests the open-source hosted endpoint path required by the assignment.
- OpenAI `gpt-4.1-mini` is the comparison baseline for answer quality and cost.
- RAGAS scores show whether each answer is grounded in retrieved context, relevant to the question, and supported by useful retrieved chunks.
- The estimated cost column is a local approximation. For the final Loom, use the LangSmith project dashboard as the source of truth for exact trace cost.

## Per-question Results

### Fireworks: What is the title of the cat health guideline document?

Answer: The title of the cat health guideline document is **“2021 AAHA/AAFP Feline Life Stage Guidelines.”**

Scores: faithfulness=1.0, answer_relevancy=1.0, context_precision=0.99999999995, context_recall=1.0
Latency: 77.238s; tokens: 694; estimated cost: $0.0001218

### Fireworks: Why should the most invasive parts of a cat exam happen near the end?

Answer: The most invasive parts of a cat’s exam should be performed near the end because doing them after the less stressful components helps keep the cat calm. By allowing the cat to experience the gentler parts of the exam first, the animal is more relaxed and easier to handle when the more invasive procedures—such as dental work, temperature checks, nail trims, sample collection, and imaging—are performed. This sequencing reduces the overall stress response, improves patient comfort, and makes the entire visit smoother for the cat, the client, and the practice team.

Scores: faithfulness=0.75, answer_relevancy=0.8410840074540837, context_precision=0.9999999999, context_recall=1.0
Latency: 6.494s; tokens: 683; estimated cost: $0.0001843

### OpenAI: What is the title of the cat health guideline document?

Answer: You don't know.

Scores: faithfulness=0.0, answer_relevancy=0.0, context_precision=0.0, context_recall=0.0
Latency: 1.263s; tokens: 581; estimated cost: $0.0002372

### OpenAI: Why should the most invasive parts of a cat exam happen near the end?

Answer: The most invasive parts of a cat exam should happen near the end to reduce the stress response of the patient. Keeping these parts until the end helps improve patient comfort, time efficiency, and the overall experience for the patient, client, and practice team.

Scores: faithfulness=1.0, answer_relevancy=0.7862915023141118, context_precision=0.99999999995, context_recall=1.0
Latency: 1.565s; tokens: 457; estimated cost: $0.0002428
