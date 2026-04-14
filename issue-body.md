### Description
We should add a CodeQL Security Scan workflow to automatically analyze our codebase for security vulnerabilities. This enhances our CI pipeline's security posture by running static analysis on pull requests and scheduled runs.

### Additional information
**Proposal**:
- Create a new GitHub Action workflow (`.github/workflows/codeql-analysis.yml`).
- Configure it to trigger on `push` and `pull_request` to the `main` branch, as well as on a schedule (e.g., weekly).
- Use `github/codeql-action/init`, `github/codeql-action/autobuild`, and `github/codeql-action/analyze` to perform the scanning.
- Set the appropriate permissions, notably `security-events: write` to upload the SARIF results.

**Example Workflow**:
```yaml
name: "CodeQL"

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  schedule:
    - cron: '30 1 * * 0'

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write

    strategy:
      fail-fast: false
      matrix:
        language: [ 'javascript', 'python' ]

    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Initialize CodeQL
      uses: github/codeql-action/init@v3
      with:
        languages: ${{ matrix.language }}

    - name: Autobuild
      uses: github/codeql-action/autobuild@v3

    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v3
```