from flask import Flask, request
import sqlite3

app = Flask(__name__)

DATABASE = "users.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn


@app.route("/")
def home():
    return {
        "application": "DevSecOps Lab",
        "status": "running"
    }


@app.route("/api/user")
def get_user():
    user_id = request.args.get("id")

    conn = get_db()

    query = "SELECT id, username, email FROM users WHERE id = ?"

    result = conn.execute(query, (user_id,)).fetchall()

    conn.close()

    return {
        "users": [
            {
                "id": row[0],
                "username": row[1],
                "email": row[2]
            }
            for row in result
        ]
    }


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
