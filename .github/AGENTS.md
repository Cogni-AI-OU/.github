# .github Directory Catalog (Agent View)

Catalog of folders within the `.github` directory of this repository.
Use this as the entry point for agent work, and follow linked catalogs where present.

## Folder catalog

| Folder | Purpose | Agent catalog |
| ------ | ------- | ------------- |
| [.github/agents/](agents/) | Agent configuration files (e.g., specialized agent definitions) | — |
| [.github/instructions/](instructions/) | Language- and file-type editing standards | [.github/instructions/AGENTS.md](instructions/AGENTS.md) |
| [.github/prompts/](prompts/) | Prompt files for AI agents (Markdown and YAML) | [.github/prompts/AGENTS.md](prompts/AGENTS.md) |
| [.github/skills/](skills/) | Loadable Copilot skills with SKILL.md entries | [.github/skills/AGENTS.md](skills/AGENTS.md) |
| [.github/workflows/](workflows/) | Reusable GitHub Actions workflows | [.github/workflows/AGENTS.md](workflows/AGENTS.md) |
| [.github/workflow-templates/](workflow-templates/) | Workflow templates for reuse | — |
| [.github/ISSUE_TEMPLATE/](ISSUE_TEMPLATE/) | Issue templates for bugs/features | — |

## Additional key files

- [.github/copilot-instructions.md](copilot-instructions.md): main coding standards for agents.
- [.github/pull_request_template.md](pull_request_template.md): PR description template.
- [.github/README.template.md](README.template.md): README scaffold for new repos.
- [.github/actionlint-matcher.json](actionlint-matcher.json) and
  [.github/pre-commit-matcher.json](pre-commit-matcher.json): problem matchers used in workflows.

Keep this catalog updated when adding, removing, or renaming folders or agent catalogs.
