#!/usr/bin/env python3
"""
Script para deixar os cards dos produtos muito mais bonitos
"""

import os
import re

def get_beautiful_card_css():
    """Retorna CSS para cards de produtos muito mais bonitos"""
    return '''
        /* CARDS DE PRODUTOS PREMIUM */
        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 35px;
            justify-items: center;
            padding: 40px 0;
            max-width: 1400px;
            margin: 0 auto;
        }
        
        .product-card {
            background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
            border-radius: 25px;
            padding: 0;
            box-shadow: 
                0 20px 40px rgba(0, 0, 0, 0.08),
                0 8px 16px rgba(0, 0, 0, 0.04),
                inset 0 1px 0 rgba(255, 255, 255, 0.9);
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: 1px solid rgba(255, 255, 255, 0.2);
            position: relative;
            overflow: hidden;
            width: 100%;
            max-width: 380px;
            min-height: 520px;
            display: flex;
            flex-direction: column;
            backdrop-filter: blur(10px);
        }
        
        .product-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(135deg, 
                rgba(255, 107, 53, 0.03) 0%, 
                rgba(247, 147, 30, 0.03) 50%,
                rgba(255, 107, 53, 0.03) 100%);
            opacity: 0;
            transition: opacity 0.4s ease;
            z-index: 0;
        }
        
        .product-card:hover::before {
            opacity: 1;
        }
        
        .product-card:hover {
            transform: translateY(-15px) scale(1.02);
            box-shadow: 
                0 35px 70px rgba(255, 107, 53, 0.15),
                0 15px 30px rgba(0, 0, 0, 0.1),
                inset 0 1px 0 rgba(255, 255, 255, 1);
            border-color: rgba(255, 107, 53, 0.2);
        }
        
        /* BADGE DE DESCONTO PREMIUM */
        .product-badge {
            position: absolute;
            top: 20px;
            left: 20px;
            background: linear-gradient(135deg, #ff4757 0%, #ff3742 100%);
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            z-index: 10;
            box-shadow: 0 8px 16px rgba(255, 71, 87, 0.3);
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        /* IMAGEM DO PRODUTO PREMIUM */
        .product-image {
            position: relative;
            width: 100%;
            height: 260px;
            margin: 0;
            border-radius: 25px 25px 0 0;
            overflow: hidden;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        }
        
        .product-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            filter: brightness(1.05) contrast(1.1);
        }
        
        .product-card:hover .product-image img {
            transform: scale(1.1) rotate(2deg);
            filter: brightness(1.1) contrast(1.15) saturate(1.1);
        }
        
        /* BOTÃO WISHLIST PREMIUM */
        .wishlist-btn {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border: none;
            width: 45px;
            height: 45px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.4s ease;
            z-index: 10;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        }
        
        .wishlist-btn:hover {
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
            color: white;
            transform: scale(1.1);
            box-shadow: 0 12px 24px rgba(255, 107, 53, 0.3);
        }
        
        .wishlist-btn i {
            font-size: 18px;
            transition: all 0.3s ease;
        }
        
        /* INFORMAÇÕES DO PRODUTO PREMIUM */
        .product-info {
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 25px;
            position: relative;
            z-index: 1;
        }
        
        .product-category {
            font-size: 11px;
            color: #ff6b35;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 12px;
            padding: 4px 12px;
            background: linear-gradient(135deg, rgba(255, 107, 53, 0.1) 0%, rgba(247, 147, 30, 0.1) 100%);
            border-radius: 15px;
            display: inline-block;
            width: fit-content;
        }
        
        .product-info h3 {
            font-size: 20px;
            font-weight: 700;
            color: #2c3e50;
            margin-bottom: 15px;
            line-height: 1.3;
            flex: 1;
            background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        /* AVALIAÇÕES PREMIUM */
        .product-rating {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 18px;
            padding: 8px 0;
        }
        
        .product-rating i {
            color: #ffd700;
            font-size: 16px;
            text-shadow: 0 2px 4px rgba(255, 215, 0, 0.3);
            transition: all 0.3s ease;
        }
        
        .product-card:hover .product-rating i {
            transform: scale(1.1);
        }
        
        .product-rating span {
            color: #7f8c8d;
            font-size: 14px;
            font-weight: 500;
            margin-left: 8px;
            background: rgba(127, 140, 141, 0.1);
            padding: 2px 8px;
            border-radius: 10px;
        }
        
        /* PREÇOS PREMIUM */
        .product-price {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 25px;
            padding: 15px 0;
            border-top: 1px solid rgba(0, 0, 0, 0.05);
            border-bottom: 1px solid rgba(0, 0, 0, 0.05);
        }
        
        .new-price {
            font-size: 28px;
            font-weight: 800;
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            text-shadow: 0 2px 4px rgba(255, 107, 53, 0.2);
        }
        
        .old-price {
            font-size: 16px;
            color: #95a5a6;
            text-decoration: line-through;
            font-weight: 500;
            background: rgba(149, 165, 166, 0.1);
            padding: 2px 8px;
            border-radius: 8px;
        }
        
        /* BOTÃO ADICIONAR AO CARRINHO PREMIUM */
        .add-to-cart-btn {
            width: 100%;
            background: linear-gradient(135deg, #ff6b35 0%, #f7931e 50%, #ff8c42 100%);
            color: white;
            border: none;
            padding: 18px 25px;
            border-radius: 15px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            position: relative;
            overflow: hidden;
            box-shadow: 
                0 8px 16px rgba(255, 107, 53, 0.3),
                inset 0 1px 0 rgba(255, 255, 255, 0.2);
        }
        
        .add-to-cart-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.6s ease;
        }
        
        .add-to-cart-btn:hover::before {
            left: 100%;
        }
        
        .add-to-cart-btn:hover {
            transform: translateY(-3px);
            box-shadow: 
                0 15px 30px rgba(255, 107, 53, 0.4),
                inset 0 1px 0 rgba(255, 255, 255, 0.3);
            background: linear-gradient(135deg, #f7931e 0%, #ff6b35 50%, #ff4757 100%);
        }
        
        .add-to-cart-btn:active {
            transform: translateY(-1px);
        }
        
        .add-to-cart-btn i {
            font-size: 18px;
            transition: all 0.3s ease;
        }
        
        .add-to-cart-btn:hover i {
            transform: scale(1.2);
        }
        
        /* RESPONSIVIDADE PREMIUM */
        @media (max-width: 1200px) {
            .products-grid {
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
            }
            
            .product-card {
                max-width: 350px;
            }
        }
        
        @media (max-width: 768px) {
            .products-grid {
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 25px;
                padding: 30px 0;
            }
            
            .product-card {
                max-width: 100%;
                min-height: 480px;
            }
            
            .product-image {
                height: 220px;
            }
            
            .product-info {
                padding: 20px;
            }
        }
        
        @media (max-width: 480px) {
            .products-grid {
                grid-template-columns: 1fr;
                gap: 20px;
                padding: 20px 0;
            }
            
            .product-card {
                min-height: 450px;
            }
            
            .product-image {
                height: 200px;
            }
        }
        
        /* ANIMAÇÕES EXTRAS */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .product-card {
            animation: fadeInUp 0.6s ease-out;
        }
        
        .product-card:nth-child(1) { animation-delay: 0.1s; }
        .product-card:nth-child(2) { animation-delay: 0.2s; }
        .product-card:nth-child(3) { animation-delay: 0.3s; }
        .product-card:nth-child(4) { animation-delay: 0.4s; }
        .product-card:nth-child(5) { animation-delay: 0.5s; }
        .product-card:nth-child(6) { animation-delay: 0.6s; }'''

def beautify_page_cards(file_path):
    """Aplica o CSS bonito aos cards de uma página"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        beautiful_css = get_beautiful_card_css()
        
        # Encontrar e substituir CSS dos produtos
        product_css_pattern = r'(\.products-grid\s*\{.*?\.product-card:nth-child\(\d+\)\s*\{[^}]*\})'
        
        if re.search(product_css_pattern, content, re.DOTALL):
            content = re.sub(product_css_pattern, beautiful_css, content, flags=re.DOTALL)
        else:
            # Se não encontrar o padrão específico, inserir antes do fechamento do style
            if '</style>' in content:
                last_style_pos = content.rfind('</style>')
                content = content[:last_style_pos] + beautiful_css + '\n        ' + content[last_style_pos:]
        
        # Salvar arquivo
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return True, "Cards embelezados com sucesso"
        
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("✨ EMBELEZANDO CARDS DOS PRODUTOS")
    print("=" * 50)
    
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    
    pages_to_beautify = [
        'moda.html',
        'eletronicos.html',
        'casa.html',
        'games.html',
        'esportes.html',
        'infantil.html',
        'index.html'
    ]
    
    success_count = 0
    
    for page in pages_to_beautify:
        file_path = os.path.join(frontend_dir, page)
        
        if os.path.exists(file_path):
            success, message = beautify_page_cards(file_path)
            
            if success:
                print(f"✨ {page} - {message}")
                success_count += 1
            else:
                print(f"❌ {page} - {message}")
        else:
            print(f"⚠️ {page} - Arquivo não encontrado")
    
    print()
    print("=" * 50)
    print(f"✨ {success_count} páginas embelezadas com sucesso!")
    print()
    print("🎨 Melhorias aplicadas:")
    print("   • Gradientes premium nos cards")
    print("   • Sombras avançadas com múltiplas camadas")
    print("   • Animações suaves e modernas")
    print("   • Hover effects espetaculares")
    print("   • Badges de desconto animados")
    print("   • Botões com efeitos de brilho")
    print("   • Tipografia com gradientes")
    print("   • Backdrop blur nos elementos")
    print("   • Animações de entrada escalonadas")
    print("   • Design responsivo premium")
    print()
    print("🚀 Cards agora têm visual PREMIUM!")

if __name__ == "__main__":
    main()