# .github/

This directory contains organization-wide defaults, templates, workflows, instructions,
prompts, skills, and AI agent configurations for the Cogni AI OÜ organization.

## AI Agents & MCP Configuration

The `.github/mcp-config.json` configuration provides GitHub Copilot access to built-in tools:

- **Repository & Code:** `get_file_contents`, `search_code`, `search_repositories`,
  `list_branches`, `list_commits`
- **Issues & PRs:** `get_issue`, `list_pull_requests`, `create_pull_request`
- **Actions:** `list_workflows`, `list_workflow_runs`, `get_job_logs`

For more details, see the [main repository README](../README.md).
