# AI Maker Space Course Git Workflow

Use this reference for the course repository workflow documented in:

- `00_Docs/Prerequisites/Initial_Setup/2_Set_Up_Initial_Repos/README.md`
- `00_Docs/Prerequisites/Initial_Setup/3_Version_Control/README.md`
- `00_Docs/Prerequisites/Initial_Setup/4_Your_Weekly_Git_Workflow/README.md`

## Repository Model

- `upstream`: AI Maker Space's source repository for course materials.
- `origin`: The student's GitHub repository.
- `local`: The student's working copy on their machine.

Use this direction:

```text
upstream -> local -> origin
```

Pull from `upstream`. Push to `origin`.

## Initial Setup

Clone the student's empty GitHub repository and enter it:

```bash
git clone git@github.com:<github-username>/<course-repo>.git
cd <course-repo>
```

Add the class repository as `upstream`. Replace `XX` with the cohort number:

```bash
git remote add upstream git@github.com:AI-Maker-Space/AIEXX.git
git remote -v
```

Pull the course material into the student's local repository:

```bash
git pull upstream main --allow-unrelated-histories
```

Push the local `main` branch to the student's GitHub repository:

```bash
git push origin main
```

## Weekly Workflow

Before starting a new assignment, pull newly released course material:

```bash
git pull upstream main --allow-unrelated-histories
```

After completing the assignment, stage, commit, and push the student's work:

```bash
git add .
git commit -m "Completed lesson X assignment"
git push origin main
```

## Guardrails

Inspect `git status --short --branch` before pulling, staging, committing, or pushing. Avoid pulling with local modifications until the user decides whether to commit or stash them. Avoid using `git add .` automatically when unrelated changes are present; stage the intended files when the task scope is narrower.
