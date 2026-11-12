import os
import tempfile
import pytest
import app as lab

@pytest.fixture()
def client(monkeypatch):
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    monkeypatch.setattr(lab, "DB_PATH", __import__("pathlib").Path(path))
    lab.init_db()
    lab.app.config.update(TESTING=True, SECRET_KEY="test-secret")
    with lab.app.test_client() as client:
        yield client
    os.unlink(path)

def login(client, username="alice", password="AliceDemo!23"):
    return client.post("/login", data={"username": username, "password": password}, follow_redirects=True)

def test_health_and_security_headers(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert "Content-Security-Policy" in response.headers

def test_secure_search_returns_expected_item(client):
    response = client.get("/secure/search?q=Pen")
    assert response.status_code == 200
    assert b"Pen" in response.data

def test_secure_greeting_escapes_html(client):
    response = client.get("/secure/hello?name=%3Cscript%3Ealert(1)%3C%2Fscript%3E")
    assert response.status_code == 200
    assert b"<script>" not in response.data
    assert b"&lt;script&gt;" in response.data

def test_secure_profile_requires_login(client):
    assert client.get("/secure/profile/1").status_code == 401

def test_user_cannot_read_another_users_profile(client):
    login(client, "alice")
    assert client.get("/secure/profile/2").status_code == 403

def test_admin_can_read_user_profile(client):
    login(client, "admin", "AdminDemo!23")
    assert client.get("/secure/profile/1").status_code == 200

def test_invalid_login_rejected(client):
    assert client.post("/login", data={"username":"alice","password":"wrong"}).status_code == 401
