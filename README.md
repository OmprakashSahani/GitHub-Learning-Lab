<div align="center">

# GitHub Learning Lab
### A production-style journey into GitHub workflows, CI/CD, and Python packaging

</div>

---

## Overview

This project is a small Python CLI application built to demonstrate real-world software engineering workflows using GitHub.

It showcases:

- Structured Git workflow (Issue → Branch → PR → Merge)
- CI/CD using GitHub Actions
- Testing, linting, and coverage
- Python packaging with `pyproject.toml`
- Installable CLI tool

---

## Features

- CLI tool: `greet`
- Automated testing with `pytest`
- Linting with `ruff`
- Test coverage (~90%)
- CI pipeline: Lint → Test → Coverage → Build
- Installable Python package
- Clean `src/` project structure

---

## Usage

```bash
pip install -e .
greet Om
```

Output:

```
Hello, Om! Welcome to GitHub.
```

---

## Demo

```bash
$ greet Om
Hello, Om! Welcome to GitHub.

$ greet --help
usage: greet [-h] [name]

Print a GitHub learning greeting.

positional arguments:
  name        Name to include in the greeting

optional arguments:
  -h, --help  show this help message and exit
```

---

## Workflow Summary

```text
Issue → Branch → Code → Commit → PR → CI → Merge → Release
```

- 12+ structured workflows completed
- Covers CI/CD, testing, packaging, and releases
- Mirrors real-world development practices

---

## Completed Workflows

- Workflow 1 — Add Python Script
- Workflow 2 — Add CLI Input
- Workflow 3 — Add Unit Tests
- Workflow 4 — Add GitHub Actions CI
- Workflow 5 — Add Ruff Linting
- Workflow 6 — Add Argparse CLI
- Workflow 7 — Refactor to `src/` Structure
- Workflow 8 — Add Requirements File
- Workflow 9 — Package as Installable CLI
- Workflow 10 — Add Test Coverage (~90%)
- Workflow 11 — Clean Package Metadata
- Workflow 12 — Build Package Artifacts

---

## Project Structure

```
src/
  app/
    greet.py

tests/

.github/
  workflows/

requirements.txt
pyproject.toml
README.md
```

---

## Architecture

```text
CLI (argparse)
      ↓
greet() logic
      ↓
Test layer (pytest)
      ↓
CI pipeline (GitHub Actions)
      ↓
Package build (wheel + sdist)
```

---

## CI Pipeline

```text
Ruff (Lint) → Pytest (Tests) → Coverage → Build
```

Ensures:

- Code quality
- Correctness
- Test completeness
- Build validity

---

## Local Setup

```bash
# Clone repository
git clone https://github.com/OmprakashSahani/github-learning-lab.git
cd github-learning-lab

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
PYTHONPATH=src pytest

# Run CLI
python src/app/greet.py Om
```

---

## Engineering Practices

This project follows:

- Feature-based branching
- Issue-driven development
- CI gating (lint → test → coverage → build)
- Reproducible environments
- Incremental versioning (v0.1.0 → v0.6.0)

---

## Releases

| Version | Description |
|---|---|
| `v0.1.0` | Initial workflow |
| `v0.2.0` | Project structure |
| `v0.3.0` | Documentation |
| `v0.4.0` | Packaging |
| `v0.5.0` | Coverage + metadata |
| `v0.6.0` | Build pipeline |

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make changes
4. Open a pull request

All contributions must pass CI checks.

---

## Future Improvements

- Publish package to PyPI
- Add pre-commit hooks
- Add Docker support
- Extend CLI functionality

---

<div align="center">

*Built with structured workflows, clean commits, and production-style engineering practices.*

</div>
