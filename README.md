# Cogni AI OÜ - Organization Configuration

This is a special `.github` repository that provides default community health
files and configurations for all repositories in the Cogni AI OÜ organization.

## What is a .github Repository?

The `.github` repository is a special GitHub repository that serves as a central
location for organization-wide defaults. It automatically provides community
health files (like issue templates, code of conduct, contributing guidelines,
etc.) to any repository in the organization that doesn't have its own versions.

### Key Features

- **Default Issue Templates**: Standardized bug reports, feature requests, and
  other issue types
- **Code of Conduct**: Organization-wide behavioral standards
- **Contributing Guidelines**: How to contribute to projects
- **Security Policies**: Instructions for reporting vulnerabilities
- **Pull Request Templates**: Standardized PR descriptions
- **GitHub Actions Workflows**: Reusable CI/CD and automation workflows
- **Organization Profile**: Public-facing information via `profile/README.md`

### How It Works

1. Files in individual repositories' `.github/` directories take precedence over
   these defaults
2. If a repository doesn't have a specific file, GitHub falls back to this
   repository
3. Changes here automatically apply organization-wide

## Organization Profile

For information about Cogni AI OÜ, our mission, and how to collaborate, see our
[organization profile](profile/README.md).

## References

- [How to Use the .github Repository](https://www.freecodecamp.org/news/how-to-use-the-dot-github-repository/)
- [Creating a Default Community Health File](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
