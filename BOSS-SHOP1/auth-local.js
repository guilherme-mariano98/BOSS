// Sistema de Autenticação Local - BOSS SHOPP
// Funciona sem backend, usando localStorage

// Configurações
const AUTH_CONFIG = {
    tokenKey: 'boss_shopp_token',
    userKey: 'boss_shopp_user',
    usersKey: 'boss_shopp_users'
};

// Inicializar usuários demo se não existirem
function initializeDemoUsers() {
    const users = getStoredUsers();
    if (users.length === 0) {
        const demoUsers = [
            {
                id: 1,
                name: 'Admin Demo',
                email: 'admin@bosshopp.com',
                password: 'admin123',
                type: 'admin',
                created: new Date().toISOString()
            },
            {
                id: 2,
                name: 'Cliente Demo',
                email: 'cliente@email.com',
                password: '123456',
                type: 'customer',
                created: new Date().toISOString()
            }
        ];
        localStorage.setItem(AUTH_CONFIG.usersKey, JSON.stringify(demoUsers));
    }
}

// Obter usuários armazenados
function getStoredUsers() {
    const users = localStorage.getItem(AUTH_CONFIG.usersKey);
    return users ? JSON.parse(users) : [];
}

// Salvar usuários
function saveUsers(users) {
    localStorage.setItem(AUTH_CONFIG.usersKey, JSON.stringify(users));
}

// Gerar token simples
function generateToken(user) {
    const tokenData = {
        id: user.id,
        email: user.email,
        name: user.name,
        type: user.type,
        timestamp: Date.now()
    };
    return btoa(JSON.stringify(tokenData));
}

// Validar token
function validateToken(token) {
    try {
        const tokenData = JSON.parse(atob(token));
        // Token válido por 24 horas
        const isValid = (Date.now() - tokenData.timestamp) < (24 * 60 * 60 * 1000);
        return isValid ? tokenData : null;
    } catch (error) {
        return null;
    }
}

// Função de Login
async function handleLogin(formData) {
    try {
        // Inicializar usuários demo
        initializeDemoUsers();
        
        // Obter dados do formulário
        const email = formData.get('email') || document.getElementById('loginEmail').value;
        const password = formData.get('password') || document.getElementById('loginPassword').value;
        
        if (!email || !password) {
            return { success: false, message: 'Email e senha são obrigatórios' };
        }
        
        // Buscar usuário
        const users = getStoredUsers();
        const user = users.find(u => u.email.toLowerCase() === email.toLowerCase());
        
        if (!user) {
            return { success: false, message: 'Email não encontrado' };
        }
        
        // Verificar senha
        if (user.password !== password) {
            return { success: false, message: 'Senha incorreta' };
        }
        
        // Gerar token e salvar sessão
        const token = generateToken(user);
        const userData = {
            id: user.id,
            name: user.name,
            email: user.email,
            type: user.type
        };
        
        localStorage.setItem(AUTH_CONFIG.tokenKey, token);
        localStorage.setItem(AUTH_CONFIG.userKey, JSON.stringify(userData));
        
        return { 
            success: true, 
            message: 'Login realizado com sucesso!',
            user: userData,
            token: token
        };
        
    } catch (error) {
        console.error('Erro no login:', error);
        return { success: false, message: 'Erro interno. Tente novamente.' };
    }
}

// Função de Registro
async function handleRegister(formData) {
    try {
        // Inicializar usuários demo
        initializeDemoUsers();
        
        // Obter dados do formulário
        const firstName = formData.get('firstName') || document.getElementById('firstName').value;
        const lastName = formData.get('lastName') || document.getElementById('lastName').value;
        const email = formData.get('email') || document.getElementById('registerEmail').value;
        const password = formData.get('password') || document.getElementById('registerPassword').value;
        
        if (!firstName || !lastName || !email || !password) {
            return { success: false, message: 'Todos os campos são obrigatórios' };
        }
        
        if (password.length < 6) {
            return { success: false, message: 'Senha deve ter pelo menos 6 caracteres' };
        }
        
        // Verificar se email já existe
        const users = getStoredUsers();
        const existingUser = users.find(u => u.email.toLowerCase() === email.toLowerCase());
        
        if (existingUser) {
            return { success: false, message: 'Email já está em uso' };
        }
        
        // Criar novo usuário
        const newUser = {
            id: users.length + 1,
            name: `${firstName} ${lastName}`,
            email: email.toLowerCase(),
            password: password,
            type: 'customer',
            created: new Date().toISOString()
        };
        
        // Salvar usuário
        users.push(newUser);
        saveUsers(users);
        
        // Fazer login automático
        const token = generateToken(newUser);
        const userData = {
            id: newUser.id,
            name: newUser.name,
            email: newUser.email,
            type: newUser.type
        };
        
        localStorage.setItem(AUTH_CONFIG.tokenKey, token);
        localStorage.setItem(AUTH_CONFIG.userKey, JSON.stringify(userData));
        
        return { 
            success: true, 
            message: 'Conta criada com sucesso!',
            user: userData,
            token: token
        };
        
    } catch (error) {
        console.error('Erro no registro:', error);
        return { success: false, message: 'Erro interno. Tente novamente.' };
    }
}

// Verificar se usuário está logado
function isLoggedIn() {
    const token = localStorage.getItem(AUTH_CONFIG.tokenKey);
    if (!token) return false;
    
    const tokenData = validateToken(token);
    return tokenData !== null;
}

// Obter usuário atual
function getCurrentUser() {
    const userStr = localStorage.getItem(AUTH_CONFIG.userKey);
    return userStr ? JSON.parse(userStr) : null;
}

// Logout
function logout() {
    localStorage.removeItem(AUTH_CONFIG.tokenKey);
    localStorage.removeItem(AUTH_CONFIG.userKey);
    
    // Redirecionar para login
    if (window.location.pathname !== '/login.html') {
        window.location.href = 'login.html';
    }
}

// Mostrar toast de notificação
function showToast(message, type = 'info') {
    // Remover toast existente
    const existingToast = document.querySelector('.auth-toast');
    if (existingToast) {
        existingToast.remove();
    }
    
    // Criar novo toast
    const toast = document.createElement('div');
    toast.className = `auth-toast auth-toast-${type}`;
    toast.innerHTML = `
        <div class="auth-toast-content">
            <span class="auth-toast-message">${message}</span>
            <button class="auth-toast-close" onclick="this.parentElement.parentElement.remove()">×</button>
        </div>
    `;
    
    // Adicionar estilos se não existirem
    if (!document.querySelector('#auth-toast-styles')) {
        const styles = document.createElement('style');
        styles.id = 'auth-toast-styles';
        styles.textContent = `
            .auth-toast {
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 10000;
                min-width: 300px;
                max-width: 500px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                animation: slideInRight 0.3s ease-out;
            }
            
            .auth-toast-success {
                background: #d4edda;
                border: 1px solid #c3e6cb;
                color: #155724;
            }
            
            .auth-toast-error {
                background: #f8d7da;
                border: 1px solid #f5c6cb;
                color: #721c24;
            }
            
            .auth-toast-info {
                background: #d1ecf1;
                border: 1px solid #bee5eb;
                color: #0c5460;
            }
            
            .auth-toast-content {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 12px 16px;
            }
            
            .auth-toast-message {
                flex: 1;
                font-weight: 500;
            }
            
            .auth-toast-close {
                background: none;
                border: none;
                font-size: 18px;
                font-weight: bold;
                cursor: pointer;
                margin-left: 10px;
                opacity: 0.7;
            }
            
            .auth-toast-close:hover {
                opacity: 1;
            }
            
            @keyframes slideInRight {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
        `;
        document.head.appendChild(styles);
    }
    
    // Adicionar ao DOM
    document.body.appendChild(toast);
    
    // Remover automaticamente após 5 segundos
    setTimeout(() => {
        if (toast.parentElement) {
            toast.remove();
        }
    }, 5000);
}

// Inicializar quando a página carregar
document.addEventListener('DOMContentLoaded', function() {
    initializeDemoUsers();
    
    // Verificar se está logado e atualizar interface
    if (isLoggedIn()) {
        const user = getCurrentUser();
        console.log('Usuário logado:', user);
        
        // Atualizar elementos da interface se existirem
        const userNameElements = document.querySelectorAll('.user-name');
        userNameElements.forEach(el => {
            if (user && user.name) {
                el.textContent = user.name;
            }
        });
        
        const loginButtons = document.querySelectorAll('.login-btn');
        loginButtons.forEach(btn => {
            btn.style.display = 'none';
        });
        
        const logoutButtons = document.querySelectorAll('.logout-btn');
        logoutButtons.forEach(btn => {
            btn.style.display = 'block';
        });
    }
});

// Exportar funções para uso global
window.handleLogin = handleLogin;
window.handleRegister = handleRegister;
window.isLoggedIn = isLoggedIn;
window.getCurrentUser = getCurrentUser;
window.logout = logout;
window.showToast = showToast;