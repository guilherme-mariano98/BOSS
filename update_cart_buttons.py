#!/usr/bin/env python3
"""
Script para atualizar os botões de "Comprar Agora" para "Adicionar ao Carrinho"
"""

import os

def update_cart_buttons():
    # Caminho para o arquivo index.html
    file_path = os.path.join('BOSS-SHOP1', 'frontend', 'index.html')
    
    if not os.path.exists(file_path):
        print(f"Arquivo não encontrado: {file_path}")
        return
    
    # Ler o arquivo
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fazer a substituição
    old_text = '<i class="fas fa-shopping-cart"></i> Comprar Agora'
    new_text = '<i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho'
    
    # Contar ocorrências antes da substituição
    count_before = content.count(old_text)
    print(f"Encontradas {count_before} ocorrências de 'Comprar Agora'")
    
    # Fazer a substituição
    updated_content = content.replace(old_text, new_text)
    
    # Contar ocorrências após a substituição
    count_after = updated_content.count(old_text)
    count_new = updated_content.count(new_text)
    
    print(f"Após substituição: {count_after} 'Comprar Agora' restantes, {count_new} 'Adicionar ao Carrinho' criados")
    
    # Salvar o arquivo atualizado
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    
    print(f"✅ Arquivo atualizado com sucesso!")
    print(f"📝 Todos os botões agora mostram 'Adicionar ao Carrinho'")

if __name__ == "__main__":
    update_cart_buttons()