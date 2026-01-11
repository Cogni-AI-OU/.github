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

## GitHub Actions

For documentation on GitHub Actions workflows, problem matchers, and CI/CD
configuration, see [.github/README.template.md](.github/README.template.md).

## AI Agents and Skills

This repository includes enhanced AI agent configurations and skills for automated
development tasks:

- **[Copilot Plus Agent](.github/agents/copilot-plus.agent.md)**: Enhanced agent
  with critical thinking, robust problem-solving, and context-aware resource
  management
- **[Agent Skills](.github/skills/)**: Specialized skills for git operations,
  GitHub Actions debugging, context-aware operations, and robust command execution

For complete agent documentation, see [AGENTS.md](AGENTS.md).

## Agentic Files and Configurations

This repository contains multiple files and directories for configuring AI agents.
Here's what each one does:

### Root-Level Agent Files

- **[AGENTS.md](AGENTS.md)**: Project-specific tips, best practices, and common
  tasks for agents working in this repository. Read by all AI agents.
- **[CLAUDE.md](CLAUDE.md)**: Claude-specific configuration including triggers,
  tools, and workflow settings. Read by Claude agents.
- **[README.md](README.md)**: High-level project overview, setup instructions,
  and usage guide for all users (humans and agents).

### .github/copilot-instructions.md

General coding standards, project structure, and troubleshooting guidance. Read
by GitHub Copilot (including VS Code extension and GitHub UI).

### .github/ Subdirectories

- **[agents/](.github/agents/)**: Specialized agent configurations for specific
  tasks (e.g., code tours, DevOps, Terraform, research). Each `.agent.md` file
  defines a custom agent with tailored prompts and capabilities.
- **[skills/](.github/skills/)**: Reusable agent skills that provide specialized
  capabilities like git operations, GitHub Actions debugging, and context-aware
  resource management.
- **[prompts/](.github/prompts/)**: Prompt templates for common automation tasks
  (e.g., repository setup).
- **[instructions/](.github/instructions/)**: Language-specific coding standards
  and formatting rules (e.g., Python, Markdown, YAML, JSON, Ansible). Applied by
  linters and followed by agents when writing code.

### Quick Reference

| File/Directory | Primary Audience | Purpose |
| -------------- | ---------------- | ------- |
| AGENTS.md | All AI agents | Repository-specific guidance and workflows |
| CLAUDE.md | Claude agents | Claude-specific configuration |
| README.md | Humans and agents | Project overview and setup |
| .github/copilot-instructions.md | GitHub Copilot | Coding standards and project context |
| .github/agents/ | Agent orchestrators | Specialized agent configurations |
| .github/skills/ | All AI agents | Reusable capabilities and tools |
| .github/prompts/ | Humans and agents | Automation prompt templates |
| .github/instructions/ | Linters and agents | Language-specific code standards |

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
