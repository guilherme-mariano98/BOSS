import requests
import json

# Test registration
url = "http://localhost:8000/api/register/"
data = {
    "username": "testuser2",
    "email": "test2@example.com",
    "password": "testpass123",
    "first_name": "Test",
    "last_name": "User"
}

headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")