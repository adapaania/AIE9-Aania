# Session 14: 🖼️ Multimodal RAG

🎯 Learn how to build retrieval systems that can understand and reason over both text and images.

📚 **Learning Outcomes**

- Understand how multimodal embeddings enable image-based retrieval
- Introduce Vision Language Models (VLMs) and how they can be used for parsing/chunking, for understanding/retrieval, or both
- Learn how to combine image + text retrieval in a single pipeline

## 📛 Required Tooling & Account Setup

No new accounts or keys are required for this session

## 📜 Recommended Reading

- [An Easy Introduction to Multimodal Retrieval-Augmented Generation](https://developer.nvidia.com/blog/an-easy-introduction-to-multimodal-retrieval-augmented-generation/) — beginner-friendly overview of multimodal RAG and three common approaches for retrieving across text and images.
- [Multi-modal RAG on Slide Decks](https://blog.langchain.com/multi-modal-rag-template/) — practical comparison of direct multimodal embeddings and image-summary-based retrieval.
- [CLIP: Connecting Text and Images](https://openai.com/index/clip/) — approachable introduction to how CLIP connects natural-language descriptions with visual concepts.
- [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) — the original CLIP research paper explaining contrastive image-text training and zero-shot transfer.
- [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/abs/2407.01449) — advanced paper on retrieving visually rich document pages directly with vision-language models and late-interaction embeddings.

## Overview

Multimodal RAG extends traditional text-based RAG so an AI system can retrieve and reason over information found in images, charts, figures, documents, audio, and video. Instead of relying only on extracted text, a multimodal system may use vision-language models to interpret visual content, shared image-text embedding models to retrieve relevant images, or separate retrieval pipelines for each type of data. The goal is to help an AI application locate the right source regardless of its format and then generate an answer grounded in the original content.

In this session, you will compare several approaches for retrieving text and images, including image captions, CLIP embeddings, and separate indexes combined through rank fusion. You will also explore an important division of labor: retrieval identifies the relevant chart or image, while a vision-language model examines the original pixels to extract exact details and produce a grounded answer. Finally, you will extend these ideas to video by aligning transcript segments with representative frames and returning answers with timestamp citations.
