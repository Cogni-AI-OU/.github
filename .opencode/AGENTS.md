# OpenCode Agents

## Directory-Specific Agent files

- [`agents/AGENTS.md`](agents/AGENTS.md)

## Permissions & Consistency

- Keep command permissions synchronized across all OpenCode surfaces:
  `.opencode/opencode.jsonc` (`permission.bash`),
  `.vscode/settings.json` (`chat.tools.terminal.autoApprove`), and workflow
  `OPENCODE_PERMISSION` blocks in `.github/workflows/opencode.yml` and
  `.github/workflows/opencode-review.yml`.
- Any allow/deny command change in one surface MUST be mirrored in the other
  three in the same update.
