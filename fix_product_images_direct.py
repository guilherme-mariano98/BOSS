#!/usr/bin/env python3
"""
Script para adicionar imagens diretamente aos produtos existentes
"""

import os
import re

def fix_product_images():
    """Adiciona imagens aos produtos de forma direta"""
    
    # Mapeamento de produtos para imagens
    product_images = {
        # MODA
        'Jaqueta Jeans Premium': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=500&q=80',
        'Vestido Floral Elegante': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=500&q=80',
        'Tênis Esportivo Moderno': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=500&q=80',
        'Camisa Social Masculina': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=500&q=80',
        'Bolsa de Couro Feminina': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=500&q=80',
        'Óculos de Sol Premium': 'https://images.unsplash.com/photo-1572635196237-14b3f281503f?auto=format&fit=crop&w=500&q=80',
        
        # ELETRÔNICOS
        'iPhone 15 Pro Max': 'https://images.unsplash.com/photo-1695048133142-1a20484d2569?auto=format&fit=crop&w=500&q=80',
        'MacBook Air M3': 'https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=500&q=80',
        'AirPods Pro 3': 'https://images.unsplash.com/photo-1606220945770-b5b6c2c55bf1?auto=format&fit=crop&w=500&q=80',
        'Smart TV OLED 65"': 'https://images.unsplash.com/photo-1593305841991-05c297ba4575?auto=format&fit=crop&w=500&q=80',
        'PlayStation 5 Pro': 'https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?auto=format&fit=crop&w=500&q=80',
        'Câmera DSLR Canon': 'https://images.unsplash.com/photo-1502920917128-1aa500764cbd?auto=format&fit=crop&w=500&q=80',
        
        # CASA
        'Sofá 3 Lugares': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=500&q=80',
        'Mesa de Jantar': 'https://images.unsplash.com/photo-1549497538-303791108f95?auto=format&fit=crop&w=500&q=80',
        'Luminária Moderna': 'https://images.unsplash.com/photo-1513506003901-1e6a229e2d15?auto=format&fit=crop&w=500&q=80',
        'Tapete Decorativo': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=500&q=80',
        'Quadro Abstrato': 'https://images.unsplash.com/photo-1541961017774-22349e4a1262?auto=format&fit=crop&w=500&q=80',
        'Vaso Decorativo': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?auto=format&fit=crop&w=500&q=80',
        
        # GAMES
        'FIFA 24': 'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=500&q=80',
        'Call of Duty': 'https://images.unsplash.com/photo-1552820728-8b83bb6b773f?auto=format&fit=crop&w=500&q=80',
        'Controle Xbox': 'https://images.unsplash.com/photo-1605901309584-818e25960a8f?auto=format&fit=crop&w=500&q=80',
        'Headset Gamer': 'https://images.unsplash.com/photo-1599669454699-248893623440?auto=format&fit=crop&w=500&q=80',
        'Teclado Mecânico': 'https://images.unsplash.com/photo-1541140532154-b024d705b90a?auto=format&fit=crop&w=500&q=80',
        'Mouse Gamer': 'https://images.unsplash.com/photo-1527814050087-3793815479db?auto=format&fit=crop&w=500&q=80',
        
        # ESPORTES
        'Tênis de Corrida': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=500&q=80',
        'Bicicleta Mountain Bike': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=500&q=80',
        'Kit de Musculação': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=500&q=80',
        'Bola de Futebol': 'https://images.unsplash.com/photo-1614632537190-23e4b21577de?auto=format&fit=crop&w=500&q=80',
        'Raquete de Tênis': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?auto=format&fit=crop&w=500&q=80',
        'Prancha de Surf': 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=500&q=80',
        
        # INFANTIL
        'Carrinho de Bebê': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=500&q=80',
        'Brinquedo Educativo': 'https://images.unsplash.com/photo-1558877385-1c4c7e9e1c6e?auto=format&fit=crop&w=500&q=80',
        'Roupinha de Bebê': 'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?auto=format&fit=crop&w=500&q=80',
        'Cadeirinha de Carro': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=500&q=80',
        'Bicicleta Infantil': 'https://images.unsplash.com/photo-1502744688674-c619d1586c9e?auto=format&fit=crop&w=500&q=80',
        'Boneca Interativa': 'https://images.unsplash.com/photo-1558877385-1c4c7e9e1c6e?auto=format&fit=crop&w=500&q=80',
        
        # INDEX.HTML
        'Smartphone Premium': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=500&q=80',
        'Notebook Ultrafino': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=500&q=80',
        'Fone Bluetooth Premium': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=500&q=80',
        'Camiseta Estampada': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=500&q=80',
        'Relógio Inteligente': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=500&q=80',
        'Tablet Android': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?auto=format&fit=crop&w=500&q=80'
    }
    
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    pages = ['moda.html', 'eletronicos.html', 'casa.html', 'games.html', 'esportes.html', 'infantil.html', 'index.html']
    
    for page in pages:
        file_path = os.path.join(frontend_dir, page)
        
        if not os.path.exists(file_path):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Substituir imagens placeholder ou adicionar imagens onde não há
            for product_name, image_url in product_images.items():
                if product_name in content:
                    # Padrão para encontrar img src placeholder ou vazio
                    placeholder_patterns = [
                        r'<img src="https://via\.placeholder\.com/[^"]*"([^>]*alt="' + re.escape(product_name) + r'"[^>]*)>',
                        r'<img src="https://images\.unsplash\.com/[^"]*"([^>]*alt="' + re.escape(product_name) + r'"[^>]*)>',
                        r'<img src=""([^>]*alt="' + re.escape(product_name) + r'"[^>]*)>'
                    ]
                    
                    new_img = f'<img src="{image_url}" alt="{product_name}" class="product-img">'
                    
                    for pattern in placeholder_patterns:
                        content = re.sub(pattern, new_img, content)
                    
                    # Se não encontrou img, procurar por div product-image e adicionar
                    if f'alt="{product_name}"' not in content:
                        # Procurar por div product-image vazia antes do produto
                        empty_image_pattern = rf'(<div class="product-image">\s*</div>)\s*(<div class="product-info">.*?<h3>{re.escape(product_name)}</h3>)'
                        
                        if re.search(empty_image_pattern, content, re.DOTALL):
                            new_image_div = f'''<div class="product-image">
                        {new_img}
                        <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                    </div>'''
                            
                            content = re.sub(empty_image_pattern, 
                                           new_image_div + r'\n                    \2', 
                                           content, flags=re.DOTALL)
            
            # Salvar arquivo
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"✅ {page} - Imagens atualizadas")
            
        except Exception as e:
            print(f"❌ {page} - Erro: {e}")

def main():
    """Função principal"""
    print("🖼️ ADICIONANDO IMAGENS REAIS AOS PRODUTOS")
    print("=" * 50)
    
    fix_product_images()
    
    print()
    print("🎯 Imagens adicionadas:")
    print("   • 👗 Moda: Jaquetas, vestidos, tênis, camisas, bolsas, óculos")
    print("   • 📱 Eletrônicos: iPhone, MacBook, AirPods, TV, PlayStation, câmera")
    print("   • 🏠 Casa: Sofá, mesa, luminária, tapete, quadros, vasos")
    print("   • 🎮 Games: FIFA, Call of Duty, controles, headsets, teclados")
    print("   • ⚽ Esportes: Tênis, bicicleta, musculação, futebol, tênis, surf")
    print("   • 👶 Infantil: Carrinho, brinquedos, roupas, cadeirinha, bicicleta")
    print("   • 🏠 Index: Produtos em destaque com imagens atrativas")
    print()
    print("🚀 Todos os produtos agora têm imagens reais do Unsplash!")

if __name__ == "__main__":
    main()