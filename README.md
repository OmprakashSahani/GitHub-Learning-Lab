# GitHub Learning Lab

This repository is my structured journey to learn GitHub from scratch.

---

## Objective

Learn and apply:

- Git basics (commit, branch, merge)
- GitHub workflow (PR, Issues)
- Clean project structure
- CI/CD using GitHub Actions

---

## GitHub Features Explained

### 1. Repository
A repository is a central place where code, documentation, and history are stored.

---

### 2. Commit
A commit is a snapshot of changes made to files.

Each commit should have a clear message describing what changed.

Example:
- feat: add new feature
- fix: resolve bug
- docs: update documentation

---

### 3. Branch
A branch is an isolated environment to work on changes without affecting the main codebase.

- `main` → stable code
- `feature/...` → new work

---

### 4. Pull Request (PR)
A pull request is used to propose changes from one branch to another.

It allows:
- Code review
- Discussion
- Validation before merging

---

### 5. Merge
Merging combines changes from a branch into `main`.

---

### 6. Issues
Issues are used to track tasks, bugs, or ideas.

Example:
- Add feature
- Fix bug
- Improve documentation

---

### 7. GitHub Actions (CI/CD)
GitHub Actions automate tasks like:

- Running code
- Testing
- Deployment

This is called Continuous Integration (CI).

---

## Step 1: Repository Initialization

- Created repository
- Added `.gitignore`
- Created README.md

---

## Approach

I will follow this workflow:

1. Create a feature branch
2. Make changes
3. Commit with proper message
4. Create Pull Request
5. Merge into main

---

## Goal

Build strong understanding of real-world GitHub workflows.

---

## Completed Workflow 1: Add Python Script

### Issue
Created Issue #3 to track the task before writing code.

### Branch
Created a branch from the issue:

`3-add-a-simple-python-script`

### Code Change
Added `hello.py` with a basic `greet()` function.

### Pull Request
Opened a pull request to merge the feature branch into `main`.

### Merge
Merged the pull request after reviewing the change.

### Cleanup
Deleted the feature branch after merge.

### Result
Issue #3 was automatically closed using `Closes #3`.

---

## Completed Workflow 2: Add Command-Line Input

### Issue
Created Issue #4 to enhance functionality.

### Branch
Created branch:

`4-add-command-line-input-support`

### Code Change
Updated `hello.py` to accept input from command line using `sys.argv`.

### Example Usage
```bash
python hello.py Om
```
### Output
Hello, Om! Welcome to GitHub.

### Pull Request
Opened PR and linked it using Closes #4.

### Merge
Merged changes into main.

### Cleanup
Deleted branch after merge.

### Result
Issue #4 closed automatically.

---

## Completed Workflow 3: Add Unit Test

### Issue
Created Issue #5 to introduce testing.

### Branch
Created branch:

`5-add-unit-test-for-greet-function`

### Code Change
Added test file:

`tests/test_greet.py`

### Test Logic
```python
from hello import greet

def test_greet():
    assert greet("Om") == "Hello, Om! Welcome to GitHub."
```
### Pull Request
Opened PR and linked using Closes #5.

### Merge
Merged into main.

### Cleanup
Deleted branch after merge.

### Result
Issue #5 closed automatically.

---

## Completed Workflow 4: Add GitHub Actions CI

### Issue
Created Issue #6 to add automated testing.

### Branch
Created branch:

`6-add-github-actions-test-workflow`

### Code Change
Added GitHub Actions workflow:

`.github/workflows/python-tests.yml`

### CI Workflow
The workflow runs on:

- Push
- Pull Request

### Debugging
The first CI run failed because Python could not import `hello`.

Fixed it by adding:

```bash
PYTHONPATH=. pytest
```
### Result
GitHub Actions now automatically runs tests successfully.

---

## Completed Workflow 5: Add Ruff Linting

### Issue
Created Issue #7 to improve code quality.

### Branch
Created branch:

`7-add-ruff-linting`

### Code Change
Added Ruff configuration:

`pyproject.toml`

### CI Enhancement
Updated GitHub Actions to include:

- Ruff lint check
- Pytest execution

### Pipeline
```text
Lint → Test → Merge
```

### Result
Code quality and correctness are automatically validated on every change.

### Commit message:
docs: document linting workflow

---

## Completed Workflow 6: Add Argparse CLI

### Issue
Created Issue #8 to improve command-line interface.

### Branch
Created branch:

`8-add-argparse-based-cli`

### Code Change
Replaced manual `sys.argv` handling with Python `argparse`.

### CLI Usage
```bash
python hello.py Om
```
### Help Command
python hello.py --help

### Result
The script now has a cleaner CLI structure with built-in help support.

---

## Completed Workflow 7: Refactor to `src/` Structure

### Issue
Created Issue #9 to restructure the project.

### Branch
Created a feature branch for the refactor.

### Code Change
Moved application code from root-level `hello.py` into:

`src/app/greet.py`

### Test Update
Updated test imports from:

```python
from hello import greet
to
from app.greet import greet
```
### CI Update
Updated GitHub Actions test command:
PYTHONPATH=src pytest

### Result
The project now follows a cleaner Python src/ layout.

---

## Completed Workflow 8: Add Requirements File

### Issue
Created Issue #10 to track dependencies.

### Branch
Created feature branch for requirements.

### Code Change
Added:

`requirements.txt`

### Dependencies
- pytest
- ruff

### Usage
Install dependencies:

```bash
pip install -r requirements.txt
```
### Result
Project is now reproducible with defined dependencies.

---

## Local Setup

### 1. Clone repository
```bash
git clone https://github.com/OmprakashSahani/github-learning-lab.git
cd github-learning-lab
```
### 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run tests
PYTHONPATH=src pytest

### 5. Run CLI
python src/app/greet.py Om

---
> Setup instructions verified and tested.

---

## Completed Workflow 9: Package as Installable CLI

### Issue
Created Issue #12 to convert project into a package.

### Branch
Created packaging branch.

### Code Changes
- Added `src/app/__init__.py`
- Updated `pyproject.toml`
- Defined CLI entry point

### CLI Command
After installation:

```bash
pip install -e .
greet Om
```
### CI Update
Updated GitHub Actions to install the package before running tests.

### Result
The project is now installable and runnable as a CLI tool.

---
