# ForgeTrack

A lightweight, automated system monitoring agent for tracking PC gaming sessions without the overhead and inaccuracies of traditional launcher-based trackers.

## Features

- **Active Window Tracking:** Only tracks time when the game is the foreground window (fixes the "Alt-Tab" inflated playtime issue).
- **Low Resource Footprint:** Designed to run silently in the background with near-zero CPU usage.

## Tech Stack

- **Language:** Python 3.12+
- **OS Interfacing:** `pywin32`, `psutil`
- **Linting & Formatting:** Ruff

## Folder Structure

\`\`\`text
ForgeTrack/
├── src/
│ ├── core/ # Core event loop and orchestration (WIP)
│ ├── os_utils/ # Windows API interactions (Sensor)
│ └── storage/ # SQLite database logic (WIP)
├── data/ # Local database storage
└── tests/ # Unit tests
\`\`\`

## Installation & Setup

1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `.\venv\Scripts\Activate.ps1`
4. Install dependencies: `pip install -r requirements.txt`

## Architecture

Currently implemented: The Sensor Layer.

- Extracts `HWND` (Window Handle) -> `PID` (Process ID) -> `.exe` (Executable Name).

Currently implemented: The Sensor Layer & Core Loop.

- **The Sensor (`src/os_utils`):** Extracts `HWND` (Window Handle) -> `PID` (Process ID) -> `.exe` (Executable Name).
- **The Brain (`src/core`):** An infinite polling loop that manages application state. It detects state transitions (window changes), calculates elapsed time using UNIX timestamps, and mitigates CPU load using sleep intervals.

Currently implemented: The Sensor, The Brain, and The Memory.

- **The Sensor (`src/os_utils`):** Extracts `HWND` (Window Handle) -> `PID` (Process ID) -> `.exe` (Executable Name).
- **The Brain (`src/core`):** An infinite polling loop that manages application state. It detects state transitions (window changes), calculates elapsed time using UNIX timestamps, and mitigates CPU load using sleep intervals.
- **The Memory (`src/storage`):** An embedded SQLite database that permanently stores gaming sessions. It uses Python Context Managers (`with`) for safe file locks and SQL Parameterization (`?`) to prevent SQL injection.

Currently implemented: Fully Integrated Tracker Pipeline.

- **The Sensor (`src/os_utils`):** Extracts `HWND` (Window Handle) -> `PID` (Process ID) -> `.exe` (Executable Name).
- **The Memory (`src/storage`):** An embedded SQLite database that permanently stores gaming sessions, utilizing Context Managers and parameterized queries.
- **The Brain (`src/core`):** The orchestrator. It bootstraps the database on startup, polls the Sensor every 2 seconds, calculates elapsed time on state transitions, and seamlessly pipelines the data into the Memory layer, including a graceful shutdown trap to catch the final session.
