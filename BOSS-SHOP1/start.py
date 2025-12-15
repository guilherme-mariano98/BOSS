#!/usr/bin/env python3
"""
Main entry point for Boss Shopp application.
This script runs both the Django backend API and serves the frontend files.
Configured for deployment on Render.
"""

import os
import sys
import subprocess
import threading
import time
import webbrowser

def get_local_ip():
    """Get the local IP address for network access"""
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "localhost"

def open_browser_fullscreen():
    """Open the browser in fullscreen mode after a short delay"""
    time.sleep(3)
    port = int(os.environ.get("PORT", 8000))
    local_ip = get_local_ip()
    
    # Open localhost URL
    url = f"http://localhost:{port}"
    
    try:
        # Open the browser
        webbrowser.open(url)
        
        # Also open network URL if different from localhost
        if local_ip != "localhost":
            webbrowser.open(f"http://{local_ip}:{port}")
    except Exception as e:
        print(f"Could not open browser: {e}")
def main():
    # Get port from environment variable (Render sets this) or default to 8000
    port = int(os.environ.get("PORT", 8000))
    
    # Change to the backend directory to run Django
    backend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'backend')
    
    if not os.path.exists(backend_dir):
        print(f"Error: Backend directory not found at {backend_dir}")
        sys.exit(1)
    
    # Run the Django backend using the existing run_server.py
    print("=" * 50)
    print("BOSS SHOPP - Starting Full Application")
    print("=" * 50)
    print(f"Starting Django backend on port {port}...")
    
    # Display access URLs
    local_ip = get_local_ip()
    print(f"Local access: http://localhost:{port}")
    print(f"Network access: http://{local_ip}:{port}")
    print("Application will open in browser - Use the 'Tela Cheia' button to toggle fullscreen mode")
    print("Press Ctrl+C to stop the server")
    print("=" * 50)
    
    # Set environment variables for Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boss_shopp.settings')
    
    # Change to backend directory
    os.chdir(backend_dir)
    
    # Open browser in a separate thread
    browser_thread = threading.Thread(target=open_browser_fullscreen, daemon=True)
    browser_thread.start()
    
    # Run Django server
    try:
        # Use gunicorn for production (when deployed on Render)
        if os.environ.get("PORT"):
            print("Using gunicorn for production deployment...")
            subprocess.run([
                "gunicorn", 
                "boss_shopp.wsgi:application", 
                "--bind", f"0.0.0.0:{port}",
                "--workers", "2",
                "--timeout", "120"
            ])
        else:
            # Development mode - use Django's built-in server
            print("Using Django development server...")
            subprocess.run([
                sys.executable, 
                "manage.py", 
                "runserver", 
                f"0.0.0.0:{port}"
            ])
    except FileNotFoundError:
        print("Gunicorn not found, falling back to Django development server...")
        subprocess.run([
            sys.executable, 
            "manage.py", 
            "runserver", 
            f"0.0.0.0:{port}"
        ])
    except Exception as e:
        print(f"Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()