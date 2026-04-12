# OpenCode Agents

## Directory-Specific Agent files

- [`agents/AGENTS.md`](agents/AGENTS.md)

## Permissions & Consistency

- The shell permissions list in `.opencode/opencode.jsonc` (`permission.bash`)
  MUST be kept in sync with the allowlist in `.vscode/settings.json` for consistency.
- Keep the same command set in workflow `OPENCODE_PERMISSION` blocks in
  `.github/workflows/opencode.yml` and `.github/workflows/opencode-review.yml`.
