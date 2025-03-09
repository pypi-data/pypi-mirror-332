[Compare the full difference.](https://github.com/callowayproject/bump-my-version/compare/1.0.1...1.0.2)

### Fixes

- Fix incorrect evaluation. [3578c87](https://github.com/callowayproject/bump-my-version/commit/3578c872ef8143f11c22cb5e83765c6e69cf3eef)
    
  The check for valid files to add should be `filename`, not `self.files`
- Refactor and improve test structure for file modifications. [8b52174](https://github.com/callowayproject/bump-my-version/commit/8b52174651e3c02daf3ba00166cd8f054498313d)
    
  Consolidated and restructured tests for `modify_files` into classes for better organization and clarity. Fixed an issue where empty file configurations were not properly ignored and enhanced filtering logic in configuration handling.

  Fixes #312
### Other

- Replace `list[str]` with `List[str]` for Python 3.8+ compatibility. [6fb977c](https://github.com/callowayproject/bump-my-version/commit/6fb977ca9144a590153e779c59c4c788efd1442f)
    
  Updated all instances of `list[str]` with the generic `List[str]` from the `typing` module to maintain compatibility with older Python versions (3.8 and earlier). This ensures consistent type annotations across the codebase.

  Fixes #313
- [pre-commit.ci] pre-commit autoupdate. [a057743](https://github.com/callowayproject/bump-my-version/commit/a0577433bd069f47d0e1eb368def4309f931a947)
    
  **updates:** - [github.com/astral-sh/ruff-pre-commit: v0.9.7 → v0.9.9](https://github.com/astral-sh/ruff-pre-commit/compare/v0.9.7...v0.9.9)
