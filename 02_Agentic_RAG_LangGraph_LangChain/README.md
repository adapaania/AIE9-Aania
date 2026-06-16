

# Session 2: Agentic RAG with LangGraph and LangChain

### [Quicklinks]()


| 📰 Session Sheet                                                                                                                                   | ⏺️ Recording                                                                                                                                           | 🖼️ Slides                                             | 👨‍💻 Repo    | 📝 Homework                                                 | 📁 Feedback                                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------ | ------------- | ----------------------------------------------------------- | --------------------------------------------------- |
| [Session 2: Agents](https://github.com/AI-Maker-Space/The-AI-Engineering-Certification-v1.0/tree/main/00_Docs/Modules/02_Agentic_RAG_From_Scratch) | [Recording!](https://us02web.zoom.us/rec/share/QY5jO23FGTCX3yYT_RkogG_aq_BISzHfzN7CcVHP3qeliXKqwBnraUQSNlHtkRUD.OwX79Wfmk0hdy087) passcode: `3fAh&+PM` | [Session 2 Slides](https://canva.link/l06gfshgqhv8svl) | You are here! | [Session 2 Assignment](https://forms.gle/9L3kTpvfJzFoAEDn8) | [Feedback 6/4](https://forms.gle/9L3kTpvfJzFoAEDn8) |


## Main Assignment

In this assignment, you will build an agentic RAG application using LangChain, LangGraph, OpenAI models, and Qdrant.

Session 1 showed a predictable two-step RAG flow:

```text
question -> retrieve -> generate
```

Session 2 makes retrieval agentic:

```text
question -> agent decides whether to retrieve -> optional retriever tool call -> answer
```

The point is not to add a complicated retrieval pipeline. The point is to give the agent a retrieval tool so it can retrieve when it decides retrieval is useful.

You will build that same loop two ways:

1. With LangChain `create_agent` and middleware, which gives you the agent loop quickly and lets you customize its behavior.
2. With LangGraph `StateGraph`, `ToolNode`, and `tools_condition`, so you can see how the loop works.

The main notebook is:

```text
01_Cat_Health_Agentic_RAG_LangGraph_LangChain.ipynb
```

The notebook uses the bundled cat health corpus:

```text
data/cat_health_guidelines.md
```

Complete all questions and activities directly in the notebook.

## Outline

### Breakout Room #1: High-Level Agentic RAG with LangChain

- Task 1: Environment Setup
- Task 2: Load and Index the Cat Health Corpus
- Task 3: Create a Retriever Tool
- Task 4: Build an Agent with `create_agent` and Middleware
- Task 5: Visualize and Stream the `create_agent` Agent
- Activity #1: Add a Retriever Tool-Call Budget

### Breakout Room #2: Explicit Agent Loop with LangGraph

- Task 6: Build the Same Agent Loop with LangGraph
- Activity #2: Add Deterministic Scope Routing
- Advanced Build: Add Explicit Retrieval Quality Control

### Setup

From this folder, install the environment with uv:

```bash
uv sync
```

Then open the notebook in Cursor or VS Code and select the Python/Jupyter environment created by uv.

You will need an OpenAI API key available when running the notebook.

Optional LangSmith tracing:

```bash
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY="your-key"
```

## Optional Deep Dive: Agentic RAG From Scratch

If you want to look underneath the library abstractions, run the optional reference notebook:

```text
02_Cat_Health_Agentic_RAG_From_Scratch.ipynb
```

It rebuilds the same cat health agentic RAG application with Python standard-library HTTP requests and handcrafted tool, model-adapter, retrieval, and agent-loop primitives.

The application-facing names are inspired by Vercel AI SDK Core, including `tool()`, `generate_text()`, `step_count_is()`, `steps`, `on_step_finish`, `prepare_step`, and `ToolLoopAgent`. The notebook is a reference walkthrough, not an additional assignment.

## Submitting Your Homework

### Main Assignment

Follow these steps to prepare and submit your homework:

1. Pull the latest updates from upstream into the main branch of your AIE9 repo:

```bash
git checkout main
git pull upstream main
git push origin main
```

1. Start Cursor from the `02_Agentic_RAG_LangGraph_LangChain` folder.
2. Complete the notebook questions and activities.
3. Keep useful notebook outputs that help explain your work, especially graph diagrams and representative agent runs. Remove secrets and excessively noisy outputs.
4. Add, commit, and push your modified work to your origin repository.

When submitting your homework, provide the GitHub URL to your AIE9 repo.

### The Advanced Build

If you complete the Advanced Build, include:

- What you changed
- Why you changed it
- How the agent's retrieval decisions or answer quality changed

When submitting your homework, include the GitHub URL to your AIE9 repo.