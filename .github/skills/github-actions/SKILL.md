<!-- markdownlint-disable MD013 MD022 MD026 MD041 -->
---
name: github-actions
description: Diagnose GitHub Actions workflow failures by retrieving run statuses and logs using MCP tools or gh CLI.
---

This skill enables autonomous diagnosis of GitHub Actions failures, preferring MCP tools for summaries and falling back to gh CLI.

When to Activate
----------------

- User reports a failing GitHub Actions workflow, CI failure, or red status check
- Pull request shows failed Actions checks
- Task requires identifying or fixing a workflow failure
- Error output references Actions job steps

Step-by-Step Process
--------------------

1. Detect available tools for diagnosis.

   First, check for gh CLI: run_in_terminal `gh --version`.
   If successful, verify access: run_in_terminal `gh auth status`.
   Prioritize MCP tools (e.g., `list_workflow_runs`, `summarize_job_log_failures`) if present — they provide the most token-efficient summaries.
   If neither MCP nor authenticated gh is available, respond: 'Automated retrieval of workflow logs is not possible in this environment. Please share the workflow run URL, specific error messages, or screenshots for diagnosis.'

2. Preferred path: Use MCP tools (if available).

   - Invoke `list_workflow_runs` with filters (current branch, PR number, or workflow name if known) to find recent runs.
   - Identify failed runs (`conclusion: "failure"`). Note the latest `run_id`.
   - Invoke `summarize_job_log_failures(run_id=RUN_ID)` for concise AI summary of failures.
   - If more detail needed: invoke `list_workflow_jobs(run_id=RUN_ID)` → target failed `job_id`(s) → `get_job_logs(job_id=JOB_ID)`.
   - Parse summary/logs for failing step, command, and error message.

3. Fallback path: Use gh CLI (if available and authenticated).

   - Run_in_terminal `gh run list --limit 20` (adds `--branch $(git rev-parse --abbrev-ref HEAD)` if needed).
   - Identify the most recent failed `run_id` from output.
   - Run_in_terminal `gh run view <run_id> --log-failed` to get only failed job logs (avoids full output).
   - If more context needed: `gh run view <run_id> --log | grep -EC 10 -i 'error|failed|exception|traceback|exit code [1-9][0-9]*'`.
   - If ripgrep available: `gh run view <run_id> --log-failed | rg -i -C 10 "failed|error|exception|exit"`.
   - Capture and analyze output for root cause.

4. With evidence from either path:

   - Trace error to specific step, dependency, environment, or configuration issue.
   - Correlate with common patterns (version mismatch, missing secret, cache failure, flaky test, timeout).
   - Propose precise code or workflow fixes.
   - If reproducible locally, recommend `act -j <job>` for validation.

5. Before committing fixes, verify logically against observed error. Stage changes and re-run verification if possible.

Finding Build Issues via `gh` Command
-------------------------------------

- Use `gh` command to interact with GitHub resources. For example:
  - `gh run list --limit 3` to list recent builds.
  - `gh run view <run_id> --log-failed` to view only failed job logs.
  - `gh run view <run_id> --log | rg -iw "failed|error|exit"` to search full logs for key terms.

Useful Diagnostic Commands
--------------------------

**MCP tools (preferred):**

- `list_workflow_runs(pull_request=PR_NUMBER)` or branch-filtered
- `summarize_job_log_failures(run_id=RUN_ID)`
- `get_job_logs(job_id=JOB_ID)`

**gh CLI (fallback):**

```bash
gh --version                          # Check availability
gh auth status                        # Verify login and repo access
gh run list --limit 20                # List recent runs
gh run view <run_id> --log-failed     # Failed jobs only (recommended first)
gh run view <run_id> --log | grep -C 10 -i "error\|failed\|exit code"
```

What to Avoid
-------------

- Never fetch full raw logs first — always use summaries (`summarize_job_log_failures`) or `--log-failed`
- Do not guess causes without log evidence
- Avoid modifying workflow YAML unless failure clearly originates there
- Do not trigger re-runs or external commands unless explicitly safety-checked

Limitations
-----------

- MCP tools require server access and may not be available in all environments
- gh CLI requires installation, authentication, and repository access (limited on public repos without login)
- Private secrets are always redacted in logs
- Large log output may truncate in terminal — prioritize failed-only retrieval
- Cannot trigger new workflow runs autonomously
