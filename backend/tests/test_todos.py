from app.main import create_app

def test_create_todo():
    app = create_app()
    client = app.test_client()

    response = client.post("/todos/", json={"title": "Test Task"})
    assert response.status_code == 201
    assert response.json["title"] == "Test Task"


def test_get_todos():
    app = create_app()
    client = app.test_client()

    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json, list)
