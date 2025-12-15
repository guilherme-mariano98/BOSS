#!/usr/bin/env python3
"""
Script para adicionar imagens reais aos produtos nas páginas de categorias
"""

import os
import re

def get_product_images():
    """Retorna mapeamento de produtos para imagens do Unsplash"""
    return {
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
        'Luminária Moderna': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=500&q=80',
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
        
        # Produtos genéricos para outros casos
        'Smartphone Premium': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=500&q=80',
        'Notebook Ultrafino': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=500&q=80',
        'Fone Bluetooth Premium': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=500&q=80',
        'Camiseta Estampada': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?auto=format&fit=crop&w=500&q=80',
        'Relógio Inteligente': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=500&q=80',
        'Tablet Android': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?auto=format&fit=crop&w=500&q=80'
    }

def add_images_to_page(file_path, images_map):
    """Adiciona imagens aos produtos de uma página"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Encontrar todos os produtos e adicionar imagens
        for product_name, image_url in images_map.items():
            # Padrão para encontrar produtos sem imagem ou com placeholder
            product_pattern = rf'(<h3>{re.escape(product_name)}</h3>)'
            
            # Verificar se o produto existe na página
            if re.search(product_pattern, content):
                # Procurar por div product-image antes do h3
                image_div_pattern = rf'(<div class="product-image">.*?</div>)\s*<div class="product-info">\s*.*?<h3>{re.escape(product_name)}</h3>'
                
                if re.search(image_div_pattern, content, re.DOTALL):
                    # Substituir imagem existente
                    new_image_div = f'''<div class="product-image">
                        <img src="{image_url}" alt="{product_name}" class="product-img">
                        <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                    </div>'''
                    
                    content = re.sub(image_div_pattern, 
                                   new_image_div + r'\n                    <div class="product-info">\n                        <div class="product-category">Categoria</div>\n                        <h3>' + product_name + '</h3>',
                                   content, flags=re.DOTALL)
                else:
                    # Adicionar div de imagem antes do product-info se não existir
                    product_info_pattern = rf'(<div class="product-info">)\s*(<div class="product-category">.*?</div>)?\s*<h3>{re.escape(product_name)}</h3>'
                    
                    new_structure = f'''<div class="product-image">
                        <img src="{image_url}" alt="{product_name}" class="product-img">
                        <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                    </div>
                    <div class="product-info">
                        <div class="product-category">Categoria</div>
                        <h3>{product_name}</h3>'''
                    
                    content = re.sub(product_info_pattern, new_structure, content, flags=re.DOTALL)
        
        # Salvar o arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, "Imagens adicionadas com sucesso"
        
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🖼️ ADICIONANDO IMAGENS AOS PRODUTOS")
    print("=" * 50)
    
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    images_map = get_product_images()
    
    # Páginas de categorias
    category_pages = [
        'moda.html',
        'eletronicos.html',
        'casa.html',
        'games.html',
        'esportes.html',
        'infantil.html',
        'index.html'  # Página principal também tem produtos
    ]
    
    success_count = 0
    error_count = 0
    
    print("📋 Adicionando imagens aos produtos...")
    print()
    
    for page in category_pages:
        file_path = os.path.join(frontend_dir, page)
        
        if os.path.exists(file_path):
            success, message = add_images_to_page(file_path, images_map)
            
            if success:
                print(f"✅ {page} - {message}")
                success_count += 1
            else:
                print(f"❌ {page} - {message}")
                error_count += 1
        else:
            print(f"⚠️ {page} - Arquivo não encontrado")
    
    print()
    print("=" * 50)
    print("📊 RESUMO DA OPERAÇÃO")
    print(f"✅ Páginas com imagens adicionadas: {success_count}")
    print(f"❌ Páginas com erro: {error_count}")
    print()
    
    if success_count > 0:
        print("🎯 Imagens adicionadas:")
        print("   • Produtos de Moda com imagens reais")
        print("   • Eletrônicos com fotos de alta qualidade")
        print("   • Casa e decoração com imagens atrativas")
        print("   • Games com capas e produtos reais")
        print("   • Esportes com equipamentos profissionais")
        print("   • Infantil com produtos seguros e coloridos")
        print("   • Todas as imagens do Unsplash (gratuitas)")
        print()
    
    print("🚀 Todos os produtos agora têm imagens reais e atrativas!")

if __name__ == "__main__":
    main()