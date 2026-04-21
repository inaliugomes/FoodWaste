# Frontend — Plano de Implementação (Aprendizagem)

## Estado actual do código
- `Navbar.jsx` — existe, estrutura correcta, mas importa `Navbar.css` que não existe
- `layout.jsx` — ficheiro vazio
- `FoodItems.jsx` — existe, mas importa `FoodItemCard` que não existe
- `FoodItems.css` — existe com grid básico
- `foodItemService.js` — correto, chama `GET /food_item`
- `userService.js` — vazio
- `App.jsx` — não está ligado a nada, renderiza `<p>Inicial</p>`

## O que já sabes
JSX · useState · useEffect · Props · Destructuring

---

## Fase 1 — HTML: estrutura antes de qualquer estilo

> Regra: primeiro faz funcionar. Só depois faz parecer bem.
> Nesta fase usas apenas HTML semântico dentro do JSX. Zero CSS.

---

### 1.1 — Completar `layout.jsx`

**O que implementar:**
Um componente que envolve todas as páginas — recebe `children` como prop e renderiza
a `Navbar` em cima, o conteúdo da página em baixo.

**O que precisas de saber:**
- A prop especial `children` — qualquer componente pode receber o conteúdo que está
  entre as suas tags de abertura e fecho, como se fosse um slot.
  `<Layout><FoodItems /></Layout>` → `Layout` recebe `FoodItems` como `children`.

**HTML que usas:** `<header>`, `<main>`, e a `<Navbar />` que já existe.

---

### 1.2 — Criar `FoodItemCard.jsx`

**O que implementar:**
Um componente que recebe um food item por prop e renderiza os seus dados:
nome, quantidade, peso, categoria, data de criação.

**O que precisas de saber:**
- Destructuring de props — em vez de `props.item.name`, podes escrever
  `const { name, quantity, weight_in_grams, category, created_at } = item`
- Como formatar uma data ISO string para o utilizador ver algo legível
  (`new Date(created_at).toLocaleDateString()`)

**HTML que usas:** `<article>` ou `<div>`, `<h3>`, `<p>`, `<span>`.

---

### 1.3 — Ligar `App.jsx` com `Layout` e `FoodItems`

**O que implementar:**
`App.jsx` deve usar `Layout` a envolver `FoodItems`, para verificares
que a estrutura toda está a funcionar antes de adicionar routing.

**O que precisas de saber:**
- Composição de componentes — não há nada novo aqui além de perceber
  que `<Layout>` envolve `<FoodItems />` como se fosse HTML normal.

**Resultado esperado:** corres a app e vês a Navbar + lista de food items.

---

### 1.4 — Criar `UserCard.jsx`

**O que implementar:**
Igual ao `FoodItemCard` mas para utilizadores. Recebe um user por prop
e mostra `name` e `unique_Code`.

**O que precisas de saber:** o mesmo que no 1.2. Treino puro de props + destructuring.

---

### 1.5 — Criar `FoodItemForm.jsx` (só estrutura HTML)

**O que implementar:**
Um formulário com campos para: nome (select), quantidade (number),
peso (number), categoria (select), user_id (number).
Ainda não precisa de funcionar — só o HTML correcto.

**O que precisas de saber:**
- Formulários HTML semânticos: `<form>`, `<label>`, `<input>`, `<select>`, `<option>`, `<button type="submit">`
- Cada `<label>` deve ter `htmlFor` (em JSX, não `for`) ligado ao `id` do input — acessibilidade básica.
- Os valores de `<select>` para nome e categoria vêm dos enums da API:
  tens de hardcodar as opções por agora (depois melhorarás).

---

### 1.6 — Criar `UserForm.jsx` (só estrutura HTML)

**O que implementar:**
Formulário com dois campos: `name` (text) e `unique_Code` (number).

**O que precisas de saber:** o mesmo que 1.5. É mais simples.

---

## Fase 2 — React: comportamento e dados

> Aqui é onde o HTML ganha vida. Cada passo ensina um conceito novo.

---

### 2.1 — Formulários controlados no `FoodItemForm`

**O que implementar:**
Ligar cada campo do formulário ao estado com `useState`.
Quando o utilizador escreve, o estado actualiza. Quando faz submit,
os dados do estado são enviados à API.

**O que precisas de saber:**
- **Formulário controlado** — o input não tem valor próprio, tens tu que
  guardar o valor no estado e passá-lo de volta via `value`. O ciclo é:
  utilizador escreve → `onChange` dispara → `setState` actualiza → React re-renderiza o input com o novo valor.
- `event.preventDefault()` no `onSubmit` — impede a página de recarregar (comportamento padrão dos forms HTML).
- Um único `useState` para um objecto com todos os campos é mais limpo do
  que um `useState` por campo — mas ambos funcionam.

---

### 2.2 — Estados de loading e erro nas chamadas à API

**O que implementar:**
Em `FoodItems.jsx`, adicionar dois estados: `loading` (boolean) e `error` (string | null).
Enquanto carrega, mostras "A carregar...". Se falhar, mostras a mensagem de erro.

**O que precisas de saber:**
- **Renderização condicional** — `if (loading) return <p>A carregar...</p>` ou
  com operador ternário inline: `{loading ? <p>...</p> : <div>...lista...</div>}`
- **Estrutura de um useEffect com async/await** — não podes marcar o useEffect
  como `async` directamente, mas podes definir uma função `async` dentro dele e chamá-la.
- O bloco `try / catch / finally` — `finally` é onde defines `loading = false`
  independentemente de ter falhado ou não.

---

### 2.3 — React Router DOM

**O que implementar:**
Substituir a estrutura estática do `App.jsx` por rotas:
- `/` → Dashboard (por agora pode ser uma página vazia)
- `/food-items` → FoodItems
- `/users` → Users

Actualizar os `<a href>` da Navbar para usar `<Link>` do React Router.

**O que precisas de saber:**
- **Por que não usar `<a href>` normais?** — Fazem reload completo da página.
  O React Router intercela a navegação e actualiza apenas o componente,
  sem recarregar — isso chama-se SPA (Single Page Application).
- **3 peças fundamentais:**
  - `BrowserRouter` — envolve toda a app (vai em `main.jsx`)
  - `Routes` + `Route` — definem qual componente renderizar para cada path (vai em `App.jsx`)
  - `Link` — substitui o `<a>` sem fazer reload (vai na `Navbar`)
- `useNavigate` — hook para navegar programaticamente (ex: após submeter um form, redireccionas para `/food-items`)

---

### 2.4 — Criar página `Users.jsx`

**O que implementar:**
Página que lista todos os utilizadores. Igual ao `FoodItems.jsx` mas
para users, usando o `userService.js` (que ainda está vazio — tens de completá-lo).

**O que precisas de saber:**
- Não há nada novo aqui — é repetição deliberada de `useEffect` + `useState` + loading/error.
  Repetir consolida o padrão.
- Completar `userService.js`: adicionar `getAllUsers()` que chama `GET /user/`.

---

### 2.5 — Criar e eliminar food items

**O que implementar:**
- O form de criação de food item envia os dados à API (`POST /food_item`)
- Após criar com sucesso, a lista actualiza automaticamente
- Cada card tem um botão "Eliminar" que chama `DELETE /food_item/{id}`

**O que precisas de saber:**
- **Lifting state up** — conceito chave. Se a lista e o formulário estão
  em componentes separados mas precisam de partilhar o estado (criar um item
  actualiza a lista), o estado tem de subir para o componente pai comum.
  O pai passa a lista como prop ao componente de lista, e passa a função
  de actualização como prop ao formulário.
- **Actualizar o estado após mutação** — duas abordagens:
  1. Após criar/eliminar, chamar `getAllFoodItems()` de novo (mais simples, menos eficiente)
  2. Actualizar o array em memória sem chamar a API (mais rápido, mais complexo)
  Começa pela abordagem 1.

---

### 2.6 — Criar página `Dashboard.jsx`

**O que implementar:**
Página com estatísticas simples: total de food items, total de utilizadores,
itens agrupados por categoria.

**O que precisas de saber:**
- **Derivar dados do estado** — não precisas de novo `useState` para as
  estatísticas. Se já tens o array de items no estado, calculas `items.length`,
  e usas `.filter()` ou `.reduce()` para agrupar por categoria.
  Valores derivados do estado não são estado — são cálculos que acontecem durante o render.
- Fazer múltiplas chamadas à API em paralelo com `Promise.all` dentro de um `useEffect`.

---

## Fase 3 — Tailwind CSS

> Só entras aqui depois da Fase 2 estar funcional.
> Tailwind é aplicado por cima — não muda a lógica, só os nomes das classes.

---

### 3.1 — Instalar e configurar Tailwind

**O que implementar:**
Instalar `tailwindcss` via npm, criar `tailwind.config.js`,
importar as directivas no ficheiro CSS principal.

**O que precisas de saber:**
- Tailwind não é um framework de componentes (não é Bootstrap).
  É uma biblioteca de **utility classes** — cada classe faz uma coisa só
  (`p-4` = padding de 1rem, `text-white` = cor branca, `flex` = display flex).
- O ficheiro `tailwind.config.js` tem um campo `content` — tens de apontar
  para todos os teus ficheiros JSX para o Tailwind saber quais classes incluir no build.

---

### 3.2 — Migrar os componentes existentes para Tailwind

**O que implementar:**
Apagar os ficheiros `.css` e substituir as classes CSS por classes Tailwind
em cada componente.

**O que precisas de saber:**
- A ordem de migração sugerida: `Navbar` → `Layout` → `FoodItemCard` → `UserCard` → páginas → forms.
- Em JSX, as classes vão no atributo `className` (não `class`).
- Para classes condicionais (ex: botão activo vs inactivo), usas template literals
  ou a biblioteca `clsx` (aprenderás quando precisares).

---

## Progresso

### Fase 1 — HTML
- [x] 1.1 — Completar `layout.jsx`
- [x] 1.2 — Criar `FoodItemCard.jsx`
- [x] 1.3 — Ligar `App.jsx`
- [x] 1.4 — Criar `UserCard.jsx`
- [x] 1.5 — Criar `FoodItemForm.jsx` (HTML)
- [x] 1.6 — Criar `UserForm.jsx` (HTML)

### Fase 2 — React
- [ ] 2.1 — Formulários controlados
- [ ] 2.2 — Loading e erro (estados loading/error já implementados em FoodItems.jsx — rever conceitos)
- [ ] 2.3 — React Router DOM
- [ ] 2.4 — Página Users
- [ ] 2.5 — Criar e eliminar items
- [ ] 2.6 — Dashboard

### Fase 3 — Tailwind
- [ ] 3.1 — Instalar e configurar
- [ ] 3.2 — Migrar componentes

---

## Notas de sessão (2026-04-21)

- `FoodItems.jsx` criado em `pages/` — fetch funcional com `useEffect` + `useState`
- A API devolve `{ total, items: [...] }` — os dados estão em `response.data.items`, não `response.data`
- `Navbar.jsx` criado de raiz (estava vazio)
- `layout.jsx` completo — recebe `children`, renderiza `NavBar` + `main`
- `FoodItemCard.jsx` completo — destructuring de props, `new Date().toLocaleDateString()` para a data
- Próximo passo: `UserCard.jsx` (1.4) e depois `UserForm.jsx` (1.6)
