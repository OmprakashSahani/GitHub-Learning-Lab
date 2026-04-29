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
