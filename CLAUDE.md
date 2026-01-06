# CLAUDE.md

This file provides Claude Code-specific guidance. For general agent instructions,
see [AGENTS.md](AGENTS.md).

## Claude Code Configuration

Claude Code is configured via GitHub Actions workflows in this repository.
The primary workflow is [.github/workflows/claude.yml](.github/workflows/claude.yml).

### Environment Variables

- `ANTHROPIC_API_KEY`: API key for Claude (stored as repository secret)
- `ALLOWED_TOOLS`: Comma-separated list of tools Claude can use

### Model Selection

By default, workflows use `claude-opus-4-5`. To change the model, update the
`--model` argument in the workflow's `claude_args`.

## Tools

Claude Code provides access to various tools for interacting with the repository
and environment.

### Allowed Tools

The allowed tools are defined in workflow files under the `ALLOWED_TOOLS`
environment variable. Current categories include:

- **Git operations**: `Bash(git:*)`
- **GitHub CLI**: `Bash(gh issue:*)`, `Bash(gh pr:*)`, `Bash(gh search:*)`
- **Data processing**: `Bash(jq:*)`, `Bash(yq:*)`

If you need a tool that isn't in the allowed tools list, suggest adding it to
the relevant workflow file in `.github/workflows/`.

### Model Context Protocol (MCP)

MCP servers extend Claude's capabilities with additional tools and integrations.
When MCP is enabled via `--mcp-config`, you gain access to:

- GitHub API integrations (issues, PRs, repositories)
- External service integrations
- Custom tool implementations

MCP configuration is specified in workflow files using JSON format.

## Prompting Best Practices

When working with Claude in this repository:

- Reference `AGENTS.md` for coding standards and formatting rules
- Run `pre-commit run -a` before finalizing changes
- Keep responses concise; avoid restating obvious context
- Focus on actionable issues rather than stylistic preferences

## Troubleshooting

### Common Issues

1. **Tool not allowed**: Check if the tool is in `ALLOWED_TOOLS`; request addition
   via PR if needed.
2. **Linting failures**: Run `pre-commit run -a` locally to identify issues before
   committing.
3. **MCP connection errors**: Verify the MCP server URL and authentication in
   workflow configuration.
