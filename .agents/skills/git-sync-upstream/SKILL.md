---
name: git-sync-upstream
description: "Safely configure and use a Git upstream remote for fork-style and course repositories. Use when Codex needs to add, inspect, repair, or explain an upstream remote; pull or fetch changes from upstream; sync newly released course materials; explain origin versus upstream; or follow the AI Maker Space course Git workflow before pushing local work to origin."
---

# Git Sync Upstream

## Overview

Manage the repository flow `upstream -> local -> origin` without overwriting local work. Treat `upstream` as the source repository to pull from and `origin` as the user's remote repository to push to.

For the AI Maker Space course commands and placeholders, read [references/course-workflow.md](references/course-workflow.md).

## Inspect Before Changing Anything

Run these commands from the target repository:

```bash
git rev-parse --show-toplevel
git status --short --branch
git remote -v
git branch --show-current
```

Use the output to confirm:

- The command is running in the intended repository.
- The active branch is the expected branch, usually `main`.
- Existing local edits, staged files, and untracked files are visible before pulling.
- `origin` points to the user's repository.
- `upstream`, if present, points to the source repository.

Do not discard, reset, stash, commit, or overwrite local changes unless the user explicitly asks. Do not push to `upstream` unless the user explicitly requests it and confirms that remote is writable.

## Set Up Upstream

When `upstream` is missing and the user provides or confirms the source repository URL, run:

```bash
git remote add upstream <upstream-url>
git remote -v
```

When `upstream` already exists:

- If its URL is correct, report that setup is already complete.
- If its URL differs from the requested URL, show both URLs and ask before changing it with `git remote set-url upstream <upstream-url>`.

For the course repository, prefer the SSH URL documented in [references/course-workflow.md](references/course-workflow.md).

## Pull Changes From Upstream

Before pulling, inspect the worktree with `git status --short --branch`.

- If the worktree has local changes, stop before pulling and explain that the pull could create conflicts. Ask whether the user wants to commit or stash their work first.
- If the worktree is clean, pull the requested upstream branch.

For the AI Maker Space course workflow, use the documented command:

```bash
git pull upstream main --allow-unrelated-histories
```

For an established non-course repository, default to:

```bash
git pull upstream main
```

Use `--allow-unrelated-histories` only when the repositories may have separate initial histories or when the course workflow explicitly calls for it.

After a successful pull, run:

```bash
git status --short --branch
```

Report whether changes were integrated and whether any follow-up push to `origin` was requested. Do not push automatically unless the user asks to sync their remote copy as well.

## Push Local Work To Origin

When the user asks to upload completed local work, inspect the branch and status first. For the course workflow, push the local `main` branch to the user's repository:

```bash
git push origin main
```

Keep the direction clear:

- Pull course materials from `upstream`.
- Edit and commit work locally.
- Push completed work to `origin`.

## Handle Common Problems

- If the directory is not a Git repository, stop and ask for the repository path.
- If `upstream` is missing, ask for or confirm the upstream URL before adding it.
- If authentication fails, report the failing remote URL and recommend checking SSH keys or GitHub access.
- If Git reports merge conflicts, show the conflicted files with `git status --short`, explain that the pull needs conflict resolution, and do not reset or push.
- If the expected branch is not `main`, inspect available branches and confirm the intended branch before pulling.

