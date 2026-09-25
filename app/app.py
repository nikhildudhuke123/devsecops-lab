from flask import Flask, request
import sqlite3

app = Flask(__name__)

class RemoveServerHeaderMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        def custom_start_response(status, headers, exc_info=None):
            headers = [(k, v) for k, v in headers if k.lower() != "server"]
            return start_response(status, headers, exc_info)
        return self.app(environ, custom_start_response)

app.wsgi_app = RemoveServerHeaderMiddleware(app.wsgi_app)

@app.after_request
def add_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'; form-action 'none'; base-uri 'none'"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    response.headers["Cross-Origin-Resource-Policy"] = "same-origin"
    response.headers["Cache-Control"] = "no-store"
    response.headers.pop("Server", None)
    return response

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
    app.run(host="0.0.0.0", port=5000)  # nosemgrep: python.flask.security.audit.app-run-param-config.avoid_app_run_with_bad_host
