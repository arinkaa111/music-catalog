def test_create_artist(client):
    response = client.post(
        "/api/artists/",
        json={"name": "Radiohead", "country": "UK", "description": "Rock band"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Radiohead"
    assert data["country"] == "UK"
    assert "id" in data


def test_list_artists_empty(client):
    response = client.get("/api/artists/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_artist_by_id(client):
    create = client.post("/api/artists/", json={"name": "Muse", "country": "UK"})
    artist_id = create.json()["id"]

    response = client.get(f"/api/artists/{artist_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Muse"


def test_get_artist_not_found(client):
    response = client.get("/api/artists/9999")
    assert response.status_code == 404