from flask import Flask, request, session, redirect, url_for, render_template_string, abort, g
import sqlite3
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.update(
    SECRET_KEY="LOCAL-DEMO-ONLY-CHANGE-ME",
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=False,  # localhost HTTP lab only; use True behind HTTPS in production
)
DB_PATH = Path(__file__).with_name("lab.db")

def db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(_error=None):
    conn = g.pop("db", None)
    if conn is not None:
        conn.close()

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL, role TEXT NOT NULL)""")
        count = conn.execute("SELECT COUNT(*) FROM users").fetchone()[0]
        if count == 0:
            conn.executemany(
                "INSERT INTO users(username,password_hash,role) VALUES(?,?,?)",
                [
                    ("alice", generate_password_hash("AliceDemo!23"), "user"),
                    ("admin", generate_password_hash("AdminDemo!23"), "admin"),
                ],
            )
        conn.execute("""CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL)""")
        pcount = conn.execute("SELECT COUNT(*) FROM products").fetchone()[0]
        if pcount == 0:
            conn.executemany("INSERT INTO products(name,category) VALUES(?,?)", [
                ("Notebook", "Stationery"), ("Pen", "Stationery"), ("Mug", "Home")
            ])

@app.after_request
def security_headers(response):
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "DENY")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    response.headers.setdefault("Content-Security-Policy", "default-src 'self'; object-src 'none'; base-uri 'self'; frame-ancestors 'none'")
    return response

@app.route("/")
def home():
    return """
    <h1>Web Application Security Local Lab</h1>
    <p>Use dummy data and localhost only. Vulnerable routes are intentionally unsafe.</p>
    <ul>
      <li><a href="/secure/search?q=Pen">Secure search</a></li>
      <li><a href="/secure/hello?name=Student">Secure greeting</a></li>
      <li><a href="/login">Login</a></li>
    </ul>
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return """<form method="post">
        <input name="username" placeholder="username">
        <input name="password" type="password" placeholder="password">
        <button>Login</button></form>"""
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    user = db().execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
    if user and check_password_hash(user["password_hash"], password):
        session.clear()  # prevents session fixation by issuing a fresh session
        session["user_id"] = user["id"]
        session["username"] = user["username"]
        session["role"] = user["role"]
        return redirect(url_for("home"))
    return "Invalid username or password", 401

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

# Deliberately vulnerable: unsafe string concatenation. Local dummy DB only.
@app.route("/lab/vulnerable/search")
def vulnerable_search():
    q = request.args.get("q", "")
    sql = "SELECT id, name, category FROM products WHERE name LIKE '%" + q + "%'"
    try:
        rows = db().execute(sql).fetchall()
        return "<h2>Vulnerable search results</h2>" + "".join(
            f"<p>{row['id']}: {row['name']} ({row['category']})</p>" for row in rows
        )
    except sqlite3.Error:
        return "Database query error", 400

# Safer counterpart: parameterized query; template engine escapes values by default.
@app.route("/secure/search")
def secure_search():
    q = request.args.get("q", "")[:100]
    rows = db().execute(
        "SELECT id, name, category FROM products WHERE name LIKE ?",
        (f"%{q}%",)
    ).fetchall()
    return render_template_string(
        "<h2>Secure search results</h2>{% for row in rows %}"
        "<p>{{ row['id'] }}: {{ row['name'] }} ({{ row['category'] }})</p>"
        "{% else %}<p>No results</p>{% endfor %}", rows=rows
    )

# Deliberately vulnerable: unescaped user-controlled HTML.
@app.route("/lab/vulnerable/hello")
def vulnerable_hello():
    name = request.args.get("name", "visitor")
    return f"<h1>Hello {name}</h1>"

# Safer counterpart: Jinja auto-escaping.
@app.route("/secure/hello")
def secure_hello():
    name = request.args.get("name", "visitor")[:80]
    return render_template_string("<h1>Hello {{ name }}</h1>", name=name)

def current_user():
    if "user_id" not in session:
        return None
    return db().execute("SELECT * FROM users WHERE id = ?", (session["user_id"],)).fetchone()

# Deliberately vulnerable: trusts the requested object ID without authorization.
@app.route("/lab/vulnerable/profile/<int:user_id>")
def vulnerable_profile(user_id):
    row = db().execute("SELECT id, username, role FROM users WHERE id = ?", (user_id,)).fetchone()
    if not row:
        abort(404)
    return f"<p>Profile: {row['username']} (role: {row['role']})</p>"

# Safer counterpart: requires login and enforces owner-or-admin authorization.
@app.route("/secure/profile/<int:user_id>")
def secure_profile(user_id):
    actor = current_user()
    if actor is None:
        abort(401)
    if actor["id"] != user_id and actor["role"] != "admin":
        abort(403)
    row = db().execute("SELECT id, username, role FROM users WHERE id = ?", (user_id,)).fetchone()
    if not row:
        abort(404)
    return render_template_string("<p>Profile: {{ row['username'] }} (role: {{ row['role'] }})</p>", row=row)

@app.route("/health")
def health():
    return {"status": "ok", "environment": "local-lab"}

if __name__ == "__main__":
    init_db()
    # Bind only to loopback. Do not change to 0.0.0.0.
    app.run(host="127.0.0.1", port=5000, debug=False)
