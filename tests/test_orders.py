import requests
import os

ORDER_URL = os.getenv("ORDER_URL", "http://order-service.base-platform.svc.cluster.local")

def test_create_order():
    payload = {
        "customerId": "cust-123",
        "items": [
            {
                "productId": "prod-101",
                "productName": "Gamepad",
                "unitPrice": 49.99,
                "quantity": 1
            }
        ]
    }
    response = requests.post(f"{ORDER_URL}/api/Orders/create", json=payload)
    assert response.status_code == 200


def test_get_order_by_id():
    order_id = "order-123"  # Replace with an existing or mocked one
    response = requests.get(f"{ORDER_URL}/api/Orders/{order_id}")
    assert response.status_code == 200

def test_update_order_status():
    order_id = "order-123"
    new_status = 2  # Shipped
    response = requests.patch(
        f"{ORDER_URL}/api/Orders/{order_id}/status",
        json=new_status
    )
    assert response.status_code == 200