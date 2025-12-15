# 🔍 DEBUG DO CARRINHO - INSTRUÇÕES

## 🚨 Problema Reportado
**"Quando aperto em adicionar no carrinho não vai para o carrinho"**

## 🛠️ Correções Aplicadas

### 1. **Conflitos Removidos**
- ✅ Comentada função `addToCart()` antiga no `script.js`
- ✅ Comentada função `updateCartCount()` conflitante no `script.js`
- ✅ Comentada declaração de `cart` duplicada no `script.js`
- ✅ Adicionados logs de debug na função `addToCart()` do `index.html`

### 2. **Arquivos de Teste Criados**
- ✅ `test_cart.html` - Página de teste isolada do carrinho

## 🧪 Como Testar

### **Teste 1: Página de Teste Isolada**
1. Acesse: `http://localhost:3000/test_cart.html`
2. Clique em "Testar addToCart()"
3. Verifique se o contador aumenta
4. Clique em "Verificar localStorage"
5. Veja se os dados estão sendo salvos

### **Teste 2: Página Principal com Debug**
1. Acesse: `http://localhost:3000`
2. Abra o **Console do Navegador** (F12 → Console)
3. Clique em qualquer botão "Adicionar ao Carrinho"
4. Observe as mensagens de debug no console:
   ```
   🛒 addToCart chamada: {name: "...", price: ...}
   📦 Produto criado: {id: ..., name: "...", ...}
   ✅ Produto adicionado ao carrinho: {...}
   💾 Carrinho salvo: [...]
   🔢 Contador atualizado
   ```

### **Teste 3: Verificar localStorage**
1. No Console do Navegador, digite:
   ```javascript
   localStorage.getItem('cart')
   ```
2. Deve mostrar os produtos adicionados em formato JSON

### **Teste 4: Verificar Carrinho**
1. Acesse: `http://localhost:3000/purchase.html`
2. Veja se os produtos aparecem na página do carrinho

## 🔍 Possíveis Problemas e Soluções

### **Problema 1: Função não é chamada**
**Sintomas**: Nenhuma mensagem no console
**Causa**: Erro de JavaScript impedindo execução
**Solução**: Verificar erros no console (F12 → Console)

### **Problema 2: Função é chamada mas não salva**
**Sintomas**: Logs aparecem mas localStorage vazio
**Causa**: Erro na função `localStorage.setItem()`
**Solução**: Verificar permissões do navegador para localStorage

### **Problema 3: Salva mas contador não atualiza**
**Sintomas**: localStorage tem dados mas contador mostra 0
**Causa**: Função `updateCartCount()` não encontra elementos
**Solução**: Verificar se elementos `.cart-count` existem na página

### **Problema 4: Contador atualiza mas carrinho não mostra**
**Sintomas**: Contador correto mas purchase.html vazio
**Causa**: Diferentes chaves de localStorage ou formato incompatível
**Solução**: Verificar se purchase.html usa a mesma chave 'cart'

## 🔧 Comandos de Debug no Console

### **Verificar Carrinho**
```javascript
console.log('Carrinho atual:', JSON.parse(localStorage.getItem('cart') || '[]'));
```

### **Limpar Carrinho**
```javascript
localStorage.removeItem('cart');
console.log('Carrinho limpo');
```

### **Testar Função Manualmente**
```javascript
addToCart('Teste Manual', 99.90);
```

### **Verificar Elementos do Contador**
```javascript
console.log('Elementos cart-count:', document.querySelectorAll('.cart-count'));
```

## 📋 Checklist de Verificação

- [ ] Console não mostra erros JavaScript
- [ ] Função `addToCart()` é chamada (logs aparecem)
- [ ] Produto é criado corretamente
- [ ] localStorage é atualizado
- [ ] Contador do carrinho atualiza
- [ ] Notificação aparece na tela
- [ ] Produtos aparecem em purchase.html

## 🚀 Próximos Passos

1. **Execute os testes** na ordem sugerida
2. **Anote os resultados** de cada teste
3. **Copie as mensagens de erro** se houver
4. **Informe qual teste falhou** para diagnóstico específico

---

## 📞 Relatório de Teste

**Por favor, execute os testes e informe:**

1. ✅/❌ Teste 1 (test_cart.html) funcionou?
2. ✅/❌ Teste 2 (console logs) apareceram?
3. ✅/❌ Teste 3 (localStorage) tem dados?
4. ✅/❌ Teste 4 (purchase.html) mostra produtos?

**Mensagens de erro (se houver):**
```
[Cole aqui qualquer erro do console]
```