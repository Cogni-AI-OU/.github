# VS Code Agents

## Permissions & Consistency

- Keep command permissions synchronized across all OpenCode surfaces:
  `.vscode/settings.json` (`chat.tools.terminal.autoApprove`),
  `.opencode/opencode.jsonc` (`permission.bash`), and workflow
  `OPENCODE_PERMISSION` blocks in `.github/workflows/opencode.yml`.
- Any allow/deny command change in one surface MUST be mirrored in the other
  three in the same update.
- The list of tool keys in these files MUST be kept in strict alphabetical order.
