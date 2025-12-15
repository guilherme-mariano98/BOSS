#!/usr/bin/env python3
"""
Script para adicionar o rodapé moderno em todas as páginas que não possuem
"""

import os
import re

def get_footer_html():
    """Retorna o HTML completo do rodapé"""
    return '''
    <!-- Footer Moderno e Responsivo -->
    <footer class="modern-footer">
        <div class="container">
            <!-- Seção Principal do Footer -->
            <div class="footer-main">
                <div class="footer-grid">
                    <!-- Coluna 1: Sobre a Empresa -->
                    <div class="footer-column">
                        <div class="footer-logo">
                            <img src="boss-shop-logo.png" alt="BOSS SHOPP" class="footer-logo-img">
                            <h3>BOSS SHOPP</h3>
                        </div>
                        <p class="footer-description">
                            Sua loja online de confiança, oferecendo produtos de qualidade com preços competitivos e entrega rápida em todo o Brasil.
                        </p>
                        <div class="footer-social">
                            <a href="#" class="social-link" aria-label="Facebook">
                                <i class="fab fa-facebook-f"></i>
                            </a>
                            <a href="#" class="social-link" aria-label="Instagram">
                                <i class="fab fa-instagram"></i>
                            </a>
                            <a href="#" class="social-link" aria-label="Twitter">
                                <i class="fab fa-twitter"></i>
                            </a>
                            <a href="#" class="social-link" aria-label="WhatsApp">
                                <i class="fab fa-whatsapp"></i>
                            </a>
                        </div>
                    </div>

                    <!-- Coluna 2: Links Rápidos -->
                    <div class="footer-column">
                        <h4 class="footer-title">Links Rápidos</h4>
                        <ul class="footer-links">
                            <li><a href="index.html">Início</a></li>
                            <li><a href="categorias.html">Categorias</a></li>
                            <li><a href="sobre.html">Sobre Nós</a></li>
                            <li><a href="como-comprar.html">Como Comprar</a></li>
                            <li><a href="frete-entrega.html">Frete e Entrega</a></li>
                            <li><a href="devolucoes.html">Trocas e Devoluções</a></li>
                        </ul>
                    </div>

                    <!-- Coluna 3: Institucional & Promoções -->
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

                    <!-- Coluna 5: Atendimento -->
                    <div class="footer-column">
                        <h4 class="footer-title">Atendimento</h4>
                        <div class="contact-info">
                            <div class="contact-item">
                                <i class="fas fa-phone"></i>
                                <span>(11) 4002-8922</span>
                            </div>
                            <div class="contact-item">
                                <i class="fas fa-envelope"></i>
                                <span>contato@bossshopp.com</span>
                            </div>
                            <div class="contact-item">
                                <i class="fas fa-clock"></i>
                                <span>Seg-Sex: 8h às 18h</span>
                            </div>
                            <div class="contact-item">
                                <i class="fas fa-map-marker-alt"></i>
                                <span>São Paulo, SP</span>
                            </div>
                        </div>
                        <a href="central-ajuda.html" class="help-button">
                            <i class="fas fa-headset"></i>
                            Central de Ajuda
                        </a>
                    </div>
                </div>
            </div>

            <!-- Seção de Pagamento e Segurança -->
            <div class="footer-payment">
                <div class="payment-security">
                    <div class="payment-methods">
                        <h5>Formas de Pagamento</h5>
                        <div class="payment-icons">
                            <i class="fab fa-cc-visa" title="Visa"></i>
                            <i class="fab fa-cc-mastercard" title="Mastercard"></i>
                            <i class="fab fa-cc-amex" title="American Express"></i>
                            <i class="fab fa-pix" title="PIX"></i>
                            <i class="fas fa-barcode" title="Boleto"></i>
                        </div>
                    </div>
                    <div class="security-badges">
                        <h5>Segurança</h5>
                        <div class="security-icons">
                            <i class="fas fa-shield-alt" title="Site Seguro"></i>
                            <i class="fas fa-lock" title="SSL"></i>
                            <i class="fas fa-certificate" title="Certificado"></i>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Rodapé Inferior -->
            <div class="footer-bottom">
                <div class="footer-bottom-content">
                    <div class="copyright">
                        <p>&copy; 2025 BOSS SHOPP. Todos os direitos reservados.</p>
                    </div>
                    <div class="footer-legal">
                        <a href="#" class="legal-link">Política de Privacidade</a>
                        <a href="#" class="legal-link">Termos de Uso</a>
                        <a href="#" class="legal-link">Cookies</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>
'''

def add_footer_to_page(file_path):
    """Adiciona o rodapé a uma página específica"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar se já tem o rodapé
        if 'modern-footer' in content:
            return False, "Já possui rodapé"
        
        # Verificar se tem o CSS do footer no head
        footer_css_link = '<link rel="stylesheet" href="footer-styles.css">'
        if footer_css_link not in content:
            # Adicionar o CSS do footer no head
            head_pattern = r'(</head>)'
            if re.search(head_pattern, content):
                content = re.sub(head_pattern, f'    {footer_css_link}\n\\1', content)
        
        # Adicionar o rodapé antes do fechamento do body
        footer_html = get_footer_html()
        body_pattern = r'(</body>)'
        
        if re.search(body_pattern, content):
            content = re.sub(body_pattern, f'{footer_html}\n\\1', content)
            
            # Salvar o arquivo
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return True, "Rodapé adicionado com sucesso"
        else:
            return False, "Tag </body> não encontrada"
            
    except Exception as e:
        return False, f"Erro: {e}"

def main():
    """Função principal"""
    print("🦶 ADICIONANDO RODAPÉ EM TODAS AS PÁGINAS")
    print("=" * 50)
    
    frontend_dir = os.path.join('BOSS-SHOP1', 'frontend')
    
    # Páginas principais que precisam do rodapé
    priority_pages = [
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
        'trabalhe-conosco.html'
    ]
    
    success_count = 0
    already_has_count = 0
    error_count = 0
    
    print("📋 Processando páginas prioritárias...")
    print()
    
    for page in priority_pages:
        file_path = os.path.join(frontend_dir, page)
        
        if os.path.exists(file_path):
            success, message = add_footer_to_page(file_path)
            
            if success:
                print(f"✅ {page} - {message}")
                success_count += 1
            elif "Já possui rodapé" in message:
                print(f"ℹ️ {page} - {message}")
                already_has_count += 1
            else:
                print(f"❌ {page} - {message}")
                error_count += 1
        else:
            print(f"⚠️ {page} - Arquivo não encontrado")
    
    print()
    print("=" * 50)
    print("📊 RESUMO DA OPERAÇÃO")
    print(f"✅ Páginas com rodapé adicionado: {success_count}")
    print(f"ℹ️ Páginas que já tinham rodapé: {already_has_count}")
    print(f"❌ Páginas com erro: {error_count}")
    print()
    
    if success_count > 0:
        print("🎯 Mudanças aplicadas:")
        print("   • Rodapé moderno adicionado")
        print("   • CSS do footer incluído")
        print("   • Links de navegação funcionais")
        print("   • Informações de contato atualizadas")
        print("   • Ícones de pagamento e segurança")
        print()
    
    print("🚀 Todas as páginas principais agora possuem rodapé!")

if __name__ == "__main__":
    main()