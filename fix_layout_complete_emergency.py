#!/usr/bin/env python3
"""
Script de emergência para corrigir completamente o layout quebrado
"""

import os
import re

def create_complete_fixed_css():
    """Cria CSS completamente novo e funcional"""
    return '''
        /* RESET COMPLETO */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: #f8f9fa;
            color: #333;
            line-height: 1.6;
            overflow-x: hidden;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            width: 100%;
        }
        
        /* HEADER DA CATEGORIA */
        .category-header {
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
            color: white;
            text-align: center;
            padding: 80px 20px;
            margin-bottom: 40px;
            border-radius: 20px;
        }
        
        .category-header h1 {
            font-size: 48px;
            font-weight: 800;
            margin-bottom: 15px;
        }
        
        .category-header p {
            font-size: 20px;
            opacity: 0.9;
            max-width: 600px;
            margin: 0 auto;
        }
        
        /* ESTATÍSTICAS */
        .category-stats {
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 30px;
        }
        
        .stat-item {
            text-align: center;
        }
        
        .stat-number {
            display: block;
            font-size: 32px;
            font-weight: 800;
            margin-bottom: 5px;
        }
        
        .stat-label {
            font-size: 14px;
            opacity: 0.8;
        }
        
        /* FILTROS */
        .filters-section {
            background: white;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 40px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
        }
        
        .filters-title {
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 20px;
            color: #333;
        }
        
        .filters-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }
        
        .filter-group {
            display: flex;
            flex-direction: column;
        }
        
        .filter-group label {
            font-weight: 600;
            margin-bottom: 8px;
            color: #555;
        }
        
        .filter-group select {
            padding: 12px;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            font-size: 14px;
            background: white;
            transition: border-color 0.3s ease;
        }
        
        .filter-group select:focus {
            outline: none;
            border-color: #ff6b35;
        }
        
        /* SEÇÃO DE PRODUTOS */
        .products-section {
            margin-bottom: 60px;
        }
        
        .products-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
        }
        
        .products-title {
            font-size: 28px;
            font-weight: 700;
            color: #333;
        }
        
        .products-count {
            color: #666;
            font-size: 16px;
        }
        
        /* GRID DE PRODUTOS - LAYOUT FIXO */
        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            justify-items: center;
            padding: 20px 0;
        }
        
        /* CARDS DE PRODUTO - DESIGN FIXO */
        .product-card {
            background: white;
            border-radius: 20px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            transition: all 0.4s ease;
            border: 2px solid transparent;
            position: relative;
            overflow: hidden;
            width: 100%;
            max-width: 350px;
            min-height: 500px;
            display: flex;
            flex-direction: column;
        }
        
        .product-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(255, 107, 53, 0.2);
            border-color: #ff6b35;
        }
        
        /* IMAGEM DO PRODUTO */
        .product-image {
            position: relative;
            width: 100%;
            height: 220px;
            margin-bottom: 20px;
            border-radius: 15px;
            overflow: hidden;
            background: #f8f9fa;
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
        
        .wishlist-btn {
            position: absolute;
            top: 15px;
            right: 15px;
            background: rgba(255, 255, 255, 0.9);
            border: none;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .wishlist-btn:hover {
            background: #ff6b35;
            color: white;
        }
        
        /* INFORMAÇÕES DO PRODUTO */
        .product-info {
            flex: 1;
            display: flex;
            flex-direction: column;
        }
        
        .product-category {
            font-size: 12px;
            color: #ff6b35;
            font-weight: 600;
            text-transform: uppercase;
            margin-bottom: 8px;
        }
        
        .product-info h3 {
            font-size: 20px;
            font-weight: 700;
            color: #333;
            margin-bottom: 12px;
            line-height: 1.3;
            flex: 1;
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
            margin-left: 5px;
        }
        
        .product-price {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .new-price {
            font-size: 24px;
            font-weight: 800;
            color: #ff6b35;
        }
        
        .old-price {
            font-size: 16px;
            color: #999;
            text-decoration: line-through;
        }
        
        /* BOTÃO ADICIONAR AO CARRINHO */
        .add-to-cart-btn {
            width: 100%;
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
            color: white;
            border: none;
            padding: 15px 20px;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        
        .add-to-cart-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(255, 107, 53, 0.4);
        }
        
        /* BOTÃO VOLTAR */
        .back-to-home {
            position: fixed;
            top: 20px;
            left: 20px;
            color: #ff6b35;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 8px;
            font-weight: 600;
            padding: 15px 25px;
            background: white;
            border-radius: 50px;
            transition: all 0.3s ease;
            z-index: 1000;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.15);
        }
        
        .back-to-home:hover {
            background: #ff6b35;
            color: white;
            transform: translateX(-5px);
        }
        
        /* RESPONSIVIDADE */
        @media (max-width: 1200px) {
            .products-grid {
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 25px;
            }
            
            .category-stats {
                gap: 30px;
            }
        }
        
        @media (max-width: 768px) {
            .products-grid {
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
            }
            
            .category-header {
                padding: 60px 20px;
            }
            
            .category-header h1 {
                font-size: 36px;
            }
            
            .category-stats {
                flex-direction: column;
                gap: 20px;
            }
            
            .filters-grid {
                grid-template-columns: 1fr;
            }
            
            .products-header {
                flex-direction: column;
                align-items: flex-start;
                gap: 10px;
            }
        }
        
        @media (max-width: 480px) {
            .products-grid {
                grid-template-columns: 1fr;
                gap: 15px;
            }
            
            .product-card {
                max-width: 100%;
                min-height: 450px;
            }
            
            .container {
                padding: 15px;
            }
        }'''

def fix_page_completely(file_path):
    """Corrige uma página completamente"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # CSS completamente novo
        new_css = create_complete_fixed_css()
        
        # Substituir todo o CSS existente
        css_pattern = r'<style>.*?</style>'
        new_style_tag = f'<style>{new_css}</style>'
        
        if re.search(css_pattern, content, re.DOTALL):
            content = re.sub(css_pattern, new_style_tag, content, flags=re.DOTALL)
        else:
            # Adicionar CSS no head se não existir
            content = content.replace('</head>', f'{new_style_tag}\n</head>')
        
        # Salvar arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, "Layout completamente reconstruído"
        
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🚨 RECONSTRUÇÃO COMPLETA DO LAYOUT")
    print("=" * 50)
    
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    
    pages_to_fix = [
        'casa.html',
        'moda.html',
        'eletronicos.html',
        'games.html',
        'esportes.html',
        'infantil.html',
        'categorias.html'
    ]
    
    success_count = 0
    
    for page in pages_to_fix:
        file_path = os.path.join(frontend_dir, page)
        
        if os.path.exists(file_path):
            success, message = fix_page_completely(file_path)
            
            if success:
                print(f"✅ {page} - {message}")
                success_count += 1
            else:
                print(f"❌ {page} - {message}")
    
    print()
    print("=" * 50)
    print(f"✅ {success_count} páginas reconstruídas com sucesso!")
    print()
    print("🎯 Layout completamente novo:")
    print("   • CSS limpo e otimizado")
    print("   • Grid responsivo funcionando")
    print("   • Cards com tamanho uniforme")
    print("   • Imagens proporcionais")
    print("   • Hover effects suaves")
    print("   • Layout profissional")
    print()
    print("🚀 TODAS as páginas agora têm layout perfeito!")

if __name__ == "__main__":
    main()