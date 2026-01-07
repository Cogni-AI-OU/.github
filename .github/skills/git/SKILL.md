<!-- markdownlint-disable MD022 MD026 MD041 -->
---
name: git
description: Guide for using git
license: MIT
---

You are an expert in advanced git usage within repository agents. Prioritize **non-interactive**, safe,
reproducible operations that maintain clean history and respect repository conventions.

### Core Principles
- **Non-interactive execution**: All commands must run without prompting for input. Never use interactive modes (`-i`, `--interactive`, default editors).
- **Linear history**: Prefer rebase over merge for feature branches to keep history clean and bisectable.
- **Atomic changes**: Favor small, focused commits. Use amend/fixup patterns for corrections instead of sprawling histories.
- **Safety**: Never perform destructive operations (force push, hard reset, branch deletion) without explicit reasoning and user confirmation.
- **Hook handling**: Aim to satisfy pre-commit/pre-push hooks. Use `--no-verify` only as a last resort when hooks are non-critical or environment-specific.
- **Conventional Commits**: Always use the format `<type>[optional scope]: <description>` with a blank line and detailed body if needed.

### Non-Interactive Patterns

- **Amending last commit** (preserve author date):
`git commit --amend --no-edit --date="$(git log -1 --format=%aD)"`
- **Fixup previous commits** (non-interactive preparation):
- Create fixup: `git commit --fixup <commit-sha>`
- Later autosquash (requires interactive rebase—propose to user or defer to PR squash if agent cannot handle `-i`):
`git rebase -i --autosquash origin/main`
- **Rebasing feature branches**:
`git fetch origin && git rebase origin/main --no-verify` (add `--no-verify` only if hooks block)
- **Cherry-picking without conflicts**:
`git cherry-pick -x <commit-sha>` (`-x` records original SHA for traceability)
- **Stashing partial work** (non-interactive):
`git stash push -m "wip-description" -p` (patch mode for selective stashing)

### Safety & Recovery

- **Check repository state non-interactively**:
- Clean working tree: `git diff --quiet && git diff --cached --quiet`
- Current branch: `git rev-parse --abbrev-ref HEAD`
- Unpushed commits: `git log origin/$(git rev-parse --abbrev-ref HEAD)..HEAD`
- **Reflog for recovery**:
Reference `git reflog` output before any history-rewriting operation to enable rollback.
- **Backup before destructive ops**:
Create temporary tag: `git tag backup/pre-op-$(date +%s)`
- **Force push only when required** (e.g., after approved history rewrite):
`git push --force-with-lease=origin <branch>`

### Useful Diagnostic Commands

- Verify identity: `git config user.name && git config user.email`
- Remote tracking status: `git status -sb`
- Commit template check: `git config commit.template`
- Signed commit verification: `git log --show-signature -1`

### What to Avoid

- Interactive operations (`git rebase -i`, `git add -p` without scripting, editor prompts).
- Direct pushes to protected branches (main/master).
- `git pull` in scripts—prefer explicit `fetch` + `rebase` or `merge --no-edit`.
- `--force` pushes without `--force-with-lease`.
- Unqualified `git reset --hard` (prefer `git reset --hard origin/main` with backup tag).

Always explain proposed git operations step-by-step, quote exact commands, and confirm irreversible actions with the user.
