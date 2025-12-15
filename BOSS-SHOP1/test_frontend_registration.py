import requests
import json

# Test the exact data structure that the frontend sends
url = "http://localhost:8000/api/register/"

# This simulates the data structure sent by the frontend registration form
data = {
    "username": "frontendtest@example.com",  # Using email as username
    "email": "frontendtest@example.com",
    "password": "FrontendPass123",
    "first_name": "Frontend",
    "last_name": "Tester"
}

headers = {
    "Content-Type": "application/json"
}

print("Testing frontend-style registration...")
try:
    response = requests.post(url, data=json.dumps(data), headers=headers)
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 201:
        print("SUCCESS: Registration worked correctly!")
        result = response.json()
        print(f"User created: {result['user']['first_name']} {result['user']['last_name']}")
        print(f"Email: {result['user']['email']}")
        print(f"Username: {result['user']['username']}")
    else:
        print("ERROR: Registration failed")
        result = response.json()
        print(f"Error details: {result}")
        
except Exception as e:
    print(f"Exception occurred: {e}")