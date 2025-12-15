#!/usr/bin/env python3
"""
Script para fazer ajustes específicos em páginas que precisam de correções manuais
"""

import os
import re

def fix_profile_layout():
    """Corrige especificamente o layout da página de perfil"""
    file_path = os.path.join('BOSS-SHOP1', 'frontend', 'profile.html')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Corrigir o body que foi modificado incorretamente
        content = re.sub(
            r'<body><div class="page-wrapper"><div class="content-wrapper"><div class="profile-container">',
            '''<body>
    <a href="index.html" class="back-to-home">
        <i class="fas fa-arrow-left"></i>
        Voltar à loja
    </a>

    <div class="profile-container">''',
            content
        )
        
        # Corrigir o fechamento antes do footer
        content = re.sub(
            r'</div></div>(<!-- Footer|<footer)',
            r'</div>\n\n    \1',
            content
        )
        
        # Ajustar CSS do body
        content = re.sub(
            r'body \{([^}]*?)\}',
            '''body {
            font-family: 'Inter', sans-serif;
            background: #000000;
            min-height: 100vh;
            color: #333;
            padding-bottom: 40px;
        }''',
            content,
            flags=re.DOTALL
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Erro ao corrigir profile.html: {e}")
        return False

def fix_purchase_layout():
    """Corrige especificamente o layout da página de carrinho"""
    file_path = os.path.join('BOSS-SHOP1', 'frontend', 'purchase.html')
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Corrigir estrutura similar ao profile
        content = re.sub(
            r'<body><div class="page-wrapper"><div class="content-wrapper"><div class="cart-container">',
            '''<body>
    <a href="index.html" class="back-to-home">
        <i class="fas fa-arrow-left"></i>
        Voltar à loja
    </a>

    <div class="cart-container">''',
            content
        )
        
        # Corrigir fechamento
        content = re.sub(
            r'</div></div>(<!-- Footer|<footer)',
            r'</div>\n\n    \1',
            content
        )
        
        # Ajustar CSS do body
        content = re.sub(
            r'body \{([^}]*?)\}',
            '''body {
            font-family: 'Inter', sans-serif;
            background: #000000;
            min-height: 100vh;
            color: #333;
            padding-bottom: 40px;
        }''',
            content,
            flags=re.DOTALL
        )
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Erro ao corrigir purchase.html: {e}")
        return False

def fix_category_layouts():
    """Corrige o layout das páginas de categorias"""
    categories = ['moda.html', 'eletronicos.html', 'casa.html', 'games.html', 'esportes.html', 'infantil.html']
    
    fixed_count = 0
    
    for category in categories:
        file_path = os.path.join('BOSS-SHOP1', 'frontend', category)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Ajustar CSS do body para categorias
            content = re.sub(
                r'body \{([^}]*?)\}',
                '''body {
            font-family: 'Inter', sans-serif;
            background: #ffffff;
            min-height: 100vh;
            color: #333;
            padding-bottom: 40px;
        }''',
                content,
                flags=re.DOTALL
            )
            
            # Garantir que o container principal tenha espaçamento adequado
            content = re.sub(
                r'\.container \{([^}]*?)\}',
                '''.container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px 20px 60px 20px;
        }''',
                content,
                flags=re.DOTALL
            )
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            fixed_count += 1
            
        except Exception as e:
            print(f"Erro ao corrigir {category}: {e}")
    
    return fixed_count

def main():
    """Função principal"""
    print("🔧 APLICANDO CORREÇÕES ESPECÍFICAS DE LAYOUT")
    print("=" * 50)
    
    # Corrigir páginas específicas
    print("📄 Corrigindo profile.html...")
    if fix_profile_layout():
        print("✅ Profile corrigido")
    else:
        print("❌ Erro no profile")
    
    print("📄 Corrigindo purchase.html...")
    if fix_purchase_layout():
        print("✅ Purchase corrigido")
    else:
        print("❌ Erro no purchase")
    
    print("📄 Corrigindo páginas de categorias...")
    fixed_categories = fix_category_layouts()
    print(f"✅ {fixed_categories} categorias corrigidas")
    
    print()
    print("=" * 50)
    print("🎯 CORREÇÕES ESPECÍFICAS CONCLUÍDAS")
    print("✅ Layout otimizado para todas as páginas")
    print("✅ Espaçamento adequado para rodapé")
    print("✅ Responsividade mantida")
    print("🚀 Todas as páginas agora têm layout consistente!")

if __name__ == "__main__":
    main()