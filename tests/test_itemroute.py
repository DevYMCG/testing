import json

def test_create_item(client):
    data = {
        "title": "Item4",
        "description": "description"
    }

    response = client.post("/items", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["title"] == "Item4"

def test_retrieve_item_by_id(client):
    response = client.get("/item/1")
    assert response.status_code == 200