# Copilot Instructions for ... Ops

## Project Overview

TBC

### Getting started

- Refer to the `README.md` in the project root for setup and installation instructions.
- Check also `.tours/getting-started.tour` which provides a guided walkthrough of key project features and structure.

## Coding Standards

### Python

- Use **Python 3.11+**.
- Use `uv` script headers for dependency management:

  ```python
  #!/usr/bin/env -S uv run --script
  # /// script
  # requires-python = ">=3.11"
  # dependencies = [
  #     "xero-python",
  #     "PyYAML",
  # ]
  # ///
  ```

- Follow **PEP 8** style guidelines.
- Use `argparse` for CLI argument parsing.
- Handle `BrokenPipeError` for CLI tools that might be piped to `head` or `grep`.

### TBC API

- Use the TBC SDK.
- Handle API rate limits and errors gracefully.

## Formatting Guidelines

### JSON

Follow the JSON rules in `.github/instructions/json.instructions.md`, which mirror the repository `.editorconfig` configuration.

To test locally, use `jq` for validation or use the VS Code JSON formatter.

### Markdown

Follow the Markdown rules in `.github/instructions/markdown.instructions.md`, which mirror the repository markdownlint configuration.

To test locally, run via `pre-commit run markdownlint -a` or use the VS Code Markdownlint extension.

### YAML

Follow the YAML rules in `./.github/instructions/yaml.instructions.md`, which mirror the repository `.yamllint` configuration.

Notes:

- Project utilizes Codespaces with config at `.devcontainer/devcontainer.json` and requirements at `.devcontainer/requirements.txt`.
- GitHub Actions run pre-commit checks (`.pre-commit-config.yaml`).
- To verify locally, run `pre-commit run yamllint -a` from the repo root.

## Project Structure

TBC

### Tours

- Keep the `.tours` folder up-to-date (especially `.tours/getting-started.tour`)
  when making significant changes to the codebase.
  Update existing tours or create new ones to reflect changes in project structure,
  workflows, or key files.

## Troubleshooting

### Finding Build Errors

To identify and diagnose the latest build errors:

1. **Check GitHub Actions workflow status:**
   - If you have access to GitHub MCP server tools, use `list_workflow_runs` to see recent workflow runs and their status
   - Look for runs with `conclusion: "failure"` or `status: "completed"` with failures
   - Note the `run_id` of failed runs (typically the "Check" workflow)

2. **View detailed error logs:**
   - If you have access to GitHub MCP server tools:
     - Use `get_job_logs` with the `run_id` and `failed_only: true` to get logs for all failed jobs
     - Alternatively, use `list_workflow_jobs` to identify specific failed jobs, then use `get_job_logs`
       with the `job_id` to get detailed logs for a specific job
     - Parse the logs to find error messages and failure patterns
   - If GitHub MCP server is not available, explain that you cannot access the logs

3. **Reproduce errors locally:**
   - For pre-commit errors: Run `pre-commit run -a` to check all files
   - For specific hooks: Run `pre-commit run <hook-name> -a` (e.g., `markdownlint`, `yamllint`)
   - For actionlint errors: Install actionlint and run it on workflow files

4. **Common error patterns:**
   - **Markdown linting errors:** Check `.markdownlint.yaml` for rules; errors show line numbers
   - **YAML linting errors:** Check `.yamllint` for rules; verify indentation and structure
   - **JSON formatting errors:** Use `jq . <file>` to validate JSON syntax

### General Troubleshooting

If Copilot or automated checks behave unexpectedly:

- Re-run `pre-commit run -a` locally to surface formatting or linting issues.
- Verify `.markdownlint.yaml` and `.yamllint` have not been modified incorrectly.
- If problems persist, open an issue with details of the command run and any error output.

## Copilot Agent

- If you encounter firewall issues when using the GitHub Copilot Agent,
  refer to <https://gh.io/copilot/firewall-config> for configuration details.
  If you need to allowlist additional hosts, update your firewall configuration accordingly
  and keep the list of allowed hosts in `.github/agents/FIREWALL.md` up to date.

## Common Tasks

TBC
