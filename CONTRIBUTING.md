# CONTRIBUTING

Thanks for helping build the Code Platoon Alumni Discord Bot!

> **⚠️ Important:** This project is limited to **Code Platoon Alumni only**. You must be a graduate of Code Platoon to contribute to this repository.

---

## 📜 Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md).
By participating in this project, you agree to abide by its terms.

---

## How to contribute
1. **Request assignment** before starting work:
   - Comment on the issue you want to work on with "I'd like to work on this"
   - Wait for a maintainer to assign you to the issue
   - Issues will be assigned on a first-come, first-served basis
2. **Fork** the repo and create a feature branch after being assigned.
3. Keep PRs **small and focused**. Include rationale and screenshots for docs/UI-related changes.
4. Write clear commit messages (e.g., `docs: add README section for stateless audits`).

## Ground rules
- **Request assignment first** - Don't start work without being assigned to an issue
- Follow the **Code of Conduct**.
- Avoid committing secrets.
- Prefer issues before large changes for alignment.
- Reference related issues in your PR description.
- If you're assigned to an issue but can't complete it, please comment to let maintainers know so it can be reassigned.

---

## 📋 Issue Assignment Process

### For Contributors:
1. **Verify eligibility** - Ensure you are a Code Platoon Alumni
2. **Browse available issues** - Look for issues labeled `good first issue` or `help wanted`
3. **Request assignment** - Comment "I'd like to work on this" on the issue
4. **Wait for assignment** - A maintainer will assign you and may provide additional context
5. **Work on your assigned issue** - Create your fork and feature branch after assignment
6. **Submit your PR** - Reference the issue number in your PR description using #issueNumber

### For Maintainers:
- **Verify contributor eligibility** - Confirm contributors are Code Platoon Alumni before assignment
- Assign issues promptly to requesting contributors
- Provide clear acceptance criteria and context when assigning
- Use issue labels to indicate status: `assigned`
- Reassign stale issues after 7 days of inactivity (with notice to the assignee)

---

## 🧱 Tech Stack
- **Language:** Python 3.12
- **Discord SDK:** `discord.py` (2.x) [Docs Here](https://discordpy.readthedocs.io/en/stable/intro.html)
- **Scheduler:** `apscheduler` (for cron-like jobs)
- **Persistence:** None (stateless audits based on join date)
- **Hosting:** Pending (AWS? Digital Ocean? Options Abound.)
- **Config:** `.env` + `python-dotenv`
- **Logging:** `post to logging channel`
- **Testing:** `pytest`
- **CI:** GitHub Actions (lint, test)

---

## 🧭 Repo Layout
```
/ (root)
  ├─ .github/
  │   ├─ PULL_REQUEST_TEMPLATE.md
  │   ├─ ISSUE_TEMPLATE/
  │   │   ├─ bug_report.yml
  │   │   ├─ feature_request.yml
  │   │   └─ task.yml
  │   └─ workflows/
  │       ├─ project-issues.yml
  │       ├─ project-prs.yml
  │       └─ ci.yml (to be added)
  ├─ src/
  │   └─ bot/
  │       ├─ __init__.py
  │       ├─ __main__.py    # Entry point
  │       ├─ app.py         # Discord client
  │       └─ config.py      # Environment loading
  ├─ tests/
  │       ├─ __init__.py
  │       ├─ test_app.py
  │       └─ test_config.py
  ├─ .env.example
  ├─ .gitignore
  ├─ .pre-commit-config.yaml
  ├─ CODE_OF_CONDUCT.md
  ├─ CONTRIBUTING.md
  ├─ LICENSE
  ├─ mise.toml
  ├─ PRIVACY.md
  ├─ pyproject.toml
  ├─ README.md
  ├─ requirements.txt
  └─ SECURITY.md
```

---

## 🚀 Getting Started

> **Note:** This project is designed to work on both Windows and macOS/Linux. Commands are provided for both where they differ.

### Prerequisites

| Tool | Purpose | Install |
|------|---------|---------|
| [Mise](https://mise.jdx.dev/getting-started.html) | Manages Python version + uv automatically | See mise docs |
| Git | Version control | You probably have this |

> **Why mise + uv?** Mise ensures everyone uses the same Python version (3.12) without "works on my machine" issues.

> UV is a fast, modern pip replacement. Both are defined in `mise.toml` so contributors don't need to manually install uv - `mise install` handles it.

Roughly you'll need to install mise, then activate it in your terminal of choice. The docs are a great reference if trouble is encountered.
```bash
brew install mise # Mac
winget install jdx.mise # Powershell
# Activate mise for your env:
echo 'eval "$(mise activate zsh)"' >> ~/.zshrc # zsh
# Or Powershell:
$shimPath = "$env:USERPROFILE\AppData\Local\mise\shims"
$currentPath = [Environment]::GetEnvironmentVariable('Path', 'User')
$newPath = $currentPath + ";" + $shimPath
[Environment]::SetEnvironmentVariable('Path', $newPath, 'User')

mise -v # -> Should see mise splash screen in terminal of choice.
```

### First-Time Setup

**1. Fork and clone the repo**

**2. Install toolchain (Python 3.12 + uv)**
```bash
mise install
uv venv
uv pip install -e .
```

**3. Activate the virtual environment**
| OS | Command |
|----|---------|
| Windows (cmd) | `.venv\Scripts\activate.bat` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |
| macOS / Linux | `source .venv/bin/activate` |
> Uv should handle this implicitly, but you might still need it. Check uv docs if issues arise.

**4. Install dependencies**
```bash
uv pip install -e . # Runner/deployed env can stop here
uv pip install -e ".[dev]" # Brings in the dev deps, like pre-commit
pre-commit install # Installs the hooks so they 'just work' :tm:
```
This installs the project in editable mode using `pyproject.toml`, which includes all dependencies.

**5. Copy Env File**
```bash
cp .env.example .env           # then add your DISCORD_TOKEN
```

**6. Configure environment**

| OS | Command |
|----|---------|
| Windows (cmd) | `copy .env.example .env` |
| Windows (PowerShell) | `Copy-Item .env.example .env` |
| macOS / Linux | `cp .env.example .env` |

Edit `.env` and add your `DISCORD_TOKEN`. See [Discord Developer Portal](https://discord.com/developers/applications) to create a bot.

**7. Run it!**
```bash
python -m bot
```
You should see: `READY: YourBot#1234`

---

## 📂 Issue Templates
*(bug_report.yml, feature_request.yml, task.yml — same as current version)*

---

## 🗓️ Roadmap
- [x] Python project init + `discord.py` client
- [ ] Slash command registration
- [ ] Event announcement listeners
- [ ] Monthly rundown job
- [ ] Stateless name policy audit job
- [ ] DM templates and kicking workflow
- [x] CI pipeline setup
- [ ] Dockerfile and deploy docs

---

## 🔐 Security & Privacy
- Never commit secrets; use environment variables.
- Scope the bot token to least privileges.
- Avoid storing DM contents.
- Provide a `/privacy` command and a `PRIVACY.md`.
