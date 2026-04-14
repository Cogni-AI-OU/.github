# OpenCode Directories

OpenCode (if installed), it uses XDG base directories (not a single `~/.opencode` dir):

| Directory                 | Purpose                                                |
| ------------------------- | ------------------------------------------------------ |
| `~/.local/share/opencode` | Data **and** auth credentials (`auth.json` lives here) |
| `~/.config/opencode`      | User configuration (`opencode.json`/`opencode.jsonc`)  |
| `~/.cache/opencode`       | Ephemeral binary cache - not worth persisting          |
| `~/.local/state/opencode` | Runtime state - not worth persisting                   |
