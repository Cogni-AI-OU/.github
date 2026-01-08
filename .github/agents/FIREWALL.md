# Firewall Allowlist for Copilot Agents

If your agent runs behind a restrictive firewall, allow these hosts. Always check the official guidance for updates.

## Important Note

Even with firewall allowlist configuration, some network environments use DNS monitoring proxies that may block
direct API calls (e.g., `curl https://api.github.com/...`). In such cases, **always use the `gh` CLI tool** to
interact with GitHub resources instead of direct HTTP requests. The `gh` CLI is designed to work better in
restricted network environments and provides proper authentication handling.

```plaintext
api.github.com
codeload.github.com
ghcr.io
github.com
npm.pkg.github.com
objects.githubusercontent.com
pkg-containers.githubusercontent.com
raw.githubusercontent.com
registry.npmjs.org
uploads.github.com
user-images.githubusercontent.com
```

Note: Keep the list sorted alphabetically for easier maintenance.

Reference: <https://gh.io/copilot/firewall-config>
