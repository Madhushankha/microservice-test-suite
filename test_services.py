import requests
from datetime import datetime, timezone
from uuid import uuid4

# Hardcoded internal service URLs in the Kubernetes cluster
BASE_URLS = {
    "analytics": "http://analytics-service-04.base-platform.svc.cluster.local:8080",
    "orders": "http://order-service-03.base-platform.svc.cluster.local:8080",
    "games": "http://game-service-02.base-platform.svc.cluster.local:8080"
}

print("🔗 Service URLs in use:")
for service, url in BASE_URLS.items():
    print(f"  {service}: {url}")


def run_game_tests():
    print("\n--- Running GameService tests ---")
    game_payload = {
        "name": "Test Game",
        "category": "Action",
        "releasedDate": datetime.now(timezone.utc).isoformat(),
        "price": 0
    }

    # Create game
    response = requests.post(f"{BASE_URLS['games']}/api/Games", json=game_payload)
    print("Game Create response:", response.status_code, response.text)
    assert response.status_code == 200
    game = response.json()
    game_id = game.get("id")

    try:
        # GET all games
        response = requests.get(f"{BASE_URLS['games']}/api/Games")
        print("Game GET all response:", response.status_code, response.text)
        assert response.status_code == 200

        # GET game by ID using query parameter
        response = requests.get(f"{BASE_URLS['games']}/api/Games/id", params={"id": game_id})
        print("Game GET by ID response:", response.status_code, response.text)
        assert response.status_code == 200

        # UPDATE game using query parameter
        updated_payload = {
            "id": game_id,
            "name": "Updated FIFA 2025",
            "category": "Simulation",
            "releasedDate": datetime.now(timezone.utc).isoformat(),
            "price": 39.99
        }
        response = requests.put(f"{BASE_URLS['games']}/api/Games/id", params={"id": game_id}, json=updated_payload)
        print("Game Update response:", response.status_code, response.text)
        assert response.status_code == 204

        # DELETE game using query parameter
        response = requests.delete(f"{BASE_URLS['games']}/api/Games/id", params={"id": game_id})
        print("Game DELETE response:", response.status_code, response.text)
        assert response.status_code == 204

    finally:
        # Cleanup
        requests.delete(f"{BASE_URLS['games']}/api/Games/id", params={"id": game_id})


def run_order_tests():
    print("\n--- Running OrderService tests ---")
    order_payload = {
        "customerId": "cust-123",
        "items": [{
            "productId": "prod-101",
            "productName": "Gamepad",
            "unitPrice": 49.99,
            "quantity": 1
        }]
    }

    response = requests.post(f"{BASE_URLS['orders']}/api/Orders/create", json=order_payload)
    print("Order Create response:", response.status_code, response.text)
    assert response.status_code == 200
    order = response.json()
    order_id = order.get("id")

    try:
        # GET order by ID
        response = requests.get(f"{BASE_URLS['orders']}/api/Orders/{order_id}")
        print("Order GET by ID response:", response.status_code, response.text)
        assert response.status_code == 200


    finally:
        # Cleanup
        requests.delete(f"{BASE_URLS['orders']}/api/Orders/{order_id}")


def run_all_tests():
    # Uncomment below if analytics test is needed
    # run_analytics_test()
    run_game_tests()
    run_order_tests()


if __name__ == "__main__":
    run_all_tests()
