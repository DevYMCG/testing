import json

def test_create_item(client):
    data = {
        "title": "Item2",
        "description": "description"
    }

    response = client.post("/items", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["title"] == "Item2"