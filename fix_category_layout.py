#!/usr/bin/env python3
"""
Script para corrigir o layout das páginas de categorias
"""

import os
import re

def get_fixed_css():
    """Retorna CSS corrigido para o grid de produtos"""
    return '''        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            justify-items: center;
            padding: 20px 0;
        }

        .product-card {
            background: white;
            border-radius: 20px;
            padding: 20px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
            width: 100%;
            max-width: 320px;
            min-height: 450px;
        }

        .product-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, rgba(255, 107, 53, 0.05) 0%, rgba(247, 147, 30, 0.05) 100%);
            opacity: 0;
            transition: opacity 0.3s ease;
            z-index: 0;
        }

        .product-card:hover::before {
            opacity: 1;
        }

        .product-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
            border-color: #ff6b35;
        }

        .product-image {
            position: relative;
            width: 100%;
            height: 200px;
            margin-bottom: 15px;
            border-radius: 15px;
            overflow: hidden;
            z-index: 1;
        }

        .product-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }

        .product-card:hover .product-image img {
            transform: scale(1.05);
        }

        .product-info {
            position: relative;
            z-index: 1;
        }

        .product-info h3 {
            font-size: 18px;
            font-weight: 700;
            color: #333;
            margin-bottom: 10px;
            line-height: 1.3;
        }

        .product-price {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 15px;
        }

        .product-price .new-price {
            font-size: 20px;
            font-weight: 800;
            color: #ff6b35;
        }

        .product-price .old-price {
            font-size: 14px;
            color: #999;
            text-decoration: line-through;
        }

        .product-rating {
            display: flex;
            align-items: center;
            gap: 5px;
            margin-bottom: 15px;
        }

        .product-rating i {
            color: #ffc107;
            font-size: 14px;
        }

        .product-rating span {
            color: #666;
            font-size: 14px;
        }

        .add-to-cart-btn {
            width: 100%;
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 10px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }

        .add-to-cart-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(255, 107, 53, 0.3);
        }

        /* Responsividade */
        @media (max-width: 1200px) {
            .products-grid {
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 25px;
            }
        }

        @media (max-width: 768px) {
            .products-grid {
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                padding: 15px 0;
            }
            
            .product-card {
                max-width: 100%;
                min-height: 400px;
            }
        }

        @media (max-width: 480px) {
            .products-grid {
                grid-template-columns: 1fr;
                gap: 15px;
            }
        }'''

def fix_category_layout(file_path):
    """Corrige o layout de uma página de categoria"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Encontrar e substituir o CSS do products-grid
        products_grid_pattern = r'\.products-grid\s*\{[^}]*\}.*?(?=\.[\w-]+\s*\{|</style>|$)'
        
        # Encontrar todo o CSS relacionado aos produtos
        product_css_pattern = r'(\.products-grid\s*\{.*?\.add-to-cart-btn:hover\s*\{[^}]*\})'
        
        fixed_css = get_fixed_css()
        
        # Substituir CSS existente
        if re.search(product_css_pattern, content, re.DOTALL):
            content = re.sub(product_css_pattern, fixed_css, content, flags=re.DOTALL)
        else:
            # Se não encontrar o padrão, substituir apenas o products-grid
            content = re.sub(r'\.products-grid\s*\{[^}]*\}', fixed_css, content)
        
        # Garantir que o container tenha largura adequada
        if 'max-width: 1400px' not in content:
            content = re.sub(r'\.container\s*\{[^}]*\}', 
                           '.container {\n            max-width: 1400px;\n            margin: 0 auto;\n            padding: 20px;\n        }', 
                           content)
        
        # Salvar o arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, "Layout corrigido com sucesso"
        
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🎨 CORRIGINDO LAYOUT DAS PÁGINAS DE CATEGORIAS")
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
    error_count = 0
    
    print("📋 Corrigindo layout das páginas...")
    print()
    
    for page in category_pages:
        file_path = os.path.join(frontend_dir, page)
        
        if os.path.exists(file_path):
            success, message = fix_category_layout(file_path)
            
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
    print("📊 RESUMO DA CORREÇÃO")
    print(f"✅ Páginas corrigidas: {success_count}")
    print(f"❌ Páginas com erro: {error_count}")
    print()
    
    if success_count > 0:
        print("🎯 Correções aplicadas:")
        print("   • Grid de produtos corrigido")
        print("   • Layout responsivo otimizado")
        print("   • Cards com tamanho uniforme")
        print("   • Espaçamento adequado")
        print("   • Hover effects funcionais")
        print()
    
    print("🚀 Layout das páginas de categorias corrigido!")

if __name__ == "__main__":
    main()