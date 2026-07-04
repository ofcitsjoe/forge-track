import sqlite3
import time
from pathlib import Path

DB_PATH = Path("data/tracker.db")

def initialize_db():
    """Creates the database file and the sessions table if they don't already exist."""
    
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                app_name TEXT NOT NULL,
                start_time REAL NOT NULL,
                end_time REAL NOT NULL,
                duration_seconds REAL NOT NULL
            )
        ''')
        conn.commit()
        print("Database initialized successfully.")

def save_session(app_name, start_time, end_time):
    """saves a session record to the database"""

    duration = end_time - start_time

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        cursor.execute('''
                       INSERT INTO sessions (application, start_time, end_time, duration_seconds)
                       VALUES (?, ?, ?, ?)
                ''', (app_name, start_time, end_time, duration))

        conn.commit()
        print(f"Saved session: [{app_name}] for duration {duration:.2f} seconds")

if __name__ == "__main__":
    print("testing database module...")

    initialize_db()

    fake_end_time = time.time()
    fake_start_time = fake_end_time - 120  # Simulate a session of 2 minutes

    save_session("TestApp", fake_start_time, fake_end_time)
    
