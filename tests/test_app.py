from app.app import app


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home():
    res = client().get("/")
    assert res.status_code == 200
    assert b"Hello" in res.data


def test_health():
    res = client().get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}
