import os
from app import app

def test_root_returns_default_message():
    # ensure GREETING is not set
    if "GREETING" in os.environ:
        del os.environ["GREETING"]
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello, World from DevOps!" in resp.data

def test_root_respects_env_override(monkeypatch):
    monkeypatch.setenv("GREETING", "Hi from env")
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hi from env" in resp.data