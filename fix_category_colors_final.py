#!/usr/bin/env python3
"""
Script final para garantir que todas as categorias usem apenas laranja e branco
"""

import os
import re

def fix_all_category_colors():
    """Corrige todas as cores das páginas de categorias"""
    
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    category_pages = ['moda.html', 'eletronicos.html', 'casa.html', 'games.html', 'esportes.html', 'infantil.html']
    
    for page in category_pages:
        file_path = os.path.join(frontend_dir, page)
        
        if not os.path.exists(file_path):
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Substituições específicas para garantir laranja e branco
        replacements = [
            # Background do body sempre branco
            (r'background: linear-gradient\([^)]+\);', 'background: #ffffff;'),
            
            # Títulos com gradiente laranja
            (r'background: #ffffff;(\s*-webkit-background-clip: text;\s*-webkit-text-fill-color: transparent;)', 
             'background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);\\1'),
            
            # Ícones sempre laranja
            (r'color: #[a-fA-F0-9]{6};(\s*margin-bottom: 20px;\s*display: block;\s*})', 
             'color: #ff6b35;\\1'),
            
            # Stats numbers laranja
            (r'color: #[a-fA-F0-9]{6};(\s*display: block;\s*})', 
             'color: #ff6b35;\\1'),
            
            # Botões com gradiente laranja
            (r'background: linear-gradient\([^)]+\);(\s*color: white;)', 
             'background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);\\1'),
            
            # Hover states laranja
            (r'background: #[a-fA-F0-9]{6};(\s*color: white;\s*})', 
             'background: #ff6b35;\\1'),
            
            # Border colors laranja
            (r'border-color: #[a-fA-F0-9]{6};', 'border-color: #ff6b35;'),
        ]
        
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
        
        # Salvar arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Corrigido: {page}")

if __name__ == "__main__":
    print("🔧 CORREÇÃO FINAL DAS CORES")
    print("=" * 40)
    fix_all_category_colors()
    print("🎨 Todas as categorias agora usam apenas laranja e branco!")