#!/usr/bin/env python3
"""
Script para padronizar as cores das páginas de categorias
Converte todas para o esquema laranja e branco
"""

import os
import re

def update_category_colors():
    """Atualiza as cores de todas as páginas de categorias para laranja e branco"""
    
    # Diretório das páginas
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    
    # Páginas de categorias para atualizar
    category_pages = [
        'moda.html',
        'eletronicos.html', 
        'casa.html',
        'games.html',
        'esportes.html',
        'infantil.html'
    ]
    
    # Padrões de cores para substituir
    color_patterns = {
        # Backgrounds gradientes coloridos -> branco
        r'background: linear-gradient\(135deg, #[a-fA-F0-9]{6} 0%, #[a-fA-F0-9]{6}.*?\);': 'background: #ffffff;',
        r'background: linear-gradient\(135deg, #[a-fA-F0-9]{3,6} 0%, #[a-fA-F0-9]{3,6}.*?\);': 'background: #ffffff;',
        
        # Cores específicas para laranja
        r'color: #667eea;': 'color: #ff6b35;',
        r'color: #56ab2f;': 'color: #ff6b35;',
        r'color: #8B5CF6;': 'color: #ff6b35;',
        r'color: #10B981;': 'color: #ff6b35;',
        r'color: #FF6B9D;': 'color: #ff6b35;',
        
        # Gradientes de texto para laranja
        r'background: linear-gradient\(135deg, #667eea 0%, #764ba2 100%\);': 'background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);',
        r'background: linear-gradient\(135deg, #56ab2f 0%, #a8e6cf 100%\);': 'background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);',
        r'background: linear-gradient\(135deg, #8B5CF6 0%, #A855F7 100%\);': 'background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);',
        r'background: linear-gradient\(135deg, #10B981 0%, #059669 100%\);': 'background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);',
        r'background: linear-gradient\(135deg, #FF6B9D 0%, #C084FC 100%\);': 'background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);',
        
        # Gradientes de fundo rgba para laranja
        r'background: linear-gradient\(135deg, rgba\(102, 126, 234, 0\.05\) 0%, rgba\(118, 75, 162, 0\.05\) 100%\);': 'background: linear-gradient(135deg, rgba(255, 107, 53, 0.05) 0%, rgba(247, 147, 30, 0.05) 100%);',
        r'background: linear-gradient\(135deg, rgba\(86, 171, 47, 0\.05\) 0%, rgba\(168, 230, 207, 0\.05\) 100%\);': 'background: linear-gradient(135deg, rgba(255, 107, 53, 0.05) 0%, rgba(247, 147, 30, 0.05) 100%);',
        r'background: linear-gradient\(135deg, rgba\(139, 92, 246, 0\.05\) 0%, rgba\(168, 85, 247, 0\.05\) 100%\);': 'background: linear-gradient(135deg, rgba(255, 107, 53, 0.05) 0%, rgba(247, 147, 30, 0.05) 100%);',
        r'background: linear-gradient\(135deg, rgba\(16, 185, 129, 0\.05\) 0%, rgba\(5, 150, 105, 0\.05\) 100%\);': 'background: linear-gradient(135deg, rgba(255, 107, 53, 0.05) 0%, rgba(247, 147, 30, 0.05) 100%);',
        r'background: linear-gradient\(135deg, rgba\(255, 107, 157, 0\.05\) 0%, rgba\(192, 132, 252, 0\.05\) 100%\);': 'background: linear-gradient(135deg, rgba(255, 107, 53, 0.05) 0%, rgba(247, 147, 30, 0.05) 100%);',
    }
    
    updated_files = []
    
    for page in category_pages:
        file_path = os.path.join(frontend_dir, page)
        
        if not os.path.exists(file_path):
            print(f"❌ Arquivo não encontrado: {file_path}")
            continue
            
        try:
            # Ler o arquivo
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Aplicar todas as substituições de cores
            for pattern, replacement in color_patterns.items():
                content = re.sub(pattern, replacement, content)
            
            # Substituir o background do body para branco
            content = re.sub(
                r'body\s*\{[^}]*background:[^;]*;',
                'body {\n            font-family: \'Inter\', sans-serif;\n            background: #ffffff;',
                content
            )
            
            # Verificar se houve mudanças
            if content != original_content:
                # Salvar o arquivo atualizado
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                updated_files.append(page)
                print(f"✅ Atualizado: {page}")
            else:
                print(f"ℹ️ Sem mudanças: {page}")
                
        except Exception as e:
            print(f"❌ Erro ao processar {page}: {e}")
    
    return updated_files

def main():
    print("🎨 ATUALIZANDO CORES DAS CATEGORIAS")
    print("=" * 50)
    print("Convertendo todas as categorias para laranja e branco...")
    print()
    
    updated_files = update_category_colors()
    
    print()
    print("=" * 50)
    print("📊 RESUMO DA ATUALIZAÇÃO")
    print(f"✅ Arquivos atualizados: {len(updated_files)}")
    
    if updated_files:
        print("\n📁 Arquivos modificados:")
        for file in updated_files:
            print(f"   • {file}")
        
        print("\n🎯 Mudanças aplicadas:")
        print("   • Background do body: branco (#ffffff)")
        print("   • Ícones e títulos: laranja (#ff6b35)")
        print("   • Gradientes: laranja para dourado (#ff6b35 → #f7931e)")
        print("   • Elementos de destaque: tons de laranja")
        
    print("\n🚀 Todas as categorias agora usam o padrão laranja e branco!")

if __name__ == "__main__":
    main()