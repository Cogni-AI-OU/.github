# Custom Agents

This folder contains custom agents designed to enhance your development workflow.
These agents are tailored to specific tasks and integrate seamlessly with GitHub Copilot and MCP servers.

## Featured Agent

**[Copilot Plus](copilot-plus.agent.md)** - Enhanced agent with critical thinking, robust problem-solving,
and context-aware resource management. Features:

- Automatic file size checking before viewing
- Smart filtering for long outputs
- Command installation fallback logic
- Self-improvement capabilities
- Never-give-up problem-solving approach

## How to Use Custom Agents

### Installation

- Download the desired agent configuration file (`*.agent.md`) and add it to your repository.
- Use the Copilot CLI for local testing: [Copilot CLI](https://gh.io/customagents/cli).

## Reference for configuring custom agents

For more details, see the [About](https://gh.io/customagents) and
[Custom Agents Documentation](https://gh.io/customagents/config).

Additional documentation:

- [About custom agents](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-custom-agents)
- [Create custom agents](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents)

For a collection of awesome custom agents, visit the
[GitHub Awesome Copilot repository](https://github.com/github/awesome-copilot).

For information on supported AI models, see
[Supported Models](https://docs.github.com/en/copilot/reference/ai-models/supported-models).

## Customizing the development environment

See: [Customizing the development environment for GitHub Copilot coding agent][customize-env].

## Firewall

See: [Customizing or disabling the firewall for GitHub Copilot coding agent][firewall-config].

### Firewall allowlist

See [FIREWALL.md](FIREWALL.md) for recommended hosts to allow and the official guidance link.

<!-- Named links -->

[customize-env]: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment
[firewall-config]: https://gh.io/copilot/firewall-config

### MCP Server Setup

Some agents require MCP servers to function. The Claude Code Action provides
built-in MCP servers for GitHub operations (`github_comment` and
`github_inline_comment`).

#### Custom MCP Servers

You can add custom MCP servers for additional integrations. There are two ways
to configure MCP servers:

**Method 1: Inline configuration (recommended for simple setups)**

Pass MCP config directly in the workflow file using `--mcp-config`:

```yaml
claude_args: |
  --model claude-opus-4-5
  --mcp-config '{
    "mcpServers": {
      "server_name": {
        "command": "node",
        "args": ["path/to/server.js"],
        "env": {
          "API_KEY": "${{ secrets.API_KEY }}"
        }
      }
    }
  }'
```

**Method 2: File-based configuration**

Create `.github/mcp-config.json` and reference it in your workflow:

```json
{
  "mcpServers": {
    "server_name": {
      "command": "node",
      "args": ["path/to/server.js"],
      "env": {
        "API_KEY": "..."
      }
    }
  }
}
```

Then reference it in `claude_args`:

```yaml
claude_args: |
  --model claude-opus-4-5
  --mcp-config-file .github/mcp-config.json
```

**Important notes:**

- File-based config cannot use GitHub Actions secrets (`${{ secrets.* }}`). Use
  inline config for secrets.
- HTTP-based MCP servers (using `"type": "http"`) may work with inline config
  but can fail with file-based config due to how the Claude Code process loads
  external files.
- The config file in this repository is currently empty (`{"mcpServers": {}}`)
  as the built-in servers are sufficient for GitHub operations.

Follow the instructions in the agent's documentation to configure the necessary MCP servers.

### Activation

- Merge the agent configuration file into the default branch of your repository.
- Access installed agents through the VS Code Chat interface, Copilot CLI, or assign them in CCA.

## Security Considerations

### Claude Code Agent Git Access

When using Claude Code (triggered via `@claude` in comments), the agent has broad
git access via `Bash(git:*)` to enable autonomous code changes. This requires
proper repository safeguards.

**Access controls in place:**

- Only trusted users (OWNER, MEMBER, COLLABORATOR, CONTRIBUTOR) can trigger Claude
- PR/issue authors can only trigger Claude on their own content
- External contributors are explicitly blocked

**Required repository protections:**

Repository administrators must configure:

1. **Branch protection rules** on main/protected branches requiring PR reviews
   and status checks
2. **GitHub audit log monitoring** for `github-actions[bot]` commit activity
3. **CODEOWNERS** files for sensitive directories requiring specific approvals

**Best practices:**

- Review Claude's commits before merging PRs
- Use draft PRs for Claude's work requiring explicit promotion
- Monitor workflow logs for unexpected behavior
- Rotate `ANTHROPIC_API_KEY` periodically

See [.github/README.md](../README.md#security) for detailed security configuration.

## Troubleshooting

### Claude Not Responding to Comments

If Claude isn't responding to your comments, verify:

1. **Permissions**: You must have one of these roles:
   - Repository OWNER, MEMBER, COLLABORATOR, or CONTRIBUTOR
   - PR/issue author (on your own content only)

2. **Trigger conditions** for PR review comments:
   - Your comment contains `@claude`, OR
   - You're replying to a comment from `github-actions[bot]` (Claude's responses), OR
   - You're replying to a comment that contains `@claude`

The workflow uses a two-stage filter to prevent abuse while allowing natural
conversation flow. Check the [Actions tab](../../actions) for workflow run details
if Claude doesn't respond as expected.
