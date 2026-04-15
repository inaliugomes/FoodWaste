# FoodWaste — Roadmap de Tarefas

## Backend (API)

### Crítico
- [ ] Adicionar `unique=True` ao campo `unique_Code` no modelo `User` (`models.py`)
- [ ] Criar função `update_user_by_id` no `crud/user.py` e rota `PUT /user/{user_id}`
- [ ] Adicionar CORS ao `main.py` (`CORSMiddleware`) — obrigatório para a interface web comunicar com a API
- [ ] Mover a URL da base de dados para variável de ambiente com `python-dotenv` (já instalado)

### Importante
- [ ] Substituir SQLite por PostgreSQL para suportar concorrência real
- [ ] Integrar Alembic para gestão de migrações de schema
- [ ] Adicionar autenticação JWT (`python-jose` + `passlib`) — proteger endpoints
- [ ] Fazer hash da password do User (quando autenticação for adicionada)
- [ ] Adicionar paginação ao `GET /user/` (igual ao `food_item` com `skip`/`limit`)

### Qualidade
- [ ] Escrever testes com `pytest` + `TestClient` para todos os endpoints
- [ ] Usar base de dados separada para testes (SQLite em memória)
- [ ] Corrigir `datetime.utcnow` → `datetime.now(timezone.utc)` no `models.py` (deprecated Python 3.12+)
- [ ] Simplificar `get_all_users` para evitar query dupla à DB

---

## Interface Web (Frontend)

### Tecnologia sugerida
React + Vite + TailwindCSS (leve, rápido de desenvolver, bom para dashboards)

### Estrutura de páginas
- [ ] **Dashboard** — visão geral: total de utilizadores, total de food items, itens por categoria
- [ ] **Página de Users** — listar, criar, eliminar utilizadores
- [ ] **Página de Food Items** — listar com filtros (nome, categoria, quantidade mínima), criar, editar, eliminar
- [ ] **Detalhe de User** — ver perfil e os food items associados

### Desenvolvimento frontend
- [ ] Criar projeto React com Vite dentro de `/frontend`
- [ ] Configurar cliente HTTP (axios ou fetch nativo)
- [ ] Criar serviços de API separados por entidade (`userService.js`, `foodItemService.js`)
- [ ] Adicionar formulários com validação para criar/editar entidades
- [ ] Adicionar feedback visual de erros da API (ex: "user has food items, cannot delete")
- [ ] Adicionar loading states nas chamadas à API

---

## Produção / Deploy

- [ ] Containerizar com Docker (Dockerfile para API + frontend)
- [ ] Criar `docker-compose.yml` com API + PostgreSQL + frontend
- [ ] Configurar variáveis de ambiente por ambiente (dev / prod)
- [ ] Adicionar logging estruturado na API
- [ ] Configurar HTTPS (via reverse proxy — nginx ou Caddy)

---

## Ordem sugerida

1. CORS → interface web consegue chamar a API -> Feito
2. `unique_Code` constraint + `update_user`
3. Variáveis de ambiente (`.env`)
4. Início do frontend (Dashboard + Food Items)
5. Autenticação (backend + frontend)
6. PostgreSQL + Alembic
7. Testes
8. Docker + Deploy
