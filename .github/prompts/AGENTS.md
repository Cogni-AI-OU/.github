# Prompt Catalog for Agents

Authoritative list of prompts in this directory. Use these entries for loading prompts in workflows or
agent sessions, and keep the catalog in sync with files on disk.

For a human-readable overview, see [README.md](README.md).

## Prompts

| Prompt | Format | Purpose |
| ------ | ------ | ------- |
| [default.prompt.yml](default.prompt.yml) | YAML | General-purpose system prompt for code help, reviews, and repo management |
| [repository-setup.prompt.md](repository-setup.prompt.md) | Markdown | Full repository setup checklist using org standards from Cogni-AI-OU/.github |
| [test.prompt.yml](test.prompt.yml) | YAML | Minimal example prompt for testing message structure |

## Notes

- Use Markdown prompts for human-readable checklists and structured guidance.
- Use YAML prompts for GitHub Models or programmatic consumption.
- Update this catalog whenever prompts are added, removed, or renamed.

## Usage

- For GitHub Models, load YAML prompts directly; for chat agents, paste Markdown prompt content.
- Keep prompts in sync with this catalog when creating or removing files.
