#!/usr/bin/env python3
"""
Script para atualizar as categorias Casa, Games, Esportes e Infantil
com produtos modernos e ícones atualizados
"""

import os
import re

def update_casa_category():
    """Atualiza a categoria Casa"""
    casa_content = '''            <!-- Casa Category Content -->
            <div class="tab-content" id="casa-content">
                <div class="products-grid flash-products">
                    <!-- Produto 1: Sofá Retrátil 3 Lugares -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-30%</div>
                        <div class="product-image">
                            <i class="fas fa-couch product-icon" style="font-size: 80px; color: #8b4513;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Móveis</div>
                            <h3>Sofá Retrátil 3 Lugares</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star-half-alt"></i>
                                <span>(234)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 2.499,00</span>
                                <span class="new-price">R$ 1.749,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Sofá Retrátil 3 Lugares', 1749.00, 2499.00, 'Móveis')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 2: Cama Box Queen Size -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-25%</div>
                        <div class="product-image">
                            <i class="fas fa-bed product-icon" style="font-size: 80px; color: #6f42c1;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Camas</div>
                            <h3>Cama Box Queen Size</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <span>(456)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 1.599,00</span>
                                <span class="new-price">R$ 1.199,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Cama Box Queen Size', 1199.00, 1599.00, 'Camas')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 3: Geladeira Frost Free -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-20%</div>
                        <div class="product-image">
                            <i class="fas fa-snowflake product-icon" style="font-size: 80px; color: #17a2b8;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Eletrodomésticos</div>
                            <h3>Geladeira Frost Free 400L</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="far fa-star"></i>
                                <span>(189)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 2.799,00</span>
                                <span class="new-price">R$ 2.239,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Geladeira Frost Free 400L', 2239.00, 2799.00, 'Eletrodomésticos')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 4: Micro-ondas Digital -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-35%</div>
                        <div class="product-image">
                            <i class="fas fa-microchip product-icon" style="font-size: 80px; color: #fd7e14;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Eletrodomésticos</div>
                            <h3>Micro-ondas Digital 30L</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <span>(312)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 699,00</span>
                                <span class="new-price">R$ 454,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Micro-ondas Digital 30L', 454.00, 699.00, 'Eletrodomésticos')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 5: Mesa de Jantar 6 Lugares -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-28%</div>
                        <div class="product-image">
                            <i class="fas fa-utensils product-icon" style="font-size: 80px; color: #20c997;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Móveis</div>
                            <h3>Mesa de Jantar 6 Lugares</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="far fa-star"></i>
                                <span>(167)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 1.399,00</span>
                                <span class="new-price">R$ 1.007,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Mesa de Jantar 6 Lugares', 1007.00, 1399.00, 'Móveis')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 6: Aspirador de Pó Robô -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-45%</div>
                        <div class="product-image">
                            <i class="fas fa-robot product-icon" style="font-size: 80px; color: #e83e8c;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Limpeza</div>
                            <h3>Aspirador de Pó Robô</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star-half-alt"></i>
                                <span>(892)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 1.799,00</span>
                                <span class="new-price">R$ 989,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Aspirador de Pó Robô', 989.00, 1799.00, 'Limpeza')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                </div>
                <div class="view-all-container">
                    <a href="casa.html" class="view-all-btn">Ver Todos os Produtos para Casa</a>
                </div>
            </div>'''
    return casa_content

def update_games_category():
    """Atualiza a categoria Games"""
    games_content = '''            <!-- Games Category Content -->
            <div class="tab-content" id="games-content">
                <div class="products-grid flash-products">
                    <!-- Produto 1: Xbox Series X -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-20%</div>
                        <div class="product-image">
                            <i class="fab fa-xbox product-icon" style="font-size: 80px; color: #107c10;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Consoles</div>
                            <h3>Xbox Series X 1TB</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star-half-alt"></i>
                                <span>(1.456)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 4.499,00</span>
                                <span class="new-price">R$ 3.599,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Xbox Series X 1TB', 3599.00, 4499.00, 'Consoles')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 2: Nintendo Switch OLED -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-15%</div>
                        <div class="product-image">
                            <i class="fas fa-gamepad product-icon" style="font-size: 80px; color: #e60012;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Consoles</div>
                            <h3>Nintendo Switch OLED</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <span>(2.134)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 2.799,00</span>
                                <span class="new-price">R$ 2.379,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Nintendo Switch OLED', 2379.00, 2799.00, 'Consoles')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 3: Headset Gamer RGB -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-40%</div>
                        <div class="product-image">
                            <i class="fas fa-headset product-icon" style="font-size: 80px; color: #ff6b35;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Acessórios</div>
                            <h3>Headset Gamer RGB 7.1</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="far fa-star"></i>
                                <span>(567)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 499,00</span>
                                <span class="new-price">R$ 299,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Headset Gamer RGB 7.1', 299.00, 499.00, 'Acessórios')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 4: Teclado Mecânico Gamer -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-35%</div>
                        <div class="product-image">
                            <i class="fas fa-keyboard product-icon" style="font-size: 80px; color: #6610f2;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Periféricos</div>
                            <h3>Teclado Mecânico Gamer</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star-half-alt"></i>
                                <span>(789)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 599,00</span>
                                <span class="new-price">R$ 389,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Teclado Mecânico Gamer', 389.00, 599.00, 'Periféricos')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 5: Mouse Gamer Wireless -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-30%</div>
                        <div class="product-image">
                            <i class="fas fa-mouse product-icon" style="font-size: 80px; color: #dc3545;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Periféricos</div>
                            <h3>Mouse Gamer Wireless RGB</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <span>(1.234)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 399,00</span>
                                <span class="new-price">R$ 279,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Mouse Gamer Wireless RGB', 279.00, 399.00, 'Periféricos')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 6: Cadeira Gamer Pro -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-25%</div>
                        <div class="product-image">
                            <i class="fas fa-chair product-icon" style="font-size: 80px; color: #28a745;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Móveis Gamer</div>
                            <h3>Cadeira Gamer Pro RGB</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="far fa-star"></i>
                                <span>(445)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 1.599,00</span>
                                <span class="new-price">R$ 1.199,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Cadeira Gamer Pro RGB', 1199.00, 1599.00, 'Móveis Gamer')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                </div>
                <div class="view-all-container">
                    <a href="games.html" class="view-all-btn">Ver Todos os Produtos Gamer</a>
                </div>
            </div>'''
    return games_content

def update_esportes_category():
    """Atualiza a categoria Esportes"""
    esportes_content = '''            <!-- Esportes Category Content -->
            <div class="tab-content" id="esportes-content">
                <div class="products-grid flash-products">
                    <!-- Produto 1: Tênis Nike Air Max -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-35%</div>
                        <div class="product-image">
                            <i class="fas fa-running product-icon" style="font-size: 80px; color: #ff6b35;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Calçados</div>
                            <h3>Tênis Nike Air Max 270</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <span>(1.567)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 699,00</span>
                                <span class="new-price">R$ 454,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Tênis Nike Air Max 270', 454.00, 699.00, 'Calçados')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 2: Bicicleta Mountain Bike -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-20%</div>
                        <div class="product-image">
                            <i class="fas fa-bicycle product-icon" style="font-size: 80px; color: #28a745;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Ciclismo</div>
                            <h3>Bicicleta Mountain Bike Aro 29</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star-half-alt"></i>
                                <span>(234)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 1.999,00</span>
                                <span class="new-price">R$ 1.599,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Bicicleta Mountain Bike Aro 29', 1599.00, 1999.00, 'Ciclismo')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 3: Kit Halteres Ajustáveis -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-40%</div>
                        <div class="product-image">
                            <i class="fas fa-dumbbell product-icon" style="font-size: 80px; color: #6c757d;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Musculação</div>
                            <h3>Kit Halteres Ajustáveis 40kg</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="far fa-star"></i>
                                <span>(456)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 599,00</span>
                                <span class="new-price">R$ 359,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Kit Halteres Ajustáveis 40kg', 359.00, 599.00, 'Musculação')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 4: Bola de Futebol Oficial -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-25%</div>
                        <div class="product-image">
                            <i class="fas fa-futbol product-icon" style="font-size: 80px; color: #007bff;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Futebol</div>
                            <h3>Bola de Futebol Oficial FIFA</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <span>(789)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 199,00</span>
                                <span class="new-price">R$ 149,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Bola de Futebol Oficial FIFA', 149.00, 199.00, 'Futebol')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 5: Esteira Elétrica -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-30%</div>
                        <div class="product-image">
                            <i class="fas fa-tachometer-alt product-icon" style="font-size: 80px; color: #dc3545;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Fitness</div>
                            <h3>Esteira Elétrica Dobrável</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star-half-alt"></i>
                                <span>(167)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 2.499,00</span>
                                <span class="new-price">R$ 1.749,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Esteira Elétrica Dobrável', 1749.00, 2499.00, 'Fitness')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 6: Raquete de Tênis Pro -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-45%</div>
                        <div class="product-image">
                            <i class="fas fa-table-tennis product-icon" style="font-size: 80px; color: #ffc107;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Tênis</div>
                            <h3>Raquete de Tênis Profissional</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="far fa-star"></i>
                                <span>(89)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 899,00</span>
                                <span class="new-price">R$ 494,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Raquete de Tênis Profissional', 494.00, 899.00, 'Tênis')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                </div>
                <div class="view-all-container">
                    <a href="esportes.html" class="view-all-btn">Ver Todos os Produtos Esportivos</a>
                </div>
            </div>'''
    return esportes_content

def update_infantil_category():
    """Atualiza a categoria Infantil"""
    infantil_content = '''            <!-- Infantil Category Content -->
            <div class="tab-content" id="infantil-content">
                <div class="products-grid flash-products">
                    <!-- Produto 1: Tablet Infantil Educativo -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-30%</div>
                        <div class="product-image">
                            <i class="fas fa-tablet-alt product-icon" style="font-size: 80px; color: #ff6b35;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Eletrônicos</div>
                            <h3>Tablet Infantil Educativo 7"</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star-half-alt"></i>
                                <span>(567)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 499,00</span>
                                <span class="new-price">R$ 349,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Tablet Infantil Educativo 7', 349.00, 499.00, 'Eletrônicos')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 2: Bicicleta Infantil Aro 16 -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-25%</div>
                        <div class="product-image">
                            <i class="fas fa-bicycle product-icon" style="font-size: 80px; color: #e91e63;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Bicicletas</div>
                            <h3>Bicicleta Infantil Aro 16</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <span>(234)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 399,00</span>
                                <span class="new-price">R$ 299,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Bicicleta Infantil Aro 16', 299.00, 399.00, 'Bicicletas')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 3: Boneca Interativa -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-35%</div>
                        <div class="product-image">
                            <i class="fas fa-baby product-icon" style="font-size: 80px; color: #6f42c1;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Bonecas</div>
                            <h3>Boneca Interativa com Som</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="far fa-star"></i>
                                <span>(456)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 199,00</span>
                                <span class="new-price">R$ 129,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Boneca Interativa com Som', 129.00, 199.00, 'Bonecas')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 4: Kit LEGO Criativo -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-20%</div>
                        <div class="product-image">
                            <i class="fas fa-cubes product-icon" style="font-size: 80px; color: #28a745;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Blocos</div>
                            <h3>Kit LEGO Criativo 500 Peças</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <span>(789)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 249,00</span>
                                <span class="new-price">R$ 199,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Kit LEGO Criativo 500 Peças', 199.00, 249.00, 'Blocos')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 5: Carrinho de Controle Remoto -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-40%</div>
                        <div class="product-image">
                            <i class="fas fa-car product-icon" style="font-size: 80px; color: #007bff;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Carrinhos</div>
                            <h3>Carrinho RC Off-Road</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star-half-alt"></i>
                                <span>(345)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 299,00</span>
                                <span class="new-price">R$ 179,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Carrinho RC Off-Road', 179.00, 299.00, 'Carrinhos')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    
                    <!-- Produto 6: Quebra-Cabeça 1000 Peças -->
                    <div class="product-card flash-product">
                        <div class="product-badge flash-badge">-15%</div>
                        <div class="product-image">
                            <i class="fas fa-puzzle-piece product-icon" style="font-size: 80px; color: #ffc107;"></i>
                            <button class="wishlist-btn"><i class="far fa-heart"></i></button>
                        </div>
                        <div class="product-info">
                            <div class="product-category">Puzzles</div>
                            <h3>Quebra-Cabeça 1000 Peças</h3>
                            <div class="product-rating">
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="fas fa-star"></i>
                                <i class="far fa-star"></i>
                                <span>(123)</span>
                            </div>
                            <div class="product-price">
                                <span class="old-price">R$ 89,00</span>
                                <span class="new-price">R$ 75,00</span>
                            </div>
                            <button class="add-to-cart-btn flash-btn" onclick="addToCart('Quebra-Cabeça 1000 Peças', 75.00, 89.00, 'Puzzles')">
                                <i class="fas fa-shopping-cart"></i> Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                </div>
                <div class="view-all-container">
                    <a href="infantil.html" class="view-all-btn">Ver Todos os Produtos Infantis</a>
                </div>
            </div>'''
    return infantil_content

def main():
    """Função principal para atualizar todas as categorias"""
    file_path = os.path.join('BOSS-SHOP1', 'frontend', 'index.html')
    
    if not os.path.exists(file_path):
        print(f"Arquivo não encontrado: {file_path}")
        return
    
    # Ler o arquivo
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔄 Atualizando categorias...")
    
    # Atualizar Casa
    casa_pattern = r'<!-- Casa Category Content -->.*?</div>\s*\n\s*<!-- Games Category Content -->'
    casa_replacement = update_casa_category() + '\n            \n            <!-- Games Category Content -->'
    content = re.sub(casa_pattern, casa_replacement, content, flags=re.DOTALL)
    print("✅ Categoria Casa atualizada")
    
    # Atualizar Games
    games_pattern = r'<!-- Games Category Content -->.*?</div>\s*\n\s*<!-- Esportes Category Content -->'
    games_replacement = update_games_category() + '\n            \n            <!-- Esportes Category Content -->'
    content = re.sub(games_pattern, games_replacement, content, flags=re.DOTALL)
    print("✅ Categoria Games atualizada")
    
    # Atualizar Esportes
    esportes_pattern = r'<!-- Esportes Category Content -->.*?</div>\s*\n\s*<!-- Infantil Category Content -->'
    esportes_replacement = update_esportes_category() + '\n            \n            <!-- Infantil Category Content -->'
    content = re.sub(esportes_pattern, esportes_replacement, content, flags=re.DOTALL)
    print("✅ Categoria Esportes atualizada")
    
    # Atualizar Infantil
    infantil_pattern = r'<!-- Infantil Category Content -->.*?</div>\s*\n\s*</div>'
    infantil_replacement = update_infantil_category() + '\n        </div>'
    content = re.sub(infantil_pattern, infantil_replacement, content, flags=re.DOTALL)
    print("✅ Categoria Infantil atualizada")
    
    # Salvar o arquivo
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n🎉 Todas as categorias foram atualizadas com sucesso!")
    print("📋 Resumo das atualizações:")
    print("   • Casa: 6 produtos (móveis, eletrodomésticos, limpeza)")
    print("   • Games: 6 produtos (consoles, periféricos, acessórios)")
    print("   • Esportes: 6 produtos (fitness, futebol, ciclismo)")
    print("   • Infantil: 6 produtos (brinquedos, eletrônicos, educativos)")
    print("\n🎨 Melhorias aplicadas:")
    print("   • Ícones modernos Font Awesome")
    print("   • Produtos atuais e relevantes")
    print("   • Preços realistas com descontos")
    print("   • Avaliações e categorias organizadas")

if __name__ == "__main__":
    main()