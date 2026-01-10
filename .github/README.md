# GitHub Workflows and Actions

This directory contains GitHub Actions workflows and related configuration.

## Active Workflows

### Claude Code Review (`claude-review.yml`)

Automated and manual PR code review workflow using Claude AI.

**Automatic Triggers:**

- Runs automatically on pull request open/sync events
- Skips bot-authored PRs to avoid review loops

**Manual Trigger (workflow_dispatch):**

Users can manually trigger reviews via the GitHub Actions UI:

1. Navigate to Actions → "Claude Code Review"
2. Click "Run workflow"
3. Provide required inputs:
   - **pr_number** (required): Pull request number to review (e.g., 123)
   - **model** (optional): Claude model to use (default: claude-opus-4-5)
     - `claude-opus-4-5`: Most capable model, best for complex reviews
     - `claude-sonnet-4-5`: Balanced performance and cost
     - `claude-haiku-4-5`: Fastest and most cost-effective
   - **additional_prompt** (optional): Custom instructions appended to the base review prompt
     (e.g., "Focus on SQL injection vulnerabilities in authentication")

**Reusable Workflow (workflow_call):**

Can be called from other workflows:

```yaml
jobs:
  custom-review:
    uses: ./.github/workflows/claude-review.yml
    with:
      pr_number: ${{ github.event.pull_request.number }}  # Optional if called with pull_request event
      model: 'claude-sonnet-4-5'  # Optional, defaults to claude-opus-4-5
      additional_prompt: 'Focus on performance optimization'
    secrets: inherit
```

The workflow focuses on bugs, security vulnerabilities, performance issues, and missing error handling.

## Problem Matchers

GitHub Actions problem matchers automatically annotate files with errors and
warnings in pull requests, making it easier to identify and fix issues.

### Available Matchers

- **actionlint-matcher.json**: Captures errors from actionlint workflow linting
- **pre-commit-matcher.json**: Captures errors from pre-commit hooks

### Pre-commit Problem Matcher

The pre-commit problem matcher supports two output formats:

1. **Generic format** (`file:line:col: message`): Used by flake8, actionlint,
   and other tools that provide column information
2. **No-column format** (`file:line message`): Used by markdownlint and other
   tools that only provide line numbers

Note: Some hooks like yamllint and ansible-lint already output GitHub Actions
annotations directly and don't need the problem matcher.

### Configuration

Problem matchers are registered in the `.github/workflows/check.yml` workflow
before running the corresponding tools.
