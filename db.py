import sqlite3
from datetime import datetime

DB_PATH = "../data/research.db"

def save_topic_ideas(text):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS topic_ideas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT,
        created_at TEXT
    )
    """)

    cur.execute("""
    INSERT INTO topic_ideas (content, created_at)
    VALUES (?, ?)
    """, (text, datetime.utcnow().isoformat()))

    conn.commit()
    conn.close()