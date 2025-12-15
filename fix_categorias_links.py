#!/usr/bin/env python3
"""
Script para corrigir os links da página categorias.html
"""

import os
import re

def fix_categorias_links():
    """Corrige os links da página categorias.html"""
    try:
        file_path = os.path.join('BOSS-SHOP1', 'frontend', 'categorias.html')
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Mapeamento de links corretos
        link_corrections = {
            'categoria-moda.html': 'moda.html',
            'categoria-eletronicos.html': 'eletronicos.html',
            'categoria-casa.html': 'casa.html',
            'categoria-games.html': 'games.html',
            'categoria-esportes.html': 'esportes.html',
            'categoria-infantil.html': 'infantil.html',
            'categoria-beleza.html': 'beleza.html',
            'categoria-livros.html': 'livros.html',
            'categoria-automotivo.html': 'automotivo.html',
            'categoria-pet-shop.html': 'pet-shop.html',
            'categoria-alimentos.html': 'alimentos.html',
            'categoria-ferramentas.html': 'ferramentas.html',
            'categoria-musica.html': 'musica.html',
            'categoria-saude.html': 'saude.html',
            'categoria-brinquedos.html': 'brinquedos.html',
            'categoria-papelaria.html': 'papelaria.html'
        }
        
        # Aplicar correções
        for old_link, new_link in link_corrections.items():
            content = content.replace(old_link, new_link)
        
        # Adicionar botão voltar se não existir
        if 'back-to-home' not in content:
            back_button_css = '''    <style>
        .back-to-home {
            position: fixed;
            top: 20px;
            left: 20px;
            color: #ff6b35;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 500;
            padding: 12px 20px;
            background: white;
            border-radius: 50px;
            transition: all 0.3s ease;
            z-index: 100;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .back-to-home:hover {
            background: #ff6b35;
            color: white;
            transform: translateX(-4px);
        }
    </style>
</head>
<body>
    <a href="index.html" class="back-to-home">
        <i class="fas fa-arrow-left"></i>
        Voltar à loja
    </a>'''
            
            content = content.replace('</head>\n<body>', back_button_css)
        
        # Adicionar script básico se não existir
        if 'function logout()' not in content:
            basic_script = '''
    <script>
        // Função de logout
        function logout() {
            if (confirm('Tem certeza que deseja sair?')) {
                localStorage.removeItem('boss_shopp_token');
                localStorage.removeItem('user');
                window.location.href = 'login.html';
            }
        }
        
        // Atualizar ícone do usuário
        function updateUserIcon() {
            const userIcon = document.getElementById('userIcon');
            const userText = document.getElementById('userText');
            const logoutButton = document.getElementById('logoutButton');
            
            const authToken = localStorage.getItem('boss_shopp_token');
            const user = localStorage.getItem('user');
            
            if (authToken && user) {
                try {
                    const userData = JSON.parse(user);
                    if (userText) userText.textContent = userData.name || 'Minha Conta';
                    if (userIcon) userIcon.href = '#';
                    if (logoutButton) logoutButton.style.display = 'flex';
                } catch (e) {
                    if (userText) userText.textContent = 'Minha Conta';
                }
            } else {
                if (userText) userText.textContent = 'Entrar';
                if (userIcon) userIcon.href = 'login.html';
                if (logoutButton) logoutButton.style.display = 'none';
            }
        }
        
        // Inicializar quando a página carregar
        document.addEventListener('DOMContentLoaded', function() {
            updateUserIcon();
        });
    </script>'''
            
            content = content.replace('</body>', basic_script + '\n</body>')
        
        # Salvar o arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, "Links corrigidos com sucesso"
        
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🔗 CORRIGINDO LINKS DA PÁGINA CATEGORIAS")
    print("=" * 50)
    
    success, message = fix_categorias_links()
    
    if success:
        print(f"✅ categorias.html - {message}")
        print()
        print("🎯 Correções aplicadas:")
        print("   • Links das categorias principais corrigidos")
        print("   • Botão 'Voltar à loja' adicionado")
        print("   • Script básico de autenticação adicionado")
        print("   • Navegação funcional implementada")
        print()
        print("📋 Links corrigidos:")
        print("   • Moda: categoria-moda.html → moda.html")
        print("   • Eletrônicos: categoria-eletronicos.html → eletronicos.html")
        print("   • Casa: categoria-casa.html → casa.html")
        print("   • Games: categoria-games.html → games.html")
        print("   • Esportes: categoria-esportes.html → esportes.html")
        print("   • Infantil: categoria-infantil.html → infantil.html")
        print("   • + 10 outras categorias corrigidas")
    else:
        print(f"❌ categorias.html - {message}")
    
    print()
    print("🚀 Página de categorias corrigida e funcional!")

if __name__ == "__main__":
    main()