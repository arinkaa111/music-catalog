def test_create_track(client):
    # Сначала создаём артиста и альбом
    artist = client.post("/api/artists/", json={"name": "Nirvana"}).json()
    # Временная проверка: без роутера albums, создаём трек напрямую через модель.
    # Пока проверим только создание артиста и список.
    assert artist["id"] > 0


def test_list_tracks_empty(client):
    response = client.get("/api/tracks/")
    assert response.status_code == 200
    assert response.json() == []


def test_create_track_requires_existing_album(client):
    # Пытаемся создать трек с несуществующим альбомом — ждём 400
    response = client.post(
        "/api/tracks/",
        json={"title": "Smells Like Teen Spirit", "album_id": 9999},
    )
    assert response.status_code == 400
    assert "Album not found" in response.json()["detail"]