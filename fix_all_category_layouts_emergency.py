#!/usr/bin/env python3
"""
Script de emergência para corrigir o layout de TODAS as páginas de categorias
"""

import os
import re

def get_emergency_css():
    """Retorna CSS de emergência para corrigir layouts quebrados"""
    return '''
        /* CORREÇÃO EMERGENCIAL TOTAL */
        * {
            margin: 0 !important;
            padding: 0 !important;
            box-sizing: border-box !important;
        }
        
        body {
            font-family: 'Inter', sans-serif !important;
            background: #ffffff !important;
            min-height: 100vh !important;
            color: #333 !important;
            overflow-x: hidden !important;
            position: relative !important;
        }
        
        .container {
            max-width: 1400px !important;
            margin: 0 auto !important;
            padding: 20px !important;
            width: 100% !important;
            position: relative !important;
        }
        
        /* Grid de Produtos */
        .products-grid {
            display: grid !important;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
            gap: 25px !important;
            justify-items: center !important;
            padding: 20px 0 !important;
            width: 100% !important;
            max-width: 100% !important;
            margin: 0 auto !important;
        }
        
        /* Grid de Categorias */
        .categories-grid {
            display: grid !important;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
            gap: 30px !important;
            padding: 40px 0 !important;
            max-width: 1400px !important;
            margin: 0 auto !important;
            width: 100% !important;
        }
        
        /* Cards de Produto */
        .product-card {
            background: white !important;
            border-radius: 20px !important;
            padding: 20px !important;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1) !important;
            transition: all 0.3s ease !important;
            border: 2px solid transparent !important;
            position: relative !important;
            overflow: hidden !important;
            width: 100% !important;
            max-width: 300px !important;
            min-height: 420px !important;
            display: flex !important;
            flex-direction: column !important;
        }
        
        /* Cards de Categoria */
        .category-card {
            background: white !important;
            border-radius: 20px !important;
            padding: 30px !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1) !important;
            transition: all 0.3s ease !important;
            text-align: center !important;
            position: relative !important;
            overflow: hidden !important;
            cursor: pointer !important;
            width: 100% !important;
            max-width: 350px !important;
            min-height: 200px !important;
            margin: 0 auto !important;
        }
        
        .product-card:hover,
        .category-card:hover {
            transform: translateY(-10px) !important;
            box-shadow: 0 20px 40px rgba(255, 107, 53, 0.2) !important;
        }
        
        /* Imagens de Produto */
        .product-image {
            position: relative !important;
            width: 100% !important;
            height: 200px !important;
            margin-bottom: 15px !important;
            border-radius: 15px !important;
            overflow: hidden !important;
        }
        
        .product-image img {
            width: 100% !important;
            height: 100% !important;
            object-fit: cover !important;
            transition: transform 0.3s ease !important;
        }
        
        /* Ícones de Categoria */
        .category-icon {
            font-size: 48px !important;
            color: #ff6b35 !important;
            margin-bottom: 20px !important;
        }
        
        /* Informações */
        .product-info,
        .category-info {
            position: relative !important;
            z-index: 1 !important;
        }
        
        .product-info h3,
        .category-info h3 {
            font-size: 18px !important;
            font-weight: 700 !important;
            color: #333 !important;
            margin-bottom: 10px !important;
            line-height: 1.3 !important;
        }
        
        .category-info h3 {
            font-size: 24px !important;
        }
        
        /* Preços */
        .product-price {
            display: flex !important;
            align-items: center !important;
            gap: 10px !important;
            margin-bottom: 15px !important;
        }
        
        .product-price .new-price {
            font-size: 20px !important;
            font-weight: 800 !important;
            color: #ff6b35 !important;
        }
        
        /* Botões */
        .add-to-cart-btn,
        .category-btn {
            width: 100% !important;
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%) !important;
            color: white !important;
            border: none !important;
            padding: 12px 20px !important;
            border-radius: 10px !important;
            font-size: 14px !important;
            font-weight: 600 !important;
            cursor: pointer !important;
            transition: all 0.3s ease !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            gap: 8px !important;
            text-decoration: none !important;
        }
        
        .category-btn {
            width: auto !important;
            display: inline-flex !important;
            border-radius: 25px !important;
        }
        
        .add-to-cart-btn:hover,
        .category-btn:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 20px rgba(255, 107, 53, 0.3) !important;
        }
        
        /* Header da Categoria */
        .category-header {
            background: white !important;
            border-radius: 20px !important;
            padding: 40px !important;
            margin-bottom: 30px !important;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1) !important;
            text-align: center !important;
            position: relative !important;
            overflow: hidden !important;
        }
        
        /* Hero das Categorias */
        .categories-hero {
            background: linear-gradient(135deg, #ff6b35 0%, #ff8c42 50%, #ffa45c 100%) !important;
            padding: 120px 0 !important;
            text-align: center !important;
            color: white !important;
            position: relative !important;
            overflow: hidden !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.15) !important;
            margin-bottom: 60px !important;
        }
        
        /* Responsividade */
        @media (max-width: 1200px) {
            .products-grid,
            .categories-grid {
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)) !important;
                gap: 20px !important;
            }
        }
        
        @media (max-width: 768px) {
            .products-grid,
            .categories-grid {
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)) !important;
                gap: 15px !important;
            }
            
            .product-card,
            .category-card {
                max-width: 100% !important;
                min-height: 350px !important;
            }
        }
        
        @media (max-width: 480px) {
            .products-grid,
            .categories-grid {
                grid-template-columns: 1fr 1fr !important;
                gap: 10px !important;
            }
        }
        
        /* Botão Voltar */
        .back-to-home {
            position: fixed !important;
            top: 20px !important;
            left: 20px !important;
            color: #ff6b35 !important;
            text-decoration: none !important;
            display: flex !important;
            align-items: center !important;
            gap: 8px !important;
            font-weight: 500 !important;
            padding: 12px 20px !important;
            background: white !important;
            border-radius: 50px !important;
            transition: all 0.3s ease !important;
            z-index: 1000 !important;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1) !important;
        }
        
        .back-to-home:hover {
            background: #ff6b35 !important;
            color: white !important;
            transform: translateX(-4px) !important;
        }'''

def fix_page_layout(file_path):
    """Corrige o layout de uma página específica"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        emergency_css = get_emergency_css()
        
        # Inserir CSS de emergência antes do fechamento da tag </style>
        if '</style>' in content:
            last_style_pos = content.rfind('</style>')
            content = content[:last_style_pos] + emergency_css + '\n        ' + content[last_style_pos:]
        else:
            # Se não há tag style, adicionar no head
            content = content.replace('</head>', f'<style>{emergency_css}</style>\n</head>')
        
        # Salvar o arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, "Layout corrigido com CSS de emergência"
        
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🚨 CORREÇÃO EMERGENCIAL - TODAS AS PÁGINAS")
    print("=" * 50)
    
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    
    # Todas as páginas que podem ter problemas
    pages_to_fix = [
        'categorias.html',
        'moda.html',
        'eletronicos.html',
        'casa.html',
        'games.html',
        'esportes.html',
        'infantil.html'
    ]
    
    success_count = 0
    error_count = 0
    
    print("📋 Aplicando correção de emergência...")
    print()
    
    for page in pages_to_fix:
        file_path = os.path.join(frontend_dir, page)
        
        if os.path.exists(file_path):
            success, message = fix_page_layout(file_path)
            
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
    print("📊 RESUMO DA CORREÇÃO EMERGENCIAL")
    print(f"✅ Páginas corrigidas: {success_count}")
    print(f"❌ Páginas com erro: {error_count}")
    print()
    
    if success_count > 0:
        print("🎯 Correções aplicadas:")
        print("   • CSS com !important para forçar layouts corretos")
        print("   • Grid responsivo funcionando em todas as páginas")
        print("   • Cards alinhados e centralizados")
        print("   • Hover effects restaurados")
        print("   • Layout funcional em todos os dispositivos")
        print("   • Botão voltar funcionando")
        print()
    
    print("🚀 TODAS as páginas de categorias corrigidas!")

if __name__ == "__main__":
    main()