import webbrowser
import time

# Wait a moment for the server to fully start
time.sleep(2)

# Open the login page in the default browser
webbrowser.open('http://localhost:8000/login.html')

print("Browser opened! You can now test the registration functionality.")
print("Navigate to the registration form and try creating a new account.")