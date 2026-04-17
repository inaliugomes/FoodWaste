# Frontend — Plano de Implementação

## Tecnologias
- React + Vite (já criado em `frontend/foodwastefront/`)
- HTML/CSS puro primeiro → Tailwind depois
- Axios para chamadas à API
- React Router DOM para navegação

---

## Ordem de implementação

1. Instalar dependências: `axios` e `react-router-dom`
2. Limpar `App.jsx` e `App.css` — remover tudo do default Vite
3. Criar estrutura de pastas em `src/`
4. Criar os serviços de API (`userService.js`, `foodItemService.js`)
5. Criar componentes base: `Navbar`, `Layout`
6. Criar página **Dashboard** (estático primeiro, depois ligar à API)
7. Criar página **Food Items** (listagem com filtros)
8. Criar página **Users** (listar, criar, eliminar)
9. Configurar rotas no `App.jsx`

---

## Estrutura de pastas (`src/`)

```
src/
├── services/
│   ├── userService.js
│   └── foodItemService.js
├── pages/
│   ├── Dashboard.jsx
│   ├── FoodItems.jsx
│   └── Users.jsx
└── components/
    ├── Navbar.jsx
    ├── FoodItemCard.jsx
    ├── FoodItemForm.jsx
    ├── UserCard.jsx
    └── UserForm.jsx
```

---

## Componentes — propósito

| Componente       | Propósito                                              |
|------------------|--------------------------------------------------------|
| `Navbar`         | Navegação entre páginas                                |
| `FoodItemCard`   | Renderizar um food item individual na lista            |
| `FoodItemForm`   | Formulário de criar/editar food item                   |
| `UserCard`       | Renderizar um utilizador na lista                      |
| `UserForm`       | Formulário de criar utilizador                         |

---

## Axios vs Fetch — decisão

**Usar axios.**
Com `fetch` nativo, erros HTTP (404, 500) não lançam exceção — tens de verificar `response.ok` manualmente.
Com `axios`, qualquer status ≥ 400 lança erro automaticamente, o que é mais natural para uma API REST.

---

## Progresso

- [ ] Passo 1 — Instalar axios + react-router-dom
- [ ] Passo 2 — Limpar App.jsx e App.css
- [ ] Passo 3 — Criar estrutura de pastas
- [ ] Passo 4 — Criar serviços de API
- [ ] Passo 5 — Navbar + Layout
- [ ] Passo 6 — Página Dashboard
- [ ] Passo 7 — Página Food Items
- [ ] Passo 8 — Página Users
- [ ] Passo 9 — Configurar rotas
