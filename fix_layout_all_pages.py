#!/usr/bin/env python3
"""
Script para corrigir o layout de todas as páginas que possuem rodapé
Evita sobreposição entre conteúdo e rodapé
"""

import os
import re

def fix_page_layout(file_path):
    """Corrige o layout de uma página específica"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar se a página tem rodapé
        if 'modern-footer' not in content:
            return False, "Página não possui rodapé"
        
        # Verificar se já foi corrigida
        if 'page-wrapper' in content or 'login-wrapper' in content or 'register-wrapper' in content:
            return False, "Já possui correção de layout"
        
        original_content = content
        
        # Padrões de CSS problemáticos para corrigir
        css_fixes = [
            # Body com display flex centralizando tudo
            (r'body\s*\{([^}]*?)display:\s*flex;([^}]*?)align-items:\s*center;([^}]*?)justify-content:\s*center;([^}]*?)\}',
             r'body {\1\2\3\4}'),
            
            # Body com min-height 100vh sem espaço para rodapé
            (r'body\s*\{([^}]*?)min-height:\s*100vh;([^}]*?)padding:\s*20px;([^}]*?)\}',
             r'body {\1min-height: 100vh;\2padding: 20px 20px 0 20px;\3}'),
            
            # Adicionar classe wrapper se necessário
        ]
        
        # Aplicar correções de CSS
        for pattern, replacement in css_fixes:
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        # Adicionar CSS para wrapper se não existir
        if '.page-wrapper' not in content:
            wrapper_css = '''
        .page-wrapper {
            display: flex;
            flex-direction: column;
            min-height: calc(100vh - 40px);
            padding-bottom: 40px;
        }

        .content-wrapper {
            flex: 1;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px 0;
        }'''
            
            # Inserir CSS antes do </style>
            content = re.sub(r'(</style>)', wrapper_css + r'\1', content)
        
        # Encontrar o conteúdo principal e envolver com wrapper
        # Procurar por containers principais comuns
        main_containers = [
            r'(<div class="auth-container">)',
            r'(<div class="profile-container">)',
            r'(<div class="cart-container">)',
            r'(<div class="container">.*?<div class="category-header">)',
            r'(<div class="container">.*?<h1>)',
        ]
        
        wrapped = False
        for pattern in main_containers:
            if re.search(pattern, content, re.DOTALL):
                # Envolver o conteúdo principal
                content = re.sub(
                    r'(<body[^>]*>)(.*?)(<div class="back-to-home">.*?</a>)?(.*?)(' + pattern + ')',
                    r'\1\2\3<div class="page-wrapper"><div class="content-wrapper">\5',
                    content,
                    flags=re.DOTALL
                )
                
                # Fechar os wrappers antes do footer
                content = re.sub(
                    r'(</div>\s*</div>\s*)(<!-- Footer|<footer)',
                    r'\1</div></div>\2',
                    content
                )
                wrapped = True
                break
        
        # Se não encontrou container específico, tentar wrapper genérico
        if not wrapped:
            # Procurar por qualquer div principal após o body
            body_pattern = r'(<body[^>]*>)(.*?)(<div class="back-to-home">.*?</a>)?(.*?)(<div[^>]*>)'
            if re.search(body_pattern, content, re.DOTALL):
                content = re.sub(
                    body_pattern,
                    r'\1\2\3<div class="page-wrapper"><div class="content-wrapper">\5',
                    content,
                    flags=re.DOTALL
                )
                
                # Fechar antes do footer
                content = re.sub(
                    r'(</div>\s*)(<!-- Footer|<footer)',
                    r'</div></div>\1\2',
                    content
                )
                wrapped = True
        
        # Verificar se houve mudanças
        if content != original_content:
            # Salvar arquivo
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, "Layout corrigido com sucesso"
        else:
            return False, "Nenhuma mudança necessária"
            
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🔧 CORRIGINDO LAYOUT DE TODAS AS PÁGINAS")
    print("=" * 50)
    
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    
    # Páginas que podem precisar de correção
    pages_to_check = [
        'profile.html',
        'purchase.html',
        'moda.html',
        'eletronicos.html',
        'casa.html',
        'games.html',
        'esportes.html',
        'infantil.html',
        'central-ajuda.html',
        'como-comprar.html',
        'frete-entrega.html',
        'devolucoes.html',
        'rastrear-pedido.html',
        'nossa-historia.html',
        'trabalhe-conosco.html',
        'imprensa.html',
        'investidores.html',
        'categorias.html',
        'atendimento.html',
        'cupons.html'
    ]
    
    success_count = 0
    already_fixed_count = 0
    no_footer_count = 0
    error_count = 0
    
    print("📋 Verificando páginas...")
    print()
    
    for page in pages_to_check:
        file_path = os.path.join(frontend_dir, page)
        
        if os.path.exists(file_path):
            success, message = fix_page_layout(file_path)
            
            if success:
                print(f"✅ {page} - {message}")
                success_count += 1
            elif "Já possui correção" in message:
                print(f"ℹ️ {page} - {message}")
                already_fixed_count += 1
            elif "não possui rodapé" in message:
                print(f"⚠️ {page} - {message}")
                no_footer_count += 1
            else:
                print(f"❌ {page} - {message}")
                error_count += 1
        else:
            print(f"📄 {page} - Arquivo não encontrado")
    
    print()
    print("=" * 50)
    print("📊 RESUMO DA CORREÇÃO")
    print(f"✅ Páginas corrigidas: {success_count}")
    print(f"ℹ️ Páginas já corrigidas: {already_fixed_count}")
    print(f"⚠️ Páginas sem rodapé: {no_footer_count}")
    print(f"❌ Páginas com erro: {error_count}")
    print()
    
    if success_count > 0:
        print("🎯 Correções aplicadas:")
        print("   • CSS do body ajustado para evitar sobreposição")
        print("   • Wrapper adicionado para controle de layout")
        print("   • Espaçamento adequado para o rodapé")
        print("   • Responsividade mantida")
        print()
    
    print("🚀 Layout corrigido em todas as páginas com rodapé!")

if __name__ == "__main__":
    main()