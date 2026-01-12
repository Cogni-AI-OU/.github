# Cogni AI OÜ - Organization Configuration

[![PR Reviews][pr-reviews-image]][pr-reviews-link]
[![License][license-image]][license-link]

This is a special `.github` repository that provides default community health
files and configurations for all repositories in the Cogni AI OÜ organization.

## What is a .github Repository?

The `.github` repository is a special GitHub repository that serves as a central
location for organization-wide defaults. It automatically provides community
health files (like issue templates, code of conduct, contributing guidelines,
etc.) to any repository in the organization that doesn't have its own versions.

### Key Features

- **Default Issue Templates**: Standardized bug reports, feature requests, and
  other issue types
- **Code of Conduct**: Organization-wide behavioral standards
- **Contributing Guidelines**: How to contribute to projects
- **Security Policies**: Instructions for reporting vulnerabilities
- **Pull Request Templates**: Standardized PR descriptions
- **GitHub Actions Workflows**: Reusable CI/CD and automation workflows
- **Organization Profile**: Public-facing information via `profile/README.md`
- **AI Agent Configurations**: Enhanced agents and skills for automated development

### How It Works

1. Files in individual repositories' `.github/` directories take precedence over
   these defaults
2. If a repository doesn't have a specific file, GitHub falls back to this
   repository
3. Changes here automatically apply organization-wide

## Development

### Setup

```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Install Python dependencies (for devcontainer)
pip install -r .devcontainer/requirements.txt
```

### Testing and Validation

```bash
# Run all pre-commit checks
pre-commit run -a

# Run specific checks
pre-commit run markdownlint -a
pre-commit run yamllint -a
pre-commit run black -a
pre-commit run flake8 -a
```

## AI Agents

This repository provides AI agent configurations for automated development.

### Agent Configuration Files

| File/Directory | Audience | Purpose |
| -------------- | -------- | ------- |
| [AGENTS.md](AGENTS.md) | All agents | Repository-specific guidance and workflows |
| [CLAUDE.md](CLAUDE.md) | Claude | Claude-specific configuration |
| [.github/copilot-instructions.md](.github/copilot-instructions.md) | Copilot | Coding standards and project context |
| [.github/agents/](.github/agents/) | Orchestrators | Specialized agent configs for specific tasks |
| [.github/skills/](.github/skills/) | All agents | Reusable capabilities (git, GitHub Actions, etc.) |
| [.github/prompts/](.github/prompts/) | All | Automation prompt templates (`.md` for VS Code, `.yaml` for GitHub Models) |
| [.github/instructions/](.github/instructions/) | Linters & agents | Language-specific code standards |

See also:

- [`AGENTS.md` file format specification](https://agents.md/)
- [Best practices for using GitHub Copilot](https://gh.io/copilot-coding-agent-tips).

## GitHub Actions

For documentation on GitHub Actions workflows, problem matchers, and CI/CD
configuration, see [.github/README.template.md](.github/README.template.md).

## Organization Profile

For information about Cogni AI OÜ, our mission, and how to collaborate, see our
[organization profile](profile/README.md).

## References

- [How to Use the .github Repository](https://www.freecodecamp.org/news/how-to-use-the-dot-github-repository/)
- [Creating a Default Community Health File](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)

## License

MIT

See: [LICENSE](./LICENSE)

<!-- Named links -->

[pr-reviews-image]: https://img.shields.io/github/issues-pr/Cogni-AI-OU/.github?label=PR+Reviews&logo=github
[pr-reviews-link]: https://github.com/Cogni-AI-OU/.github/pulls
[license-image]: https://img.shields.io/badge/License-MIT-blue.svg
[license-link]: https://tldrlegal.com/license/mit-license
