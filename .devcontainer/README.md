# Claude Code Sandbox — Dev Container

A VS Code dev container that runs Claude Code in a sandboxed environment:
- **Filesystem isolation**: only your repo is mounted; host files are invisible to the agent
- **Network restriction**: outbound traffic is allowlisted to the Anthropic API, npm, and GitHub only
- **Non-root user**: Claude runs as `vscode`, not root
- **Persistent auth**: Claude credentials survive container rebuilds via a named Docker volume

## Files

```
.devcontainer/
├── devcontainer.json   # Container config: mounts, features, VS Code extensions
├── Dockerfile          # Base image + iptables/ipset/dnsutils
├── init-firewall.sh    # Outbound network allowlist (runs before workspace opens)
└── README.md           # This file
```

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (or Docker Engine on Linux)
- VS Code with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- An Anthropic account (Claude Code will prompt you to log in on first run)

## Usage

1. Copy `.devcontainer/` into your repo root.
2. Open the repo in VS Code.
3. When prompted, click **Reopen in Container** (or run `Dev Containers: Reopen in Container` from the Command Palette).
4. Wait for the container to build and the firewall script to run.
5. Open a terminal and run `claude` to authenticate on first use.

## Customising the network allowlist

Edit the `ALLOWED_DOMAINS` array in `init-firewall.sh`.

Common additions depending on your stack:

```bash
# PyPI (Python projects)
"pypi.org"
"files.pythonhosted.org"

# Docker Hub (if agent pulls images)
"registry-1.docker.io"
"auth.docker.io"

# Your private package registry
"npm.your-org.com"
```

After editing, rebuild the container:
`Dev Containers: Rebuild Container` from the Command Palette.

## Persisting Claude auth across rebuilds

The `claude-code-config-${devcontainerId}` Docker volume stores your credentials
and settings. It survives `Rebuild Container` but is removed by
`Dev Containers: Clean Up Dev Containers` or manual `docker volume rm`.

To pre-authenticate without interactive login (useful for CI or team rollouts):

```bash
# On your host, generate a token once:
claude setup-token

# Add to your shell profile or .env:
export CLAUDE_CODE_OAUTH_TOKEN=sk-ant-oat01-...
```

Then add to `devcontainer.json`:
```json
"containerEnv": {
  "CLAUDE_CODE_OAUTH_TOKEN": "${localEnv:CLAUDE_CODE_OAUTH_TOKEN}"
}
```

## Known limitations

- **Selection context**: passing selected editor lines to Claude via the sidebar
  panel has a known bug in devcontainer environments. Use `@filename` references
  as a workaround. Tracked at: https://github.com/anthropics/claude-code/issues/14153
