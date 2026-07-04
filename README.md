# ForgeTrack

A lightweight, automated Windows application that accurately tracks your PC gaming sessions by monitoring the active foreground window. Unlike launcher-based trackers, ForgeTrack only counts time while you're actually playing.

---

## ✨ Features

- **🎮 Active Window Tracking** – Only records playtime when your game is the active foreground window, preventing inflated playtime from Alt-Tabbing or leaving games idle.
- **⚡ Low Resource Footprint** – Runs silently in the background with minimal CPU and memory usage.
- **📝 Whitelist Filtering** – Uses a customizable `config.json` file so only the games you choose are tracked.
- **💾 Local Storage** – Stores all gaming sessions in a local SQLite database. No internet connection or cloud account required.
- **🔒 Privacy First** – Your data never leaves your computer.

---

# 🚀 Download & Usage (Quick Start)

You **do not** need Python or any programming knowledge to use ForgeTrack.

### 1. Download

Download the latest release from the **Releases** page:

> **https://github.com/YOUR_USERNAME/ForgeTrack/releases/latest**

Download **ForgeTrack.exe**.

---

### 2. Setup

Create a folder anywhere on your PC, for example:

```text
Documents/
└── ForgeTrack/
```

Place **ForgeTrack.exe** inside that folder.

---

### 3. Run

Double-click **ForgeTrack.exe**.

The first time it runs, ForgeTrack automatically creates:

```text
config.json
data/
└── tracker.db
```

---

### 4. Configure

Open `config.json` with Notepad.

Example:

```json
{
  "games": ["Hades.exe", "DetroitBecomeHuman.exe", "Stardew Valley.exe"]
}
```

Simply add or remove executable names as needed.

---

### 5. Play

Leave ForgeTrack running in the background.

Whenever one of your configured games becomes the active window, ForgeTrack automatically records your play session.

---

# 🏗️ Architecture

ForgeTrack is built around a simple four-stage pipeline.

### Sensor (`src/os_utils`)

Uses the Windows API to retrieve:

```
HWND
   ↓
PID
   ↓
Executable (.exe)
```

This determines exactly which application is currently active.

---

### Filter (`src/core/config.py`)

Loads your whitelist from `config.json` and ignores everything except the games you've specified.

---

### Memory (`src/storage`)

Uses SQLite to permanently store gaming sessions with:

- Context Managers
- Parameterized SQL Queries
- ACID-compliant persistence

---

### Brain (`src/core/loop.py`)

Coordinates the entire application by:

- Loading configuration
- Initializing the database
- Polling the active window
- Detecting game switches
- Calculating session duration
- Saving completed sessions

---

# 🛠 Tech Stack

- **Language:** Python 3.12+
- **Operating System:** Windows
- **OS Interfacing:** `pywin32`, `psutil`
- **Database:** SQLite3
- **Packaging:** PyInstaller
- **Linting & Formatting:** Ruff

---

# 📁 Folder Structure

```text
ForgeTrack/
├── src/
│   ├── core/          # Main application loop and configuration manager
│   ├── os_utils/      # Windows API interactions
│   └── storage/       # SQLite database layer
├── data/              # Generated local database
├── tests/             # Unit tests
├── config.json        # User whitelist
├── pyproject.toml     # Ruff configuration
├── requirements.txt
└── README.md
```

---

# 👨‍💻 Developer Setup

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/ForgeTrack.git
cd ForgeTrack
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the tracker:

```bash
python -m src.core.loop
```

---

# 📦 Building the Executable

Install PyInstaller:

```bash
pip install pyinstaller
```

Build ForgeTrack:

```powershell
pyinstaller --noconsole --onefile src/core/loop.py
```

The executable will be generated inside:

```text
dist/
└── loop.exe
```

You may rename it to:

```text
ForgeTrack.exe
```

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve ForgeTrack:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.
