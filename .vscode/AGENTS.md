# VS Code Agents

## Permissions & Consistency

- The shell permissions list in `.vscode/settings.json`
  MUST be kept in sync with the allowlist in `.opencode/opencode.jsonc` (`permission.bash`) for consistency.
- Keep the same command set in workflow `OPENCODE_PERMISSION` blocks in
  `.github/workflows/opencode.yml` and `.github/workflows/opencode-review.yml`.
