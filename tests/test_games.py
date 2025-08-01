import requests
from datetime import datetime
import os

GAME_URL = os.getenv("GAME_URL", "http://game-service.base-platform.svc.cluster.local")

def test_create_game():
    payload = {
        "name": "FIFA 2025",
        "category": "Sports",
        "releasedDate": datetime.utcnow().isoformat(),
        "price": 59.99
    }
    response = requests.post(f"{GAME_URL}/api/Games", json=payload)
    assert response.status_code == 200


def test_get_all_games():
    response = requests.get(f"{GAME_URL}/api/Games")
    assert response.status_code == 200

def test_get_game_by_id():
    game_id = "game-123"  # Replace with an existing one
    response = requests.get(f"{GAME_URL}/api/Games/{game_id}")
    assert response.status_code == 200

def test_update_game():
    game_id = "game-123"
    payload = {
        "name": "Updated Game",
        "category": "Action",
        "releasedDate": datetime.utcnow().isoformat(),
        "price": 39.99
    }
    response = requests.put(f"{GAME_URL}/api/Games/{game_id}", json=payload)
    assert response.status_code == 200

def test_delete_game():
    game_id = "game-123"
    response = requests.delete(f"{GAME_URL}/api/Games/{game_id}")
    assert response.status_code == 200