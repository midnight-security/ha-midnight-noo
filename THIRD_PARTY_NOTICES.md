# Third-Party Notices

This project vendors source code from other open-source projects. Each is
listed below along with its license and provenance, per the attribution
requirements of the licenses involved.

---

## Alarmo

- **Source:** https://github.com/nielsfaber/alarmo
- **Copyright:** © nielsfaber and Alarmo contributors
- **License:** Apache License, Version 2.0 (same license as this project — see [LICENSE](LICENSE))
- **Vendored at:** [`custom_components/midnight_alerts/vendor/alarmo/`](custom_components/midnight_alerts/vendor/alarmo/) as a **git submodule** tracking the upstream repository directly (see `.gitmodules`)
- **Pinned to:** tag [`v1.10.18`](https://github.com/nielsfaber/alarmo/releases/tag/v1.10.18), commit `b06a42c3f84ddd04833b0bbc088ec873728511cd`
- **Scope:** the submodule contains the *entire* upstream repository (it's not possible to submodule a single subdirectory). Only `custom_components/alarmo/` and `LICENSE` from within it are actually shipped to end users - the release zip build explicitly excludes upstream `tests/`, `screenshots/`, and dev tooling (`pyproject.toml`, `uv.lock`, `pytest.ini`, `.pre-commit-config.yaml`, `DEVELOPMENT.md`) via `-x` flags in `package.json`'s release config and `.github/workflows/release.yml`.
- **Modifications:** none — the submodule is an unmodified checkout of upstream. If this code is later edited, each changed file must carry a notice stating that it was changed, per [License §4(b)](https://www.apache.org/licenses/LICENSE-2.0#redistribution).
- **Trademark note:** "Alarmo" is nielsfaber's project name. The Apache License does not grant trademark rights (§6), so features built on this vendored code should not be marketed under the Alarmo name.

To pull a newer Alarmo release: `cd custom_components/midnight_alerts/vendor/alarmo && git fetch --tags && git checkout <new-tag>`, then commit the updated submodule pointer from the parent repo and update the pinned tag/commit above. Cloning this repository requires `git clone --recurse-submodules` (or `git submodule update --init` after a plain clone) - see `CONTRIBUTING.md`.
