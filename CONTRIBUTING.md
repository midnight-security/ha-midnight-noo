# Contributing

Thank you for helping improve the Midnight 911 Home Assistant integration.

## Development setup

1. Clone this repository into your Home Assistant `custom_components` path, or symlink `custom_components/midnight_alerts` into a dev instance.
2. Restart Home Assistant and add the integration via **Settings → Devices & services**.

## Branch workflow

- **`develop`** — active development
- **`master`** — production; merges here trigger semantic-release

Open PRs against `develop`. When ready for release, merge `develop` → `master`.

## Commit messages

This project uses [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Version bump |
|--------|--------------|
| `fix:` | Patch |
| `feat:` | Minor |
| `feat!:` or `BREAKING CHANGE:` | Major |
| `docs:`, `chore:`, etc. | No release |

## Validation

CI runs [hassfest](https://github.com/home-assistant/actions/tree/master/hassfest) and [HACS validation](https://github.com/hacs/action) on every push and PR.

Run locally before opening a PR:

```bash
# Requires Docker
docker run --rm -v $(pwd):/github/workspace ghcr.io/home-assistant/hassfest
```

## Security

Do not open public issues for security vulnerabilities. See [SECURITY.md](SECURITY.md).
