# AGENTS.md

Guidance for Claude automation agents working in this repository.

## Quick Start

- See [README.md](README.md) for setup and installation instructions
- See [.tours/getting-started.tour](.tours/getting-started.tour) for a guided walkthrough
- For enhanced agent capabilities, see [Copilot Plus](.github/agents/copilot-plus.agent.md)

## Instructions

For detailed coding standards and formatting guidelines, refer to:

- [Copilot Instructions](.github/copilot-instructions.md) - Main coding standards
- [Ansible](.github/instructions/ansible.instructions.md) - Ansible conventions
- [JSON](.github/instructions/json.instructions.md) - JSON formatting standards
- [Markdown](.github/instructions/markdown.instructions.md) - Markdown standards
- [YAML](.github/instructions/yaml.instructions.md) - YAML formatting standards

## Common Tasks

### Before the changes

Before committing the new changes, install pre-commit via pip and its hooks by:

```bash
pre-commit install
```

### Linting and Validation

```bash
# Run all pre-commit checks
pre-commit run -a

# Run specific checks
pre-commit run markdownlint -a
pre-commit run yamllint -a
ansible-lint
```

### Testing

```bash
# Run Molecule tests
molecule test

# Syntax check
molecule syntax
```

### Updating Organization Defaults

- Edit files in `.github/ISSUE_TEMPLATE/` to modify issue templates
- Edit `.github/pull_request_template.md` for PR template changes
- Update `profile/README.md` to change the organization's public profile

### Adding or Modifying Workflows

- Workflows in `.github/workflows/` can be reused via `workflow_call`
- Test workflow changes on a feature branch before merging to main
- Use `actionlint` to validate workflow syntax locally

### Updating Coding Standards

- Language-specific instructions are in `.github/instructions/`
- Update `.markdownlint.yaml`, `.yamllint`, or `.editorconfig` for linting rules
- Run `pre-commit run -a` to verify changes pass all checks

## Integrating Changes from Target Branch

When asked to "integrate changes from the target branch" (e.g., `dev` or `main`) into your feature branch,
**DO NOT** use `git merge`. Merging creates a merge commit that includes all commits from the target branch,
making it impossible for reviewers to see only your changes.

### Recommended Approach: Cherry-Pick Your Changes

The correct way to integrate target branch changes is to rebase your commits on top of the updated target branch:

1. **Identify your feature commits**:

   ```bash
   # List commits that are in your branch but not in target
   git log --oneline <target-branch>..HEAD
   
   # Or compare with remote target
   git log --oneline origin/dev..HEAD
   ```

2. **Fetch the latest target branch**:

   ```bash
   git fetch origin <target-branch>
   ```

3. **Reset your branch to target** (creates clean starting point):

   ```bash
   # Create backup first (optional but recommended)
   git tag backup/before-rebase-$(date +%s)
   
   # Reset to target branch
   git reset --hard origin/<target-branch>
   ```

4. **Cherry-pick your feature commits**:

   ```bash
   # Cherry-pick individual commits
   git cherry-pick <commit-1> <commit-2> <commit-3>
   
   # Or use range syntax for many commits
   git cherry-pick <first-commit>^..<last-commit>
   ```

5. **Verify only your changes appear**:

   ```bash
   git diff origin/<target-branch>..HEAD --stat
   git diff origin/<target-branch>..HEAD --name-status
   ```

   The diff should show ONLY files you created or modified, not all files from the target branch.

### Handling Conflicts During Cherry-Pick

If conflicts occur during cherry-picking:

1. **Resolve conflicts** in the files (preserve target branch content and add your changes)
2. **Stage resolved files**: `git add <resolved-files>`
3. **Continue**: Use `GIT_EDITOR=true git cherry-pick --continue` to bypass editor prompts
4. **Or skip**: Use `git cherry-pick --skip` to skip the problematic commit
5. **Or abort**: Use `git cherry-pick --abort` to cancel and start over

### Common Pitfalls to Avoid

- **Using `git merge <target-branch>`**: This includes all target branch commits in your PR,
  making review impossible. Use cherry-pick instead.
- **Force pushing without verification**: Always verify your changes with `git diff` before force pushing.
- **Forgetting to fetch**: Always `git fetch origin <target-branch>` to get the latest changes.
- **Losing work**: Create a backup tag before resetting: `git tag backup/before-rebase-$(date +%s)`

### When Using `report_progress` Tool

**CRITICAL WARNING**: The `report_progress` tool automatically attempts to rebase your branch against the remote
tracking branch. This **WILL CRASH** the session when:

- **You've rewritten history** (e.g., using `git reset --hard` + `git cherry-pick`)
- **Your branch has diverged** from the remote (e.g., after rebasing locally)
- **The remote has many commits** that would trigger rebase conflicts

**The crash occurs because:**

1. `report_progress` switches to your branch
2. It attempts `git rebase origin/<your-branch>` automatically
3. If your local history diverged from remote (e.g., after `git reset --hard`), this creates conflicts
4. The tool cannot resolve conflicts interactively, so it fails and crashes the session

### Prevention Strategies

**Option 1: Use a New Branch Name** (Recommended when history was rewritten)

After using `git reset --hard` and cherry-picking, create a new branch instead of reusing the old one:

```bash
# After your reset + cherry-pick workflow
git checkout -b <feature-name>-rebased

# Now safe to call report_progress - no divergence, no auto-rebase needed
```

This avoids the force-push issue entirely and prevents `report_progress` from attempting to rebase.

**Option 2: Complete Git Operations Before `report_progress`**

If you must reuse the same branch name:

1. Complete all git operations manually (fetch, reset, cherry-pick, verify)
2. **DO NOT** call `report_progress` after `git reset --hard` on a pushed branch
3. Instead, ask the user to manually force-push: `git push --force-with-lease origin <branch-name>`
4. Document what you prepared so the user knows the branch is ready

### If `report_progress` Fails with Rebase Errors

If you already called it and it's failing:

1. **Abort the rebase**: `git rebase --abort`
2. **Verify your local branch is correct**: `git diff origin/<target-branch>..HEAD --stat`
3. **Document what you prepared**: Explain the commits are ready, just need manual push
4. **Ask the user** to push manually: `git push --force-with-lease origin <branch-name>`
5. **Alternative**: Create new branch and push that instead: `git checkout -b <branch>-rebased && git push origin <branch>-rebased`

### Error Pattern Recognition

If you see these errors, you've hit the auto-rebase issue:

- `error: could not apply <commit>...`
- `CONFLICT (content): Merge conflict in <file>`
- `Rebasing (1/XXX)` with many commits (e.g., 113 commits)
- `hint: Resolve all conflicts manually...` followed by crash

### Example: Integrating Dev Changes

```bash
# 1. See what commits you have
git log --oneline origin/dev..HEAD

# 2. Fetch latest dev
git fetch origin dev

# 3. Create backup and reset to dev
git tag backup/before-dev-rebase-$(date +%s)
git reset --hard origin/dev

# 4. Cherry-pick your commits
git cherry-pick abc123 def456 ghi789

# 5. Verify only your changes
git diff origin/dev..HEAD --stat

# 6. Now call report_progress or ask user to push
```

## References

- Org profile and collaboration info: [profile/README.md](profile/README.md)
- Claude-specific guidance: [CLAUDE.md](CLAUDE.md)
- Community standards: [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

## Troubleshooting

### GitHub Build issues

- Use `gh` command to interact with GitHub resources. For example:

  - `gh run list --limit 3` to list recent builds.
  - `gh run view {ID} --log | rg -iw "failed|error|exit"` to look for build errors.

### Firewall issues

If you encounter firewall issues when using the GitHub Copilot Agent:

- Refer to <https://gh.io/copilot/firewall-config> for configuration details.
- If you need to allowlist additional hosts, update your firewall configuration accordingly
  and keep the list of allowed hosts in `.github/agents/FIREWALL.md` up to date.

### Linting issues

If Copilot or automated checks behave unexpectedly:

- Re-run `pre-commit run -a` locally to surface formatting or linting issues.
- Verify `.markdownlint.yaml` and `.yamllint` have not been modified incorrectly.
- If problems persist, open an issue with details of the command run and any error output.

### Shell commands issues

- Prefix shell commands with `time` to measure execution duration for better visibility.
- When command takes too long, use `timeout` or similar approach to limit execution time.
