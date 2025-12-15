#!/usr/bin/env python3
"""
Script para adicionar mais produtos às páginas de categorias
"""

import os
import re

def get_additional_products():
    """Retorna produtos adicionais para cada categoria"""
    return {
        'moda.html': [
            {
                'name': 'Calça Jeans Skinny',
                'category': 'roupas',
                'price': '129.90',
                'old_price': '179.90',
                'rating': '4.5',
                'reviews': '342',
                'image': 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=500&q=80',
                'brand': 'levis'
            },
            {
                'name': 'Blusa de Tricot Feminina',
                'category': 'roupas',
                'price': '89.90',
                'old_price': '119.90',
                'rating': '4.7',
                'reviews': '156',
                'image': 'https://images.unsplash.com/photo-1434389677669-e08b4cac3105?auto=format&fit=crop&w=500&q=80',
                'brand': 'zara'
            },
            {
                'name': 'Sapato Social Masculino',
                'category': 'calcados',
                'price': '199.90',
                'old_price': '299.90',
                'rating': '4.6',
                'reviews': '89',
                'image': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=500&q=80',
                'brand': 'democrata'
            },
            {
                'name': 'Vestido Midi Elegante',
                'category': 'roupas',
                'price': '159.90',
                'old_price': '219.90',
                'rating': '4.8',
                'reviews': '234',
                'image': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=500&q=80',
                'brand': 'farm'
            },
            {
                'name': 'Relógio Masculino Esportivo',
                'category': 'acessorios',
                'price': '249.90',
                'old_price': '349.90',
                'rating': '4.4',
                'reviews': '167',
                'image': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=500&q=80',
                'brand': 'casio'
            },
            {
                'name': 'Mochila Executiva',
                'category': 'acessorios',
                'price': '179.90',
                'old_price': '249.90',
                'rating': '4.5',
                'reviews': '98',
                'image': 'https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=500&q=80',
                'brand': 'kipling'
            }
        ],
        'eletronicos.html': [
            {
                'name': 'Smartphone Samsung Galaxy',
                'category': 'smartphones',
                'price': '1899.90',
                'old_price': '2299.90',
                'rating': '4.6',
                'reviews': '456',
                'image': 'https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?auto=format&fit=crop&w=500&q=80',
                'brand': 'samsung'
            },
            {
                'name': 'Tablet iPad Air',
                'category': 'tablets',
                'price': '2499.90',
                'old_price': '2899.90',
                'rating': '4.8',
                'reviews': '234',
                'image': 'https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?auto=format&fit=crop&w=500&q=80',
                'brand': 'apple'
            },
            {
                'name': 'Notebook Gamer Acer',
                'category': 'notebooks',
                'price': '3299.90',
                'old_price': '3899.90',
                'rating': '4.5',
                'reviews': '189',
                'image': 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=500&q=80',
                'brand': 'acer'
            },
            {
                'name': 'Smartwatch Apple Watch',
                'category': 'wearables',
                'price': '1999.90',
                'old_price': '2399.90',
                'rating': '4.7',
                'reviews': '567',
                'image': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=500&q=80',
                'brand': 'apple'
            },
            {
                'name': 'Fone JBL Bluetooth',
                'category': 'audio',
                'price': '399.90',
                'old_price': '499.90',
                'rating': '4.4',
                'reviews': '345',
                'image': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=500&q=80',
                'brand': 'jbl'
            },
            {
                'name': 'Monitor 4K Dell',
                'category': 'monitores',
                'price': '1299.90',
                'old_price': '1599.90',
                'rating': '4.6',
                'reviews': '123',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=500&q=80',
                'brand': 'dell'
            }
        ],
        'casa.html': [
            {
                'name': 'Cama Box Casal',
                'category': 'moveis',
                'price': '899.90',
                'old_price': '1199.90',
                'rating': '4.5',
                'reviews': '234',
                'image': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=500&q=80',
                'brand': 'ortobom'
            },
            {
                'name': 'Guarda-Roupa 6 Portas',
                'category': 'moveis',
                'price': '1299.90',
                'old_price': '1699.90',
                'rating': '4.3',
                'reviews': '156',
                'image': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=500&q=80',
                'brand': 'madesa'
            },
            {
                'name': 'Conjunto de Panelas',
                'category': 'cozinha',
                'price': '299.90',
                'old_price': '399.90',
                'rating': '4.7',
                'reviews': '89',
                'image': 'https://images.unsplash.com/photo-1556909114-f6e7ad7d3136?auto=format&fit=crop&w=500&q=80',
                'brand': 'tramontina'
            },
            {
                'name': 'Aspirador de Pó Robô',
                'category': 'eletrodomesticos',
                'price': '799.90',
                'old_price': '999.90',
                'rating': '4.6',
                'reviews': '167',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=500&q=80',
                'brand': 'electrolux'
            },
            {
                'name': 'Espelho Decorativo Grande',
                'category': 'decoracao',
                'price': '199.90',
                'old_price': '279.90',
                'rating': '4.4',
                'reviews': '78',
                'image': 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=500&q=80',
                'brand': 'tok-stok'
            },
            {
                'name': 'Kit Toalhas de Banho',
                'category': 'banho',
                'price': '149.90',
                'old_price': '199.90',
                'rating': '4.5',
                'reviews': '234',
                'image': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?auto=format&fit=crop&w=500&q=80',
                'brand': 'buddemeyer'
            }
        ],
        'games.html': [
            {
                'name': 'God of War Ragnarök',
                'category': 'jogos',
                'price': '199.90',
                'old_price': '249.90',
                'rating': '4.9',
                'reviews': '1234',
                'image': 'https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=500&q=80',
                'brand': 'sony'
            },
            {
                'name': 'Cadeira Gamer RGB',
                'category': 'acessorios',
                'price': '899.90',
                'old_price': '1199.90',
                'rating': '4.6',
                'reviews': '345',
                'image': 'https://images.unsplash.com/photo-1592300410033-3d0c9bd1bfb8?auto=format&fit=crop&w=500&q=80',
                'brand': 'dxracer'
            },
            {
                'name': 'Nintendo Switch OLED',
                'category': 'consoles',
                'price': '2299.90',
                'old_price': '2599.90',
                'rating': '4.8',
                'reviews': '567',
                'image': 'https://images.unsplash.com/photo-1606144042614-b2417e99c4e3?auto=format&fit=crop&w=500&q=80',
                'brand': 'nintendo'
            },
            {
                'name': 'Webcam Gamer 4K',
                'category': 'streaming',
                'price': '399.90',
                'old_price': '499.90',
                'rating': '4.5',
                'reviews': '189',
                'image': 'https://images.unsplash.com/photo-1527814050087-3793815479db?auto=format&fit=crop&w=500&q=80',
                'brand': 'logitech'
            },
            {
                'name': 'Monitor Gamer 144Hz',
                'category': 'monitores',
                'price': '1599.90',
                'old_price': '1899.90',
                'rating': '4.7',
                'reviews': '234',
                'image': 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?auto=format&fit=crop&w=500&q=80',
                'brand': 'asus'
            },
            {
                'name': 'SSD Gamer 1TB',
                'category': 'hardware',
                'price': '599.90',
                'old_price': '799.90',
                'rating': '4.6',
                'reviews': '456',
                'image': 'https://images.unsplash.com/photo-1591799264318-7e6ef8ddb7ea?auto=format&fit=crop&w=500&q=80',
                'brand': 'kingston'
            }
        ],
        'esportes.html': [
            {
                'name': 'Whey Protein 1kg',
                'category': 'suplementos',
                'price': '89.90',
                'old_price': '119.90',
                'rating': '4.7',
                'reviews': '567',
                'image': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=500&q=80',
                'brand': 'optimum'
            },
            {
                'name': 'Esteira Elétrica',
                'category': 'fitness',
                'price': '1899.90',
                'old_price': '2399.90',
                'rating': '4.5',
                'reviews': '234',
                'image': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=500&q=80',
                'brand': 'movement'
            },
            {
                'name': 'Chuteira Nike Mercurial',
                'category': 'futebol',
                'price': '399.90',
                'old_price': '499.90',
                'rating': '4.8',
                'reviews': '345',
                'image': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=500&q=80',
                'brand': 'nike'
            },
            {
                'name': 'Kit Yoga Completo',
                'category': 'yoga',
                'price': '149.90',
                'old_price': '199.90',
                'rating': '4.6',
                'reviews': '189',
                'image': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=500&q=80',
                'brand': 'liveup'
            },
            {
                'name': 'Mochila de Hidratação',
                'category': 'ciclismo',
                'price': '199.90',
                'old_price': '249.90',
                'rating': '4.4',
                'reviews': '123',
                'image': 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?auto=format&fit=crop&w=500&q=80',
                'brand': 'camelbak'
            },
            {
                'name': 'Luvas de Boxe',
                'category': 'luta',
                'price': '129.90',
                'old_price': '179.90',
                'rating': '4.5',
                'reviews': '89',
                'image': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?auto=format&fit=crop&w=500&q=80',
                'brand': 'everlast'
            }
        ],
        'infantil.html': [
            {
                'name': 'Berço Convertível',
                'category': 'moveis',
                'price': '799.90',
                'old_price': '999.90',
                'rating': '4.7',
                'reviews': '234',
                'image': 'https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=500&q=80',
                'brand': 'cia-do-movel'
            },
            {
                'name': 'Kit Mamadeiras',
                'category': 'alimentacao',
                'price': '89.90',
                'old_price': '119.90',
                'rating': '4.6',
                'reviews': '345',
                'image': 'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?auto=format&fit=crop&w=500&q=80',
                'brand': 'avent'
            },
            {
                'name': 'Conjunto Roupinha RN',
                'category': 'roupas',
                'price': '129.90',
                'old_price': '169.90',
                'rating': '4.8',
                'reviews': '456',
                'image': 'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?auto=format&fit=crop&w=500&q=80',
                'brand': 'tip-top'
            },
            {
                'name': 'Tablet Educativo Infantil',
                'category': 'educativo',
                'price': '299.90',
                'old_price': '399.90',
                'rating': '4.5',
                'reviews': '189',
                'image': 'https://images.unsplash.com/photo-1558877385-1c4c7e9e1c6e?auto=format&fit=crop&w=500&q=80',
                'brand': 'multilaser'
            },
            {
                'name': 'Patinete Infantil',
                'category': 'brinquedos',
                'price': '199.90',
                'old_price': '249.90',
                'rating': '4.4',
                'reviews': '123',
                'image': 'https://images.unsplash.com/photo-1502744688674-c619d1586c9e?auto=format&fit=crop&w=500&q=80',
                'brand': 'bandeirante'
            },
            {
                'name': 'Kit Higiene Bebê',
                'category': 'higiene',
                'price': '79.90',
                'old_price': '99.90',
                'rating': '4.7',
                'reviews': '567',
                'image': 'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?auto=format&fit=crop&w=500&q=80',
                'brand': 'johnson'
            }
        ]
    }

def create_product_html(product):
    """Cria HTML para um produto"""
    return f'''
                <!-- {product['name']} -->
                <div class="product-card" data-category="{product['category']}" data-price="{product['price']}" data-brand="{product['brand']}">
                    <div class="product-badge flash-badge">-{int((float(product['old_price']) - float(product['price'])) / float(product['old_price']) * 100)}%</div>
                    <div class="product-image">
                        <img src="{product['image']}" alt="{product['name']}" class="product-img">
                        <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                    </div>
                    <div class="product-info">
                        <div class="product-category">{product['category'].title()}</div>
                        <h3>{product['name']}</h3>
                        <div class="product-rating">
                            {'<i class="fas fa-star"></i>' * int(float(product['rating']))}
                            {'<i class="fas fa-star-half-alt"></i>' if float(product['rating']) % 1 >= 0.5 else ''}
                            {'<i class="far fa-star"></i>' * (5 - int(float(product['rating'])) - (1 if float(product['rating']) % 1 >= 0.5 else 0))}
                            <span>({product['reviews']})</span>
                        </div>
                        <div class="product-price">
                            <span class="old-price">R$ {product['old_price']}</span>
                            <span class="new-price">R$ {product['price']}</span>
                        </div>
                        <button class="add-to-cart-btn" onclick="addToCart('{product['name']}', {product['price']})">
                            <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                        </button>
                    </div>
                </div>'''

def add_products_to_page(file_path, products):
    """Adiciona produtos a uma página"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Encontrar o final do grid de produtos
        grid_end_pattern = r'(</div>\s*</div>\s*</section>)'
        
        # Criar HTML dos novos produtos
        new_products_html = ''
        for product in products:
            new_products_html += create_product_html(product)
        
        # Inserir produtos antes do fechamento do grid
        if re.search(r'</div>\s*</div>\s*</section>', content):
            # Encontrar a posição antes do fechamento do grid
            insertion_point = content.rfind('</div>\n            </div>\n        </div>\n    </section>')
            if insertion_point != -1:
                content = content[:insertion_point] + new_products_html + '\n            ' + content[insertion_point:]
        
        # Salvar arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, f"{len(products)} produtos adicionados"
        
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🛍️ ADICIONANDO MAIS PRODUTOS")
    print("=" * 50)
    
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    additional_products = get_additional_products()
    
    success_count = 0
    total_products = 0
    
    for page, products in additional_products.items():
        file_path = os.path.join(frontend_dir, page)
        
        if os.path.exists(file_path):
            success, message = add_products_to_page(file_path, products)
            
            if success:
                print(f"✅ {page} - {message}")
                success_count += 1
                total_products += len(products)
            else:
                print(f"❌ {page} - {message}")
        else:
            print(f"⚠️ {page} - Arquivo não encontrado")
    
    print()
    print("=" * 50)
    print("📊 RESUMO DA ADIÇÃO")
    print(f"✅ Páginas atualizadas: {success_count}")
    print(f"🛍️ Total de produtos adicionados: {total_products}")
    print()
    
    if success_count > 0:
        print("🎯 Produtos adicionados por categoria:")
        print("   • 👗 Moda: +6 produtos (calças, blusas, sapatos, vestidos)")
        print("   • 📱 Eletrônicos: +6 produtos (smartphones, tablets, notebooks)")
        print("   • 🏠 Casa: +6 produtos (móveis, cozinha, eletrodomésticos)")
        print("   • 🎮 Games: +6 produtos (jogos, acessórios, hardware)")
        print("   • ⚽ Esportes: +6 produtos (fitness, futebol, suplementos)")
        print("   • 👶 Infantil: +6 produtos (móveis, roupas, brinquedos)")
        print()
    
    print("🚀 Catálogo expandido com sucesso!")

if __name__ == "__main__":
    main()