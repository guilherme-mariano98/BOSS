# Login and Registration Fix - TEST

## Summary

I've fixed the login and registration issues in the BOSS SHOPP application by:

1. **Updating the API endpoint** in `auth.js` from the Django backend (port 8000) to the Node.js backend (port 3000)
2. **Fixing the registration data format** to match the Node.js API requirements
3. **Simplifying error handling** to work with Node.js API responses
4. **Creating a batch file** (`start-node-server.bat`) to easily start the Node.js server
5. **Providing detailed documentation** (`FIX_LOGIN_REGISTER.md`) with instructions

## Files Modified

1. `frontend/auth.js` - Updated API endpoint and registration format
2. `frontend/start-node-server.bat` - Created batch file to start Node.js server
3. `FIX_LOGIN_REGISTER.md` - Created comprehensive fix documentation

## How to Test

1. Double-click on `start-node-server.bat` in the frontend folder
2. Wait for the server to start (should show "Server is running on all network interfaces")
3. Open your browser and go to `http://localhost:3000`
4. Click on "Entrar" in the top navigation bar
5. Test registration with a new email and password
6. Test login with the same credentials

## Expected Results

- Registration should succeed with message "Conta criada e login realizado com sucesso!"
- Login should succeed with message "Login realizado com sucesso!"
- After login, the "Entrar" button in the navigation bar should change to show your name
- You should be redirected to the homepage after successful login

## Troubleshooting

If you encounter issues:

1. **Port already in use**: Delete `database.db` file and restart server
2. **Module not found**: Run `npm install` in the frontend folder
3. **Server won't start**: Check that Node.js is installed on your system

The Node.js server requires these packages:
- express
- sqlite3
- cors
- bcryptjs
- jsonwebtoken

These will be automatically installed by the batch file if missing.