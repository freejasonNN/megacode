# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added

- Public repository URL references updated to
  `https://github.com/mitkox/megacode`.
- `--fast-mode` profile and `--overview-top-files` controls for small-context
  local model deployments.
- Progress heartbeat logging during long-running RLM attempts.
- Backward-compatible `limit_files` alias for `list_manifest`.
- `SKILL.md` for agent-based skill consumption (Claude Code/OpenCode style).

### Changed

- Strengthened RLM instructions toward strict tool-only repository access.
- Improved manifest ranking to prioritize code-centric extensions.
- README and contribution docs updated to match latest CLI/runtime behavior.

## [0.2.0] - 2026-02-08

### Added

- GitHub open-source scaffolding:
  - `README.md`
  - `LICENSE` (MIT)
  - `CONTRIBUTING.md`
  - `SECURITY.md`
  - `CODE_OF_CONDUCT.md`
  - CI workflow and issue/PR templates
- Packaging improvements in `pyproject.toml`:
  - explicit build system
  - console script entrypoint
  - project metadata/classifiers/URLs
  - pytest configuration
- Basic unit tests for manifest/path/tool helpers.

### Changed

- Dependency floor updated to `dspy-ai>=3.1.3`.
