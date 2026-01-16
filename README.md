# Code Platoon Alumni Discord Bot

A community-maintained Discord bot for the Code Platoon Alumni server. The bot focuses on:

- **Event announcements** (automatic reminders at creation, 1 week before, 12 hours before, and at start)
- **Monthly event rundown** (post on the 1st of each month with all events and times)
- **Name policy audit** (DM users with rename instructions and a grace-period countdown; auto-kick when grace expires — stateless using join date)

> **Status:** Pre-code planning phase. This repo contains documentation, issues, and contribution guidelines to coordinate work before implementation.

---

## ✨ MVP Scope

### 1) Event Announcements
- Detect **Discord Scheduled Events** create/update/delete.
- Post reminders in a configured channel:
  - At event creation (instant summary)
  - **1 week before** start
  - **12 hours before** start
  - **At event start**

### 2) Monthly Event Rundown
- On the **1st of each month**, post a list of all scheduled events for the month in a configured channel.

### 3) Name Check + DM & Auto-Boot (No Database)
- Run daily or weekly based on config.
- For each non-compliant member:
  - Calculate days since `joinedAt`.
  - If days ≥ grace period (7 days daily / 30 days weekly) → kick and log.
  - Else → DM with policy and remaining days.

---

## 🧩 Slash Commands (planned)
- `/audit run` — run name audit manually
- `/privacy` — show privacy policy link

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

## 🤝 Contributing
**Contributors must be Code Platoon Alumni.** Please read **[CONTRIBUTING.md](CONTRIBUTING.md)** and **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)** before contributing. Good first issues are labeled accordingly.

### Getting Started

**Prerequisites:** [Mise](https://mise.jdx.dev/getting-started.html) installed and functional.

```bash
# Install Python 3.12 + uv via mise
mise install

# Create and activate virtual environment
uv venv
source .venv/bin/activate      # macOS/Linux
# .venv\Scripts\activate.bat   # Windows (cmd)
# .venv\Scripts\Activate.ps1   # Windows (PowerShell)

# Install dependencies in editable mode
uv pip install -e .

# Configure and run
cp .env.example .env           # then add your DISCORD_TOKEN
python -m bot
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed setup instructions.
---

## 🌍 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


---

## 🔒 Privacy

Our privacy policy and data handling practices are detailed in the [PRIVACY.md](PRIVACY.md) file.
This bot is designed to be stateless with minimal data collection.

---

## 🛡️ Security

For information on how to report security vulnerabilities privately, please see our [SECURITY.md](SECURITY.md) file.

---

## 📨 Contact

Have a question or suggestion? Feel free to [open an issue](https://github.com/Code-Platoon-Alumni/CP-Discord-Bot/issues) or reach out via the Discussions tab.

---

## 🏅 Acknowledgments

This project is developed and maintained by Code Platoon Alumni to support our community and automate server management for events, audits, and member engagement.
