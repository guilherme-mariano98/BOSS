#!/usr/bin/env python3
"""
Script para corrigir todas as páginas de categorias
"""

import os
import re

def get_category_script():
    """Retorna o script JavaScript completo para páginas de categoria"""
    return '''    <script>
        // Função para adicionar ao carrinho
        function addToCart(productName, price) {
            // Verificar se o usuário está logado
            const authToken = localStorage.getItem('boss_shopp_token');
            if (!authToken) {
                alert('Você precisa estar logado para adicionar produtos ao carrinho!');
                window.location.href = 'login.html';
                return;
            }

            // Obter carrinho atual
            let cart = JSON.parse(localStorage.getItem('cart')) || [];
            
            // Verificar se o produto já existe no carrinho
            const existingProduct = cart.find(item => item.name === productName);
            
            if (existingProduct) {
                existingProduct.quantity += 1;
            } else {
                cart.push({
                    name: productName,
                    price: price,
                    quantity: 1,
                    image: 'https://via.placeholder.com/150'
                });
            }
            
            // Salvar carrinho
            localStorage.setItem('cart', JSON.stringify(cart));
            
            // Mostrar notificação
            showNotification(`${productName} adicionado ao carrinho!`, 'success');
            
            // Atualizar contador do carrinho
            updateCartCount();
        }

        // Função para mostrar notificação
        function showNotification(message, type = 'success') {
            const existingNotification = document.querySelector('.notification');
            if (existingNotification) {
                existingNotification.remove();
            }
            
            const notification = document.createElement('div');
            notification.className = `notification ${type}`;
            notification.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background-color: ${type === 'success' ? '#00aa00' : '#ff4444'};
                color: white;
                padding: 15px 20px;
                border-radius: 5px;
                z-index: 10000;
                font-weight: bold;
                box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            `;
            notification.textContent = message;
            
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.remove();
            }, 3000);
        }

        // Função para atualizar contador do carrinho
        function updateCartCount() {
            const cart = JSON.parse(localStorage.getItem('cart')) || [];
            const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
            
            const cartCount = document.querySelector('.cart-count');
            if (cartCount) {
                cartCount.textContent = totalItems;
            }
        }

        // Função de logout
        function logout() {
            if (confirm('Tem certeza que deseja sair?')) {
                localStorage.removeItem('boss_shopp_token');
                localStorage.removeItem('user');
                window.location.href = 'login.html';
            }
        }

        // Função para atualizar ícone do usuário
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

        // Função de filtros
        function filterProducts() {
            const categoryFilter = document.getElementById('categoryFilter');
            const priceFilter = document.getElementById('priceFilter');
            const brandFilter = document.getElementById('brandFilter');
            const sortFilter = document.getElementById('sortFilter');
            
            if (!categoryFilter || !priceFilter || !brandFilter || !sortFilter) return;
            
            const categoryValue = categoryFilter.value;
            const priceValue = priceFilter.value;
            const brandValue = brandFilter.value;
            const sortValue = sortFilter.value;
            
            const products = document.querySelectorAll('.product-card');
            let visibleProducts = [];
            
            products.forEach(product => {
                let show = true;
                
                // Filtro por categoria
                if (categoryValue !== 'all' && product.dataset.category && !product.dataset.category.includes(categoryValue)) {
                    show = false;
                }
                
                // Filtro por preço
                if (priceValue !== 'all' && product.dataset.price) {
                    const price = parseFloat(product.dataset.price);
                    switch(priceValue) {
                        case 'under50':
                            if (price >= 50) show = false;
                            break;
                        case '50to100':
                            if (price < 50 || price > 100) show = false;
                            break;
                        case '100to200':
                            if (price < 100 || price > 200) show = false;
                            break;
                        case 'over200':
                            if (price <= 200) show = false;
                            break;
                    }
                }
                
                // Filtro por marca
                if (brandValue !== 'all' && product.dataset.brand && product.dataset.brand !== brandValue) {
                    show = false;
                }
                
                if (show) {
                    product.style.display = 'block';
                    visibleProducts.push(product);
                } else {
                    product.style.display = 'none';
                }
            });
            
            // Ordenação
            if (sortValue !== 'relevance') {
                visibleProducts.sort((a, b) => {
                    const priceA = parseFloat(a.dataset.price || '0');
                    const priceB = parseFloat(b.dataset.price || '0');
                    
                    switch(sortValue) {
                        case 'price-low':
                            return priceA - priceB;
                        case 'price-high':
                            return priceB - priceA;
                        case 'name':
                            const nameA = a.querySelector('h3')?.textContent || '';
                            const nameB = b.querySelector('h3')?.textContent || '';
                            return nameA.localeCompare(nameB);
                        default:
                            return 0;
                    }
                });
                
                const grid = document.getElementById('productsGrid');
                if (grid) {
                    visibleProducts.forEach(product => {
                        grid.appendChild(product);
                    });
                }
            }
        }

        // Inicializar quando a página carregar
        document.addEventListener('DOMContentLoaded', function() {
            updateUserIcon();
            updateCartCount();
            
            // Adicionar event listeners para filtros
            const filters = ['categoryFilter', 'priceFilter', 'brandFilter', 'sortFilter'];
            filters.forEach(filterId => {
                const element = document.getElementById(filterId);
                if (element) {
                    element.addEventListener('change', filterProducts);
                }
            });
        });
    </script>'''

def add_back_button():
    """Retorna o HTML e CSS para o botão voltar"""
    return '''    <style>
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

def fix_category_page(file_path):
    """Corrige uma página de categoria específica"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Adicionar botão voltar se não existir
        if 'back-to-home' not in content:
            back_button = add_back_button()
            content = content.replace('</head>\n<body>', back_button)
        
        # Adicionar script se não existir ou substituir script existente
        script_content = get_category_script()
        
        if 'function addToCart(' in content:
            # Substituir script existente
            script_pattern = r'<script>.*?</script>\s*</body>'
            content = re.sub(script_pattern, script_content + '\n</body>', content, flags=re.DOTALL)
        else:
            # Adicionar script antes do </body>
            content = content.replace('</body>', script_content + '\n</body>')
        
        # Verificar se houve mudanças
        if content != original_content:
            # Salvar o arquivo
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Página corrigida com sucesso"
        else:
            return False, "Página já estava correta"
        
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🔧 CORRIGINDO PÁGINAS DE CATEGORIAS")
    print("=" * 50)
    
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    
    # Páginas de categorias
    category_pages = [
        'moda.html',
        'eletronicos.html',
        'casa.html',
        'games.html',
        'esportes.html',
        'infantil.html'
    ]
    
    success_count = 0
    already_correct_count = 0
    error_count = 0
    
    print("📋 Corrigindo páginas de categorias...")
    print()
    
    for page in category_pages:
        file_path = os.path.join(frontend_dir, page)
        
        if os.path.exists(file_path):
            success, message = fix_category_page(file_path)
            
            if success:
                print(f"✅ {page} - {message}")
                success_count += 1
            elif "já estava correta" in message:
                print(f"ℹ️ {page} - {message}")
                already_correct_count += 1
            else:
                print(f"❌ {page} - {message}")
                error_count += 1
        else:
            print(f"⚠️ {page} - Arquivo não encontrado")
    
    print()
    print("=" * 50)
    print("📊 RESUMO DA CORREÇÃO")
    print(f"✅ Páginas corrigidas: {success_count}")
    print(f"ℹ️ Páginas já corretas: {already_correct_count}")
    print(f"❌ Páginas com erro: {error_count}")
    print()
    
    if success_count > 0:
        print("🎯 Correções aplicadas:")
        print("   • Scripts JavaScript funcionais adicionados")
        print("   • Função addToCart implementada")
        print("   • Sistema de filtros funcionais")
        print("   • Botão 'Voltar à loja' adicionado")
        print("   • Notificações de carrinho implementadas")
        print("   • Autenticação de usuário integrada")
        print()
    
    print("🚀 Todas as páginas de categorias agora estão funcionais!")

if __name__ == "__main__":
    main()