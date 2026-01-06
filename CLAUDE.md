# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Quick Start

- See [README.md](README.md) for setup and installation instructions
- See [.tours/getting-started.tour](.tours/getting-started.tour) for a guided walkthrough

## Instructions

For detailed coding standards and formatting guidelines, refer to:

- [Copilot Instructions](.github/copilot-instructions.md) - Main coding standards
- [Ansible](.github/instructions/ansible.instructions.md) - Ansible conventions
- [JSON](.github/instructions/json.instructions.md) - JSON formatting standards
- [Markdown](.github/instructions/markdown.instructions.md) - Markdown standards
- [YAML](.github/instructions/yaml.instructions.md) - YAML formatting standards

## Common Tasks

### Linting and Validation

```bash
# Run all pre-commit checks
pre-commit run -a

# Run specific checks
pre-commit run markdownlint -a
pre-commit run yamllint -a
ansible-lint
```

### Testing

```bash
# Run Molecule tests
molecule test

# Syntax check
molecule syntax
```

## Tools

Claude Code provides access to various tools for interacting with the repository and environment.

### Model Context Protocol (MCP)

MCP servers can be enabled to extend Claude's capabilities with additional tools and integrations.
If MCP is enabled, you'll have access to specialized tools for:

- External service integrations
- Enhanced development workflows
- Custom tool implementations

### Allowed Tools

If you need a tool that isn't in the allowed tools list, suggest adding it to
[.github/workflows/claude.yml](.github/workflows/claude.yml) in the `ALLOWED_TOOLS` environment variable.
