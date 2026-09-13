import sqlite3

conn = sqlite3.connect("users.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    email TEXT
)
""")

conn.execute("""
INSERT OR IGNORE INTO users VALUES
(1, 'alice', 'alice@example.com')
""")

conn.execute("""
INSERT OR IGNORE INTO users VALUES
(2, 'bob', 'bob@example.com')
""")

conn.commit()
conn.close()

print("Database initialized")
