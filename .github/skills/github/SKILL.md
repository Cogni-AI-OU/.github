<!-- markdownlint-disable MD022 MD026 MD041 -->
---
name: github-actions-failure-debugging
description: Guide for debugging failing GitHub Actions workflows. Use this when asked to debug failing GitHub Actions workflows
---

To debug failing GitHub Actions workflows in a pull request, follow this process using tools from the GitHub MCP Server:

1. Use the `list_workflow_runs` tool to look up recent workflow runs for the pull request and their status
2. Use the `summarize_job_log_failures` tool to get an AI summary of failed job logs, avoiding large context windows
3. For more details, use `get_job_logs` or `get_workflow_run_logs` to get full failure logs
4. Reproduce the failure in your environment
5. Fix the build. Ensure it's fixed before committing if reproduced
