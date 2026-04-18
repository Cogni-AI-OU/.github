# GitHub Actions Workflows (Agent Catalog)

Authoritative, agent-facing catalog of workflows in this repository. Use this when loading or modifying
workflows and keep it in sync with the files in this directory.

For a human-readable overview, see [README.md](README.md).

## Workflow catalog

- **[check.yml](check.yml)**: Linting and quality gates via actionlint and pre-commit.
- **[devcontainer-ci.yml](devcontainer-ci.yml)**: Build/test devcontainer and required tools/packages.
- **[opencode.yml](opencode.yml)**: OpenCode agent invocation via comments or manual triggers.

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
- Inputs: `agent` (default `cogni-ai-architect`), `model` (workflow_call default via
  `vars.OPENCODE_MODEL_DEFAULT` with fallback `opencode/gpt-5-codex`; workflow_dispatch
  default `opencode/gpt-5-codex`), `prompt` (optional override).
- Triggers: `workflow_dispatch`, `workflow_call`, or issue comments and PR review comments with `/oc` or `/opencode`
  from trusted (non-bot) collaborators/members/owners.
- Guardrail: comment-triggered runs do not populate `inputs.*`; back shared OpenCode defaults
  with workflow-level `env` values instead of hardcoding agent/model literals in steps.
- Concurrency: Only one run per issue/PR/branch at a time; new runs cancel pending ones.
- Permissions: `contents: read`, `id-token: write`, `issues: write`, `pull-requests: write`.
- Reusable: `uses: Cogni-AI-OU/.github/.github/workflows/opencode.yml@main`.

## Synchronized Configuration

The following configuration values **MUST** be kept in sync across multiple files:

### OPENCODE_PERMISSION

The `OPENCODE_PERMISSION` environment variable defines the bash command allowlist for OpenCode agents.
It must be identical in the workflow file:

| File | Location |
| ---- | -------- |
| [opencode.yml](opencode.yml) | env section |

### Model options list

The `model` input options for `workflow_dispatch` must be identical in the workflow file:

| File | Location |
| ---- | -------- |
| [opencode.yml](opencode.yml) | `workflow_dispatch` inputs |

## Notes

- Follow [.github/instructions/github-workflows.instruction.md](../instructions/github-workflows.instruction.md)
  when editing workflow files (ordering, formatting, validation).
- Keep this catalog updated when workflows are added, removed, or renamed.
