<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719"
     width="200px"
     height="auto"/>
</p>

<h1 align="center" id="heading">Session 16: Reinforcement Learning with Verifiable Rewards (RLVR)</h1>

### [Quicklinks](https://github.com/AI-Maker-Space/The-AI-Engineering-Certification-v1.0/tree/main/00_Docs/Modules)

| 📰 Session Sheet | ⏺️ Recording | 🖼️ Slides | 👨‍💻 Repo | 📝 Homework | 📁 Feedback |
|:-----------------|:-------------|:----------|:----------|:------------|:------------|
| [Session 16: RLVR](https://github.com/AI-Maker-Space/The-AI-Engineering-Certification-v1.0/tree/main/00_Docs/Modules/16_RLVR) |[Recording!](https://us02web.zoom.us/rec/share/nFLWt0guwrpQI6LxPS91qr6j1eeI9csKjj7oub5P4gQc86V-2Uedr3rvuS_JAdhx.2RxM5BRGjmn6DwX0) <br> passcode: `1Suw?vDP`| [Session 16 Slides](https://canva.link/l8691ralz271ogr) | You are here! | [Session 16 Assignment](https://forms.gle/sAhcKBmd4UqgooPG6) | [Feedback 7/23](https://forms.gle/BnDW3TnRZTCXyK4h8) |

## Main Assignment

In Session 15 you changed a model's weights with GRPO, rewarding verifiably correct answers. In this assignment you will build the other half of that loop: the **verifier** and the data pipeline around it.

You will implement the RLVR loop against an API model — no GPU required:

```text
prompt -> sample N completions -> verify each against a deterministic checker
       -> assign rewards -> keep verified-correct samples as preference data
       -> policy update -> repeat
```

Along the way you will build verifiable reward functions for two domains (math exact-match and code judged by unit tests), detect reward-hacking signatures, maintain a verifier audit trail, and construct chosen/rejected preference pairs ready for DPO-style training.

The main notebook is:

```text
01_RLVR_Verifiable_Rewards.ipynb
```

Complete all questions and the activity directly in the notebook.

## Outline

### Breakout Room #1: The Verifiable Reward Loop

- Task 1: Environment Setup
- Task 2: Problems and Answer Extraction
- Task 3: A Math Reward Function
- Question #1 and Question #2
- Task 4: Sample and Verify

### Breakout Room #2: Reward Hacking, Code Verification, and Preference Data

- Task 5: Reward-Hacking Detection and the Audit Trail
- Question #3
- Task 6: A Code Verifier
- Question #4
- Task 7: Build Preference Pairs
- Activity #1: Build Your Own Verifier

## Setup

### Prerequisites

- **An OpenAI API key** — the sampling loop makes a few dozen small-model calls (roughly cents of usage).
- Any OS (macOS, Linux, Windows). Unlike Session 15, this session needs no GPU.

> ⚠️ Task 6 executes model-generated Python in a subprocess on your machine. The demo programs are trivial, but read the sandboxing notes in the notebook before running.

### Install

From this folder, install the environment with uv:

```bash
uv sync
```

Then open the notebook in Cursor or VS Code and select the Python/Jupyter environment created by uv.

## Submitting Your Homework

Follow these steps to prepare and submit your homework:

1. Pull the latest updates from upstream into the main branch of your AIE9 repo:

```bash
git checkout main
git pull upstream main
git push origin main
```

2. Start Cursor from the `16_RLVR` folder.
3. Complete the notebook questions and Activity #1.
4. Keep useful notebook outputs that help explain your work, especially the verified-correct rates, flagged-sample counts, and a preference-pair example. Remove secrets and excessively noisy outputs.
5. Add, commit, and push your modified work to your origin repository.

When submitting your homework, provide the GitHub URL to your AIE9 repo.
