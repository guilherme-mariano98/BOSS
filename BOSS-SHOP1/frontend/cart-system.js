// Sistema de Carrinho - BOSS SHOPP
// Arquivo separado para evitar conflitos

console.log('🛒 Sistema de carrinho carregado');

// Cart functionality
let cart = JSON.parse(localStorage.getItem('cart') || '[]');

// Add to cart function
function addToCart(name, price, originalPrice = null, category = 'Produto', image = null) {
    console.log('🛒 addToCart chamada:', { name, price, originalPrice, category, image });
    
    // Generate unique ID based on name and timestamp
    const id = Date.now() + Math.random();
    
    const product = {
        id: id,
        name: name,
        price: parseFloat(price),
        originalPrice: originalPrice ? parseFloat(originalPrice) : null,
        category: category,
        image: image,
        quantity: 1
    };

    console.log('📦 Produto criado:', product);

    // Check if product already exists in cart
    const existingItem = cart.find(item => item.name === name && item.price === price);
    
    if (existingItem) {
        existingItem.quantity += 1;
        console.log('✅ Quantidade atualizada:', existingItem);
        showNotification(`Quantidade de "${name}" atualizada!`, 'success');
    } else {
        cart.push(product);
        console.log('✅ Produto adicionado ao carrinho:', product);
        showNotification(`"${name}" adicionado ao carrinho!`, 'success');
    }
    
    // Save to localStorage
    localStorage.setItem('cart', JSON.stringify(cart));
    console.log('💾 Carrinho salvo:', cart);
    
    // Update cart count
    updateCartCount();
    console.log('🔢 Contador atualizado');
    
    return true;
}

// Update cart count in navigation
function updateCartCount() {
    const cartCountElements = document.querySelectorAll('.cart-count');
    const itemCount = cart.reduce((sum, item) => sum + item.quantity, 0);
    
    console.log('🔢 Atualizando contador:', itemCount, 'elementos encontrados:', cartCountElements.length);
    
    cartCountElements.forEach((element, index) => {
        if (element) {
            element.textContent = itemCount;
            element.style.display = itemCount > 0 ? 'block' : 'none';
            console.log(`🔢 Elemento ${index} atualizado:`, element);
        }
    });
}

// Show notification message
function showNotification(message, type = 'success') {
    console.log('🔔 Mostrando notificação:', message, type);
    
    // Remove any existing notifications
    const existingNotification = document.querySelector('.notification');
    if (existingNotification) {
        existingNotification.remove();
    }
    
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: ${type === 'success' ? '#00aa00' : '#ff4444'};
        color: white;
        padding: 15px 20px;
        border-radius: 5px;
        z-index: 10000;
        font-weight: bold;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    `;
    notification.textContent = message;
    
    // Add to document
    document.body.appendChild(notification);
    
    // Remove after 3 seconds
    setTimeout(() => {
        notification.remove();
    }, 3000);
}

// Initialize cart count on page load
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Inicializando sistema de carrinho...');
    updateCartCount();
    console.log('✅ Sistema de carrinho inicializado');
});

// Export functions for global use
window.addToCart = addToCart;
window.updateCartCount = updateCartCount;
window.showNotification = showNotification;
window.cart = cart;

console.log('✅ Funções do carrinho exportadas globalmente');