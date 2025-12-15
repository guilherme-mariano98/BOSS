#!/usr/bin/env python3
"""
BOSS SHOPP - Servidor Frontend
Serve os arquivos da pasta src/frontend com autenticação local
"""

import os
import sys
import http.server
import socketserver
import webbrowser
import threading
import time

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

def open_browser():
    """Open the browser after a short delay"""
    time.sleep(2)
    webbrowser.open("http://localhost:3000")

def main():
    # Change to the frontend directory
    frontend_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'BOSS-SHOP1', 'frontend')
    
    if not os.path.exists(frontend_dir):
        print(f"Error: Frontend directory not found at {frontend_dir}")
        sys.exit(1)
    
    print(f"Using frontend directory: {frontend_dir}")
    os.chdir(frontend_dir)
    
    # Set up the server
    PORT = 3000
    
    # Custom handler to serve index.html for root and handle SPA routing
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            super().end_headers()
        
        def send_error(self, code, message=None):
            if code == 404:
                # Serve index.html for any 404s (SPA routing)
                self.path = '/index.html'
                return self.do_GET()
            super().send_error(code, message)
    
    # Start the server
    try:
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            local_ip = get_local_ip()
            
            print("=" * 60)
            print("🚀 BOSS SHOPP - Frontend Server")
            print("=" * 60)
            print(f"📁 Serving files from: {frontend_dir}")
            print(f"🌐 Local access: http://localhost:{PORT}")
            print(f"📱 Network access: http://{local_ip}:{PORT}")
            print("🔒 Zoom fixo em 100% ativo")
            print("🖥️ Modo tela cheia ativo")
            print("=" * 60)
            print("📋 Páginas disponíveis:")
            print("   • http://localhost:3000 (Página inicial)")
            print("   • http://localhost:3000/login.html (Login)")
            print("   • http://localhost:3000/profile.html (Perfil)")
            print("   • http://localhost:3000/categorias.html (Categorias)")
            print("=" * 60)
            print("⚡ Pressione Ctrl+C para parar o servidor")
            
            # Open browser in a separate thread
            browser_thread = threading.Thread(target=open_browser, daemon=True)
            browser_thread.start()
            
            # Start serving
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Servidor parado pelo usuário")
    except Exception as e:
        print(f"❌ Erro no servidor: {e}")

if __name__ == "__main__":
    main()