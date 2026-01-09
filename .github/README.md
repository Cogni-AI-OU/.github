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
      additional_prompt: 'Focus on performance optimization'
    secrets: inherit
```

The workflow uses Claude Opus 4.5 and focuses on bugs, security vulnerabilities, performance
issues, and missing error handling.

## Workflow Templates

The `workflow-templates/` directory contains reference workflows that are not
actively executed but are preserved for future use or copying to other
repositories. These templates can be customized and moved to the `workflows/`
directory when needed.

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

## Security

### Claude Workflow Git Access

The Claude Code workflow (`claude.yml`) grants intentionally broad git access
via `Bash(git:*)` to enable autonomous code changes. This permission is necessary
for Claude to commit and push changes, but requires proper safeguards.

#### Security Controls

**Access Control:**

- Only trusted users can trigger Claude (OWNER, MEMBER, COLLABORATOR, CONTRIBUTOR)
- PR/issue authors can only trigger on their own content
- External contributors (FIRST_TIME_CONTRIBUTOR, NONE) are explicitly blocked

**Required Repository Protections:**

To safely use Claude with git access, repository administrators must configure:

1. **Branch Protection Rules** on main/protected branches:
   - Require pull request reviews before merging
   - Require status checks to pass (e.g., linting, tests)
   - Require conversation resolution before merging
   - Do not allow bypassing the above settings

2. **GitHub Audit Logs** (organization-level):
   - Enable and regularly review audit logs
   - Monitor commits made by `github-actions[bot]` (Claude's identity)
   - Set up alerts for suspicious patterns (rapid commits, deleted branches, etc.)

3. **Protected Branch Policies**:
   - Restrict who can push to protected branches
   - Consider requiring deployment approvals for production branches
   - Use CODEOWNERS to require specific reviewer approval for sensitive files

#### Best Practices

- Review Claude's commits before merging PRs
- Use draft PRs for Claude's work to require explicit promotion
- Regularly audit Claude's tool usage and permissions
- Rotate `ANTHROPIC_API_KEY` periodically
- Monitor workflow run logs for unexpected behavior

For more details, see [CLAUDE.md](../CLAUDE.md).
