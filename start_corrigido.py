#!/usr/bin/env python3
"""
BOSS SHOPP - Servidor Frontend Corrigido
Serve os arquivos HTML com autenticação local funcionando
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
    # Procurar diretório frontend com arquivos HTML
    possible_dirs = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'frontend'),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'BOSS-SHOP1', 'frontend'),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'frontend')
    ]
    
    frontend_dir = None
    for dir_path in possible_dirs:
        if os.path.exists(dir_path) and os.path.exists(os.path.join(dir_path, 'index.html')):
            frontend_dir = dir_path
            break
    
    if not frontend_dir:
        print("❌ Erro: Diretório frontend com index.html não encontrado")
        print("Procurado em:")
        for dir_path in possible_dirs:
            print(f"  - {dir_path}")
        sys.exit(1)
    
    print(f"✅ Usando diretório frontend: {frontend_dir}")
    
    # Copiar arquivo de autenticação local se não existir
    auth_local_path = os.path.join(frontend_dir, 'auth-local.js')
    if not os.path.exists(auth_local_path):
        # Copiar da pasta src/frontend se existir
        src_auth = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src', 'frontend', 'auth-local.js')
        if os.path.exists(src_auth):
            import shutil
            shutil.copy2(src_auth, auth_local_path)
            print("✅ Arquivo auth-local.js copiado")
    
    # Mudar para o diretório frontend
    os.chdir(frontend_dir)
    
    # Configurar servidor
    PORT = 3000
    
    class CustomHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Expires', '0')
            super().end_headers()
        
        def send_error(self, code, message=None):
            if code == 404:
                # Servir index.html para 404s (SPA routing)
                self.path = '/index.html'
                return self.do_GET()
            super().send_error(code, message)
    
    # Iniciar servidor
    local_ip = get_local_ip()
    
    print("=" * 60)
    print("🚀 BOSS SHOPP - Servidor Frontend")
    print("=" * 60)
    print(f"📁 Diretório: {frontend_dir}")
    print(f"🌐 Local: http://localhost:{PORT}")
    print(f"📱 Rede: http://{local_ip}:{PORT}")
    print("🔒 Zoom fixo em 100% ativo")
    print("🖥️ Modo tela cheia ativo")
    print("🔐 Autenticação local funcionando")
    print("=" * 60)
    print("📋 Contas de teste:")
    print("   Admin: admin@bosshopp.com / admin123")
    print("   Cliente: cliente@email.com / 123456")
    print("=" * 60)
    
    # Abrir navegador em thread separada
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    try:
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print(f"✅ Servidor rodando na porta {PORT}")
            print("⚡ Pressione Ctrl+C para parar")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Servidor parado pelo usuário")
    except Exception as e:
        print(f"❌ Erro no servidor: {e}")

if __name__ == "__main__":
    main()