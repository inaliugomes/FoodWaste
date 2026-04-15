# Teste de Conhecimento — FoodWaste API

Responde às perguntas sem consultar o código. No final compara com as respostas.

---

## Secção 1 — Arquitetura e Estrutura

**1.** Qual é a ordem correta do fluxo de um pedido HTTP neste projeto?

- a) model → crud → route → schema
- b) route → schema → model → crud
- c) route → crud → SQLAlchemy → SQLite
- d) crud → route → model → schema

--- B

**2.** Para que serve o ficheiro `app/database/base.py`?

--- Onde vamos criar o nosso base model , que vem de sqlalchemy y que vai permitir converter nossas classes depois
em tabelas de base de dados

**3.** O que acontece quando o servidor arranca e executa `Base.metadata.create_all(bind=engine)`?

- a) Apaga e recria todas as tabelas
- b) Cria as tabelas que ainda não existem, sem tocar nas existentes
- c) Executa as migrações pendentes do Alembic
- d) Valida se o schema da DB coincide com os modelos

--- B

**4.** Qual é a diferença entre um **schema Pydantic** e um **modelo SQLAlchemy**? Para que serve cada um?

--- Modelo Pydantic permite que fastapi saiba que tipo de dados esperar y que tipo de dados temos de passar api
--- Modelo SQLALCHEMY depois de receber os dados , sera ele que vai validar se esta tudo correcto antes de adicionar 
na base de dado , em realidad ambos devem ser simetricos 

## Secção 2 — FastAPI

**5.** O que faz o decorator `@router.get("/{user_id}", response_model=UserItemResponse)`?

--- Informa que o nosso endpoint sera de Get que deve ser pasado um user_id e que vai devolver os dados com o modelo UserItem

**6.** Qual é o problema com este código?

```python
@router.get("/{id}", response_model=UserItemResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(user_id, db)
```

--- O que estamos a passar como id no parametros da url nao corresponto com o que estamos receber na funcao e  ambos 
devem ser iguais

**7.** Para que serve `Depends(get_db)` nos parâmetros de uma route?

--- 

**8.** Qual é a diferença entre um **path parameter** e um **query parameter**? Dá um exemplo de cada um com base neste projeto.

---

**9.** O que significa `response_model` num router do FastAPI? O que acontece se o crud retornar mais campos do que os definidos no schema?

---

**10.** Num `GET /food_item/`, o parâmetro `food_quantity` filtra itens com quantidade:

- a) Igual ao valor indicado
- b) Menor ou igual ao valor indicado
- c) Maior ou igual ao valor indicado
- d) Diferente do valor indicado

---

## Secção 3 — Pydantic

**11.** Para que serve `model_config = ConfigDict(from_attributes=True)` num schema Pydantic?

---

**12.** Qual é a diferença entre `UserCreate` e `UserItemResponse` neste projeto?

---

**13.** O que faz `item.model_dump(exclude_unset=True)` e porque é importante num endpoint de `PUT`/`PATCH`?

---

**14.** O que acontece se enviares um `POST /user/` com `name = "Ana"` (3 caracteres)?

- a) O user é criado normalmente
- b) FastAPI retorna erro 422 antes de chegar ao crud
- c) O crud lança um HTTPException 400
- d) A base de dados rejeita o valor

---

## Secção 4 — SQLAlchemy e Base de Dados

**15.** O que é uma **Foreign Key**? Como está implementada neste projeto entre `FoodItem` e `User`?

---

**16.** O que é `back_populates` numa relação SQLAlchemy? O que acontece se não o definires?

---

**17.** Explica o erro abaixo com as tuas palavras:

```
sqlalchemy.exc.IntegrityError: NOT NULL constraint failed: food_item.user_id
[SQL: UPDATE food_item SET user_id=? WHERE food_item.id = ?]
[parameters: (None, 1)]
```

---

**18.** Porque é que não podes apagar um `User` que tem `FoodItems` associados (sem cascade)?

---

**19.** Qual é a diferença entre `cascade="all, delete-orphan"` e a solução que implementaste para o delete de user?

---

**20.** O que faz `db.refresh(obj)` após um `db.commit()`?

---

## Secção 5 — HTTP e REST

**21.** Associa o método HTTP ao seu uso correto neste projeto:

| Método | Uso |
|--------|-----|
| GET    | ? |
| POST   | ? |
| PUT    | ? |
| DELETE | ? |

---

**22.** Associa o status code ao seu significado:

| Status Code | Significado |
|-------------|-------------|
| 200 | ? |
| 201 | ? |
| 400 | ? |
| 404 | ? |
| 409 | ? |
| 422 | ? |

---

**23.** Porque usaste `status_code=409` em vez de `404` quando um user tem food items associados e não pode ser eliminado?

---

## Secção 6 — Conceitos de Produção

**24.** Porque é que o SQLite não é adequado para produção?

---

**25.** O que é o **Alembic** e porque é necessário se já temos `create_all`?

---

**26.** O que é **CORS** e porque é obrigatório ativar antes de ligar uma interface web à API?

---

**27.** O que é um **JWT** e para que serve no contexto de autenticação numa API REST?

---

---

# Respostas

## Secção 1
1. **c)**
2. Define a classe base `DeclarativeBase` que todos os modelos SQLAlchemy herdam — é o ponto de registo das tabelas.
3. **b)** — Só cria tabelas em falta, nunca altera estrutura existente. Por isso mudanças de schema requerem Alembic ou apagar a DB.
4. **Schema Pydantic** — valida e serializa dados de entrada/saída (requests e responses). Não sabe nada da DB. **Modelo SQLAlchemy** — representa uma tabela na DB e é usado para ler/escrever registos. Não valida requests.

## Secção 2
5. Define uma rota HTTP GET no path `/{user_id}`, extrai `user_id` como inteiro do URL, e garante que a resposta é serializada segundo o schema `UserItemResponse`.
6. O path param é `{id}` mas o parâmetro da função é `user_id`. FastAPI não os consegue associar — trata `user_id` como query param obrigatório e a rota falha.
7. É injeção de dependência — FastAPI chama `get_db()` automaticamente e injeta a sessão da DB na função. Garante que a sessão é aberta e fechada corretamente por request.
8. **Path param** — faz parte do URL: `/user/5` (o `5` é o id). **Query param** — vem após `?` no URL: `/food_item/?food_category=Verdura`.
9. FastAPI usa o schema para serializar a resposta e filtrar campos. Se o crud retornar mais campos do que o schema define, esses campos extras são ignorados e não aparecem na resposta.
10. **c)** — `FoodItem.quantity >= food_quantity`

## Secção 3
11. Permite que o Pydantic leia os dados de um objeto SQLAlchemy (ORM object) em vez de exigir um dicionário. Necessário em schemas de Response.
12. `UserCreate` só tem os campos que o utilizador envia (`name`, `unique_Code`). `UserItemResponse` inclui também `id` e `created_at`, gerados pela DB.
13. Converte só os campos que foram explicitamente enviados no request, ignorando os que ficaram com valor default. Essencial no PUT/PATCH para não sobrescrever campos com `None` acidentalmente.
14. **b)** — O Pydantic valida `min_length=4` antes de qualquer lógica. FastAPI retorna 422 Unprocessable Entity automaticamente.

## Secção 4
15. Uma Foreign Key é uma coluna que referencia a chave primária de outra tabela, criando uma ligação entre registos. Neste projeto: `FoodItem.user_id` referencia `User.id` — cada food item pertence a um user.
16. `back_populates` define a relação bidirecional — permite aceder a `user.foodItems` e a `food_item.user`. Sem ele a relação é só num sentido e o SQLAlchemy não sincroniza os dois lados automaticamente.
17. O SQLAlchemy tentou fazer UPDATE num `food_item` existente para definir `user_id = NULL`, mas a coluna tem `nullable=False`. Isto aconteceu porque ao apagar o `User`, o SQLAlchemy tentou "desligar" os food items associados antes de eliminar o registo pai.
18. Porque a FK `user_id` é `NOT NULL` — sem cascade, o SQLAlchemy tenta anular a FK nos filhos antes de apagar o pai, o que viola a constraint.
19. `cascade="all, delete-orphan"` apaga automaticamente os food items quando o user é eliminado. A solução implementada **impede** a eliminação se houver food items, forçando o utilizador a resolver a dependência manualmente — mais seguro para não perder dados acidentalmente.
20. Recarrega o objeto da DB, atualizando campos gerados automaticamente pela base de dados (ex: `id`, `created_at`) que só existem após o commit.

## Secção 5
21. GET = ler dados / POST = criar novo registo / PUT = atualizar registo existente / DELETE = eliminar registo
22. 200 = OK (sucesso) / 201 = Created (recurso criado) / 400 = Bad Request (erro do cliente) / 404 = Not Found / 409 = Conflict (conflito de estado) / 422 = Unprocessable Entity (validação falhou)
23. O recurso existe (o user foi encontrado) mas há um conflito de estado que impede a operação. O 404 seria errado porque significaria que o user não existe.

## Secção 6
24. SQLite não suporta múltiplas escritas simultâneas (bloqueia a DB inteira por write). Em produção com vários utilizadores em simultâneo causaria erros e lentidão.
25. Alembic gere versões do schema da DB com migrações. `create_all` só cria tabelas novas — se adicionares uma coluna a uma tabela existente, `create_all` não faz nada. Alembic aplica a alteração sem perder dados.
26. CORS (Cross-Origin Resource Sharing) é um mecanismo de segurança do browser que bloqueia pedidos de um domínio diferente do servidor. Se a interface web estiver em `localhost:3000` e a API em `localhost:8000`, o browser bloqueia as chamadas sem CORS configurado.
27. JWT (JSON Web Token) é um token assinado que o servidor emite após login. O cliente envia esse token em cada pedido subsequente para provar a sua identidade, sem o servidor precisar de guardar sessões.
