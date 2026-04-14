# GitHub Actions Workflows (Agent Catalog)

Authoritative, agent-facing catalog of workflows in this repository. Use this when loading or modifying
workflows and keep it in sync with the files in this directory.

For a human-readable overview, see [README.md](README.md).

## Workflow catalog

- **[check.yml](check.yml)**: Linting and quality gates via actionlint and pre-commit.
- **[devcontainer-ci.yml](devcontainer-ci.yml)**: Build/test devcontainer and required tools/packages.
- **[opencode.yml](opencode.yml)**: OpenCode agent invocation via comments or manual triggers.
- **[opencode-review.yml](opencode-review.yml)**: OpenCode PR review.

## Details

### check.yml

- Purpose: run actionlint and pre-commit to enforce workflow and repo standards.
- Triggers: `push`, `pull_request`, `schedule`, `workflow_call`, `workflow_dispatch`,
  `workflow_run` (after bot workflow completions).
- Bot-PR support: `workflow_run` trigger enables checks on PRs created by bots,
  since normal `pull_request` events don't trigger for bot actors.
- Reusable: `uses: Cogni-AI-OU/.github/.github/workflows/check.yml@main`.
- Jobs: `actionlint`, `link-checker`, `pre-commit`.

### devcontainer-ci.yml

- Purpose: build and validate the dev container; ensure required tools and Python packages exist.
- Inputs: `required_commands` (defaults to common CLI tools), `required_python_packages`
  (defaults to ansible, ansible-lint, docker, molecule, pre-commit, uv).
- Triggers: pull_request/push affecting `.devcontainer/` or this workflow; weekly schedule;
  `workflow_call`.
- Permissions: callers must grant `packages: write` when pushing images to GHCR.
- Reusable: `uses: Cogni-AI-OU/.github/.github/workflows/devcontainer-ci.yml@main`.

### opencode.yml

- Purpose: invoke OpenCode agents via slash commands or manual triggers.
- Inputs: `agent`, `model`, `prompt`, `issue_number` (used to override defaults on manual dispatch/calls).
- Triggers: `workflow_dispatch`, `workflow_call`, `issues: opened`, `pull_request_review: submitted`, or issue comments
  and PR review comments with `/oc` or `/opencode` from trusted (non-bot) collaborators/members/owners.
- Permissions: `actions: read`, `contents: write`, `id-token: write`, `issues: write`, `pull-requests: write`.
- Reusable: `uses: Cogni-AI-OU/.github/.github/workflows/opencode.yml@main`.

### opencode-review.yml

- Purpose: OpenCode-driven PR review.
- Inputs: `pr_number` (req for call/dispatch). Note that `opencode-review.yml` only
  exposes `pr_number` so callers should use the wrapper's inputs instead.
- Triggers: pull_request_target (trusted authors), /review comment (COLLABORATOR/OWNER/MEMBER), workflow_call,
  workflow_dispatch.
- Permissions: `contents: read`, `id-token: write`, `issues: read`, `pull-requests: write`.
- Reusable: `uses: Cogni-AI-OU/.github/.github/workflows/opencode-review.yml@main`.

## Configuration Delegation

The `OPENCODE_PERMISSION` environment variable and `model` input options are now managed
centrally by the local wrapper (`.github/workflows/opencode.yml`).
Callers should use that wrapper's inputs/environment (`OPENCODE_PERMISSION`, `model`, `prompt`)
instead of defining them locally so future readers fix the correct file and avoid reintroducing
missing-input regressions.

## Notes

- Follow [.github/instructions/github-workflows.instruction.md](../instructions/github-workflows.instruction.md)
  when editing workflow files (ordering, formatting, validation).
- Keep this catalog updated when workflows are added, removed, or renamed.
