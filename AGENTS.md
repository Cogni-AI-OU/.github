# AGENTS.md

Guidance for Claude automation agents working in this repository.

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

### Before the changes

Before committing the new changes, install pre-commit via pip and its hooks by:

```bash
pre-commit install
```

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

## References

- Org profile and collaboration info: [profile/README.md](profile/README.md)
- Claude-specific guidance: [CLAUDE.md](CLAUDE.md)
- Community standards: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
