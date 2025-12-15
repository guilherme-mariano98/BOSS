# Fix for Login and Registration Issues

## Problem Analysis

The BOSS SHOPP application has two different backend systems:
1. **Django Backend** (runs on port 8000) - Not working or not accessible
2. **Node.js Backend** (runs on port 3000) - Working with SQLite database

The authentication system in `auth.js` was configured to connect to the Django backend, causing login and registration failures.

## Solution Implemented

### 1. Updated API Endpoint
Changed the API base URL in `auth.js` from Django to Node.js backend:
```javascript
// Before
const API_BASE_URL = 'http://localhost:8000/api';

// After  
const API_BASE_URL = 'http://localhost:3000/api';
```

### 2. Fixed Registration Data Format
Updated the registration function to match the Node.js API format:
```javascript
// Before
const userData = {
    username: formData.get('email'), // Django requires username
    email: formData.get('email'),
    password: formData.get('password'),
    first_name: formData.get('firstName'),
    last_name: formData.get('lastName')
};

// After
const userData = {
    name: formData.get('firstName') + ' ' + formData.get('lastName'),
    email: formData.get('email'),
    password: formData.get('password')
};
```

### 3. Updated Error Handling
Modified error handling to work with Node.js API responses:
```javascript
// Simplified error handling for Node.js API
let errorMessage = 'Erro ao criar conta. Tente novamente.';
if (data.error) {
    errorMessage = data.error;
    // Translate common error messages
    if (errorMessage === 'User already exists') {
        errorMessage = 'Este email já está registrado.';
    }
}
```

## How to Run the Fixed System

### Option 1: Using the Batch File (Recommended)
1. Double-click on `start-node-server.bat` in the frontend folder
2. The server will automatically install required packages if needed
3. The server will start on `http://localhost:3000`

### Option 2: Manual Start
1. Open Command Prompt or PowerShell
2. Navigate to the frontend folder:
   ```
   cd c:\Users\guilh\OneDrive - SENAC DF\boss-shop2-master\boss-shop2-master\BOSS-SHOP1\frontend
   ```
3. Install required packages:
   ```
   npm install express sqlite3 cors bcryptjs jsonwebtoken
   ```
4. Start the server:
   ```
   node server.js
   ```

## Accessing the Application

After starting the server:
1. Open your browser
2. Go to `http://localhost:3000`
3. Click on "Entrar" to access the login/registration page

## Testing the Fix

### Registration Test
1. Click "Cadastre-se"
2. Fill in the registration form:
   - Nome: João
   - Sobrenome: Silva
   - Email: joao@teste.com
   - Telefone: (11) 99999-9999
   - Senha: senha123
   - Confirmar Senha: senha123
3. Check "Aceito os Termos de Uso"
4. Click "Criar Conta"

### Login Test
1. Click "Faça login" to switch to login form
2. Enter:
   - Email: joao@teste.com
   - Senha: senha123
3. Click "Entrar"

## Database Information

The Node.js backend uses SQLite database (`database.db`) which is automatically created and populated with:
- Users table (with enhanced customer information)
- Products table (with sample products)
- Orders and order_items tables
- Password reset tokens table

## Troubleshooting

### If you get "Port already in use" error:
1. Find the process using port 3000:
   ```
   netstat -ano | findstr :3000
   ```
2. Kill the process:
   ```
   taskkill /PID <process_id> /F
   ```

### If registration says "User already exists":
1. Delete the `database.db` file in the frontend folder
2. Restart the server
3. Try registering again

### If you see "Module not found" errors:
1. Make sure Node.js is installed
2. Run `npm install` in the frontend folder
3. Make sure all required packages are installed:
   ```
   npm install express sqlite3 cors bcryptjs jsonwebtoken
   ```

## Security Notes

This is a development setup:
- Uses SQLite database (not suitable for production)
- Stores passwords securely with bcrypt encryption
- Uses JWT tokens for authentication
- No HTTPS encryption (HTTP only)

For production deployment, you would need:
- Proper database (PostgreSQL, MySQL)
- HTTPS certificates
- Environment variable management
- Proper error logging
- Security headers and CORS configuration