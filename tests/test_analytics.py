import requests
from uuid import uuid4
from datetime import datetime
import os

BASE_URL = os.getenv("BASE_URL", "http://analytics-service.base-platform.svc.cluster.local")

def test_post_analytics():
    data = {
        "event": "click",
        "url": "http://example.com",
        "referrer": "http://google.com",
        "timestamp": datetime.utcnow().isoformat(),
        "sessionId": str(uuid4()),
        "userAgent": "Mozilla/5.0",
        "element": "button",
        "id": "btn123",
        "class": "primary-btn",
        "depth": 1,
        "durationSec": 5
    }
    response = requests.post(f"{BASE_URL}/api/Analytics", json=data)
    assert response.status_code == 200
