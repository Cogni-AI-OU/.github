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

### Updating Organization Defaults

- Edit files in `.github/ISSUE_TEMPLATE/` to modify issue templates
- Edit `.github/pull_request_template.md` for PR template changes
- Update `profile/README.md` to change the organization's public profile

### Adding or Modifying Workflows

- Workflows in `.github/workflows/` can be reused via `workflow_call`
- Test workflow changes on a feature branch before merging to main
- Use `actionlint` to validate workflow syntax locally

### Updating Coding Standards

- Language-specific instructions are in `.github/instructions/`
- Update `.markdownlint.yaml`, `.yamllint`, or `.editorconfig` for linting rules
- Run `pre-commit run -a` to verify changes pass all checks

## References

- Org profile and collaboration info: [profile/README.md](profile/README.md)
- Claude-specific guidance: [CLAUDE.md](CLAUDE.md)
- Community standards: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## Troubleshooting

### Firewall issues

If you encounter firewall issues when using the GitHub Copilot Agent:

- Refer to <https://gh.io/copilot/firewall-config> for configuration details.
- If you need to allowlist additional hosts, update your firewall configuration accordingly
  and keep the list of allowed hosts in `.github/agents/FIREWALL.md` up to date.

### Linting issues

If Copilot or automated checks behave unexpectedly:

- Re-run `pre-commit run -a` locally to surface formatting or linting issues.
- Verify `.markdownlint.yaml` and `.yamllint` have not been modified incorrectly.
- If problems persist, open an issue with details of the command run and any error output.

### Shell commands issues

- Prefix shell commands with `time` to measure execution duration for better visibility.
- When command takes too long, use `timeout` or similar approach to limit execution time.
