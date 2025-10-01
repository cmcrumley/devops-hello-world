from app import app

def test_root_returns_hello_world():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello, World from DevOps!" in resp.data