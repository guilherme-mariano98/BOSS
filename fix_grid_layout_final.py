#!/usr/bin/env python3
"""
Script para corrigir definitivamente o layout em grid das páginas de categorias
"""

import os
import re

def fix_grid_layout(file_path):
    """Corrige o layout em grid de uma página"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Adicionar CSS específico para forçar o grid correto
        grid_fix_css = '''
        /* CORREÇÃO FORÇADA DO GRID */
        .products-grid {
            display: grid !important;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) !important;
            gap: 25px !important;
            justify-items: center !important;
            padding: 20px 0 !important;
            width: 100% !important;
            max-width: 100% !important;
        }
        
        .product-card {
            width: 100% !important;
            max-width: 300px !important;
            min-height: 420px !important;
            display: flex !important;
            flex-direction: column !important;
        }
        
        .container {
            max-width: 1400px !important;
            margin: 0 auto !important;
            padding: 20px !important;
            width: 100% !important;
        }
        
        /* Responsividade forçada */
        @media (max-width: 1200px) {
            .products-grid {
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)) !important;
                gap: 20px !important;
            }
        }
        
        @media (max-width: 768px) {
            .products-grid {
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)) !important;
                gap: 15px !important;
            }
        }
        
        @media (max-width: 480px) {
            .products-grid {
                grid-template-columns: 1fr 1fr !important;
                gap: 10px !important;
            }
        }
        '''
        
        # Inserir o CSS antes do fechamento da tag </style>
        if '</style>' in content:
            content = content.replace('</style>', grid_fix_css + '\n        </style>')
        else:
            # Se não há tag style, adicionar no head
            content = content.replace('</head>', f'<style>{grid_fix_css}</style>\n</head>')
        
        # Salvar o arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, "Grid layout corrigido com !important"
        
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🔧 CORREÇÃO FINAL DO LAYOUT EM GRID")
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
    
    print("📋 Aplicando correção forçada do grid...")
    print()
    
    for page in category_pages:
        file_path = os.path.join(frontend_dir, page)
        
        if os.path.exists(file_path):
            success, message = fix_grid_layout(file_path)
            
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
        print("   • CSS com !important para forçar grid")
        print("   • Layout responsivo garantido")
        print("   • Grid de 2-4 colunas dependendo da tela")
        print("   • Espaçamento otimizado")
        print()
    
    print("🚀 Layout em grid forçado com sucesso!")

if __name__ == "__main__":
    main()