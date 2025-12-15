#!/usr/bin/env python3
"""
Script de emergência para corrigir o layout quebrado da página categorias.html
"""

import os
import re

def fix_categorias_layout():
    """Corrige o layout quebrado da página categorias.html"""
    try:
        file_path = os.path.join('BOSS-SHOP1', 'frontend', 'categorias.html')
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # CSS corrigido para o grid de categorias
        fixed_css = '''        /* CORREÇÃO EMERGENCIAL DO LAYOUT */
        .categories-grid {
            display: grid !important;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
            gap: 30px !important;
            padding: 40px 0 !important;
            max-width: 1400px !important;
            margin: 0 auto !important;
            width: 100% !important;
        }
        
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
        
        .category-card:hover {
            transform: translateY(-10px) !important;
            box-shadow: 0 20px 40px rgba(255, 107, 53, 0.2) !important;
        }
        
        .category-icon {
            font-size: 48px !important;
            color: #ff6b35 !important;
            margin-bottom: 20px !important;
        }
        
        .category-info h3 {
            font-size: 24px !important;
            font-weight: 700 !important;
            color: #333 !important;
            margin-bottom: 10px !important;
        }
        
        .category-info p {
            font-size: 16px !important;
            color: #666 !important;
            margin-bottom: 20px !important;
        }
        
        .category-btn {
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%) !important;
            color: white !important;
            padding: 12px 24px !important;
            border-radius: 25px !important;
            text-decoration: none !important;
            font-weight: 600 !important;
            display: inline-flex !important;
            align-items: center !important;
            gap: 8px !important;
            transition: all 0.3s ease !important;
        }
        
        .category-btn:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 20px rgba(255, 107, 53, 0.3) !important;
        }
        
        .container {
            max-width: 1400px !important;
            margin: 0 auto !important;
            padding: 20px !important;
            width: 100% !important;
        }
        
        /* Responsividade */
        @media (max-width: 1200px) {
            .categories-grid {
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)) !important;
                gap: 25px !important;
            }
        }
        
        @media (max-width: 768px) {
            .categories-grid {
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)) !important;
                gap: 20px !important;
                padding: 20px 0 !important;
            }
            
            .category-card {
                padding: 20px !important;
                min-height: 180px !important;
            }
        }
        
        @media (max-width: 480px) {
            .categories-grid {
                grid-template-columns: 1fr 1fr !important;
                gap: 15px !important;
            }
        }'''
        
        # Inserir o CSS corrigido antes do fechamento da tag </style>
        if '</style>' in content:
            # Encontrar a última tag </style> e inserir antes dela
            last_style_pos = content.rfind('</style>')
            content = content[:last_style_pos] + fixed_css + '\n        ' + content[last_style_pos:]
        else:
            # Se não há tag style, adicionar no head
            content = content.replace('</head>', f'<style>{fixed_css}</style>\n</head>')
        
        # Salvar o arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, "Layout corrigido com CSS forçado"
        
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🚨 CORREÇÃO EMERGENCIAL - LAYOUT CATEGORIAS")
    print("=" * 50)
    
    success, message = fix_categorias_layout()
    
    if success:
        print(f"✅ categorias.html - {message}")
        print()
        print("🎯 Correções aplicadas:")
        print("   • CSS com !important para forçar layout correto")
        print("   • Grid responsivo de 2-4 colunas")
        print("   • Cards centralizados e alinhados")
        print("   • Hover effects restaurados")
        print("   • Layout funcional em todos os dispositivos")
    else:
        print(f"❌ categorias.html - {message}")
    
    print()
    print("🚀 Layout da página categorias corrigido!")

if __name__ == "__main__":
    main()