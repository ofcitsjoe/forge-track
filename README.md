# ForgeTrack

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Python](https://img.shields.io/badge/python-3.12+-blue)

A lightweight, privacy-first Windows application that automatically tracks your PC gaming sessions by monitoring the active foreground window. Unlike launcher-based trackers, ForgeTrack only records time while you're actually playing.

---

## 📋 Table of Contents

1. [About the Project](#-about-the-project)
2. [Features](#-features)
3. [Architecture](#-architecture)
4. [Tech Stack](#-tech-stack)
5. [Installation](#-installation)
6. [Usage](#-usage)
7. [Developer Setup](#-developer-setup)
8. [Building the Executable](#-building-the-executable)
9. [Roadmap](#-roadmap)
10. [Contributing](#-contributing)
11. [License](#-license)

---

# 🎯 About the Project

Most game launchers measure how long a game is open—not how long it's actually being played. This often leads to inflated playtime whenever the game is left idle or minimized.

**ForgeTrack** solves this by monitoring the active foreground window and only recording playtime while your game is actually in focus.

All tracking is performed locally using native Windows APIs and SQLite. No cloud services, user accounts, or internet connection are required.

**Key highlights:**

- 🎮 Tracks only active gameplay
- 🔒 100% local with no data collection
- ⚡ Lightweight background application
- 💾 Stores sessions in a local SQLite database
- 📄 Simple JSON configuration
- 📦 Distributed as a standalone executable

---

# ✨ Features

- 🎮 **Active Window Tracking** — Records playtime only while your game is the active foreground window.
- ⚡ **Low Resource Usage** — Runs quietly in the background with minimal CPU and memory usage.
- 📝 **Whitelist Configuration** — Track only the games you choose using `config.json`.
- 💾 **Local SQLite Storage** — Gaming sessions remain entirely on your computer.
- 🔒 **Privacy First** — No telemetry, analytics, accounts, or internet connectivity required.

---

# 🏗️ Architecture

```text
Active Window
      │
      ▼
Windows API
      │
      ▼
Executable Detection
      │
      ▼
Whitelist Filter
      │
      ▼
Session Tracking
      │
      ▼
SQLite Database
```

*All processing occurs locally. No information is transmitted outside your computer.*

---

# 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.12+ |
| Platform | Windows |
| OS Integration | pywin32, psutil |
| Database | SQLite3 |
| Packaging | PyInstaller |
| Formatting & Linting | Ruff |

---

# 🚀 Installation

## Prerequisites

- Windows 10 or later
- Git (for developers)

---

## Option 1 — Download (Recommended)

Download the latest release from GitHub.

👉 **https://github.com/ofcitsjoe/forge-track/releases/latest**

Download:

```
ForgeTrack.exe
```

Place it inside any folder, for example:

```text
Documents/
└── ForgeTrack/
```

Double-click **ForgeTrack.exe** to start tracking.

---

## Option 2 — Build from Source

Clone the repository:

```bash
git clone https://github.com/ofcitsjoe/forge-track.git
cd forge-track
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

# 📝 Usage

When ForgeTrack starts for the first time, it automatically creates:

```text
config.json

data/
└── tracker.db
```

Open `config.json` and add the executables you want to track.

Example:

```json
{
  "games": [
    "Hades.exe",
    "DetroitBecomeHuman.exe",
    "Stardew Valley.exe"
  ]
}
```

Leave ForgeTrack running in the background.

Whenever one of the configured games becomes the active foreground window, the application automatically records:

- Game executable
- Session start time
- Session end time
- Session duration

To stop ForgeTrack completely, open **Task Manager** and end the **ForgeTrack** process.

---

## Viewing Your Data

ForgeTrack stores all sessions inside:

```text
data/
└── tracker.db
```

To inspect the database:

1. Install **DB Browser for SQLite**
2. Open `tracker.db`
3. Browse the `sessions` table

Everything remains stored locally on your computer.

---

# 👨‍💻 Developer Setup

Clone the repository:

```bash
git clone https://github.com/ofcitsjoe/forge-track.git
cd forge-track
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

# 📦 Building the Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build ForgeTrack:

```powershell
pyinstaller --noconsole --onefile --name ForgeTrack main.py
```

The executable will be generated inside:

```text
dist/
└── ForgeTrack.exe
```

---

# 🔭 Roadmap

- [ ] Dashboard application
- [ ] Daily, weekly, and monthly statistics
- [ ] CSV export
- [ ] Automatic updates
- [ ] Game artwork and icons
- [ ] Configurable polling interval
- [ ] Pause tracking hotkey
- [ ] Multi-language support

---

# 🤝 Contributing

Contributions are always welcome!

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

# 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

<p align="center">
Built with ❤️ for gamers who want accurate, launcher-independent playtime tracking.
</p>
