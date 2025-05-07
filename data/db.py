# data/db.py
import sqlite3
import os

DB_PATH = "data/sessions.db"

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT,
            session_type TEXT,
            start_time TEXT,
            duration INTEGER
        )
    ''')
    conn.commit()
    conn.close()

from datetime import datetime

def log_session(task: str, session_type: str, start_time: datetime, duration: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sessions (task, session_type, start_time, duration) VALUES (?, ?, ?, ?)",
        (task, session_type, start_time.isoformat(), duration)
    )
    conn.commit()
    conn.close()
































































