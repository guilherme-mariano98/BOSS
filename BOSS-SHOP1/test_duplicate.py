import requests
import json

# Test registration with duplicate email
url = "http://localhost:8000/api/register/"
data = {
    "username": "testuser2",
    "email": "test@example.com",  # Same email as before
    "password": "TestPass123",
    "first_name": "Test2",
    "last_name": "User2"
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