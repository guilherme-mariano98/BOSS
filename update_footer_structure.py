#!/usr/bin/env python3
"""
Script para atualizar a estrutura do rodapé de 4 colunas para 5 colunas
Adicionando a seção "Institucional & Promoções"
"""

import os
import re

def update_footer_structure(file_path):
    """Atualiza a estrutura do rodapé em uma página específica"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar se já tem a nova estrutura
        if 'Institucional & Promoções' in content or 'Institucional</h4>' in content:
            return False, "Já possui nova estrutura"
        
        # Padrão para encontrar a coluna 3 atual (Categorias)
        old_column_3_pattern = r'(<!-- Coluna 3: Categorias -->.*?</div>\s*<!-- Coluna 4: Atendimento -->)'
        
        # Nova estrutura com 5 colunas
        new_columns_3_4_5 = '''<!-- Coluna 3: Institucional & Promoções -->
                    <div class="footer-column">
                        <h4 class="footer-title">Institucional</h4>
                        <ul class="footer-links">
                            <li><a href="nossa-historia.html">Nossa História</a></li>
                            <li><a href="trabalhe-conosco.html">Trabalhe Conosco</a></li>
                            <li><a href="imprensa.html">Imprensa</a></li>
                            <li><a href="investidores.html">Investidores</a></li>
                        </ul>
                        <h4 class="footer-title" style="margin-top: 30px;">Promoções</h4>
                        <ul class="footer-links">
                            <li><a href="cupons.html">Cupons de Desconto</a></li>
                            <li><a href="ofertas.html">Ofertas Especiais</a></li>
                        </ul>
                    </div>

                    <!-- Coluna 4: Categorias -->
                    <div class="footer-column">
                        <h4 class="footer-title">Categorias</h4>
                        <ul class="footer-links">
                            <li><a href="moda.html">Moda</a></li>
                            <li><a href="eletronicos.html">Eletrônicos</a></li>
                            <li><a href="casa.html">Casa e Decoração</a></li>
                            <li><a href="esportes.html">Esportes</a></li>
                            <li><a href="games.html">Games</a></li>
                            <li><a href="infantil.html">Infantil</a></li>
                        </ul>
                    </div>

                    <!-- Coluna 5: Atendimento -->'''
        
        # Fazer a substituição
        if re.search(old_column_3_pattern, content, re.DOTALL):
            content = re.sub(old_column_3_pattern, new_columns_3_4_5, content, flags=re.DOTALL)
            
            # Salvar o arquivo
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True, "Estrutura atualizada com sucesso"
        else:
            return False, "Padrão não encontrado"
            
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🔄 ATUALIZANDO ESTRUTURA DO RODAPÉ")
    print("=" * 50)
    
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    
    # Páginas que precisam da atualização
    pages_to_update = [
        'login.html',
        'register.html', 
        'profile.html',
        'purchase.html',
        'moda.html',
        'eletronicos.html',
        'casa.html',
        'games.html',
        'esportes.html',
        'infantil.html',
        'devolucoes.html',
        'frete-entrega.html',
        'imprensa.html',
        'investidores.html',
        'nossa-historia.html',
        'rastrear-pedido.html',
        'trabalhe-conosco.html',
        'cupons.html',
        'ofertas.html',
        'central-ajuda.html',
        'como-comprar.html'
    ]
    
    success_count = 0
    already_updated_count = 0
    error_count = 0
    
    print("📋 Atualizando estrutura do rodapé...")
    print()
    
    for page in pages_to_update:
        file_path = os.path.join(frontend_dir, page)
        
        if os.path.exists(file_path):
            success, message = update_footer_structure(file_path)
            
            if success:
                print(f"✅ {page} - {message}")
                success_count += 1
            elif "Já possui nova estrutura" in message:
                print(f"ℹ️ {page} - {message}")
                already_updated_count += 1
            else:
                print(f"❌ {page} - {message}")
                error_count += 1
        else:
            print(f"⚠️ {page} - Arquivo não encontrado")
    
    print()
    print("=" * 50)
    print("📊 RESUMO DA OPERAÇÃO")
    print(f"✅ Páginas atualizadas: {success_count}")
    print(f"ℹ️ Páginas já atualizadas: {already_updated_count}")
    print(f"❌ Páginas com erro: {error_count}")
    print()
    
    if success_count > 0:
        print("🎯 Mudanças aplicadas:")
        print("   • Estrutura do rodapé atualizada para 5 colunas")
        print("   • Adicionada seção 'Institucional & Promoções'")
        print("   • Links para páginas institucionais")
        print("   • Links para páginas promocionais")
        print("   • Categorias movidas para coluna 4")
        print("   • Atendimento movido para coluna 5")
        print()
    
    print("🚀 Estrutura do rodapé atualizada em todas as páginas!")

if __name__ == "__main__":
    main()