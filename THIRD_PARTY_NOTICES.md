# Third-Party Notices

This project vendors source code from other open-source projects. Each is
listed below along with its license and provenance, per the attribution
requirements of the licenses involved.

---

## Alarmo

- **Source:** https://github.com/nielsfaber/alarmo
- **Copyright:** © nielsfaber and Alarmo contributors
- **License:** Apache License, Version 2.0 (same license as this project — see [LICENSE](LICENSE))
- **Vendored at:** [`custom_components/midnight_alerts/vendor/alarmo/`](custom_components/midnight_alerts/vendor/alarmo/)
- **Pinned to:** tag [`v1.10.18`](https://github.com/nielsfaber/alarmo/releases/tag/v1.10.18), commit `b06a42c3f84ddd04833b0bbc088ec873728511cd`
- **Scope:** `custom_components/alarmo/` and `LICENSE` from the upstream repository only. Upstream `tests/`, `screenshots/`, and dev tooling (`pyproject.toml`, `uv.lock`, `pytest.ini`, `.pre-commit-config.yaml`, `DEVELOPMENT.md`) were not imported.
- **Modifications:** none — imported unmodified. If this code is later edited, each changed file must carry a notice stating that it was changed, per [License §4(b)](https://www.apache.org/licenses/LICENSE-2.0#redistribution).
- **Trademark note:** "Alarmo" is nielsfaber's project name. The Apache License does not grant trademark rights (§6), so features built on this vendored code should not be marketed under the Alarmo name.

To pull a newer Alarmo release, repeat the filtered-import process against the
new tag and re-merge into `custom_components/midnight_alerts/vendor/alarmo/`,
updating the pinned tag/commit above.
