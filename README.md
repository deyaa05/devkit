# devkit 

AI-powered developer toolkit — wraps GitHub CLI, GitHub Copilot CLI and Git into one seamless command.

## Installation

```bash
pip install -e .
```

## Commands

### GitHub operations
```bash
devkit gh issues                        # List open issues in a rich table
devkit gh issues --repo cli/cli         # List issues from any repo
devkit gh pr-summary <number>           # Show PR title, body and changed files
devkit gh open-pr                       # Create a pull request interactively
devkit gh run-status                    # Show latest CI run status
```

### AI tools
```bash
devkit ai explain "git rebase -i HEAD~3"   # Explain a shell command
devkit ai suggest "find python files"       # Suggest a command for a task
devkit ai review <pr-number>               # AI code review of a PR
devkit ai commit                           # Generate commit message from staged diff
```

### Workflows
```bash
devkit workflow feature-start <name>            # Create branch + push + draft PR
devkit workflow feature-start <name> --issue 5  # Same + AI implementation plan
```

## Demo

[![devkit demo](https://asciinema.org/a/QmINTuDP80LhJkFx.svg)](https://asciinema.org/a/QmINTuDP80LhJkFx)

### 1. List open issues
```bash
devkit gh issues --repo cli/cli
```

### 2. PR overview
```bash
devkit gh pr-summary 1 --repo cli/cli
```

### 3. Start a feature with AI scaffold
```bash
devkit workflow feature-start my-feature --issue 5
```

### 4. AI commit message
```bash
git add .
devkit ai commit
```

### 5. Explain a command
```bash
devkit ai explain "git rebase -i HEAD~3"
```

## Project structure


devkit/
├── src/devkit/
│   ├── commands/
│   │   ├── github.py     # Phase 2 — GitHub commands
│   │   ├── ai.py         # Phase 3 — AI commands
│   │   └── workflow.py   # Phase 4 — Orchestration
│   ├── utils/
│   │   ├── gh.py         # gh subprocess wrapper
│   │   └── check.py      # Tool availability checker
│   ├── config.py         # User preferences
│   └── main.py           # CLI entry point
├── pyproject.toml
└── README.md

## Requirements

- Python 3.10+
- [GitHub CLI](https://cli.github.com) — `gh auth login`
- GitHub Copilot CLI — included in `gh` v2.89+