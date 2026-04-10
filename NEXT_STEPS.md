# Next Steps

## 1. Clean up `schemas/food_item.py`

Remove the `FilterParams` class at the bottom of `app/schemas/food_item.py`.
It inherits from `FoodItemResponse` incorrectly and is not used anywhere.

---

## 2. Wire up the `User` entity

The `User` model already exists in `app/database/models.py` but has no supporting code.
Follow the exact same pattern used for `FoodItem`.

### 2a. Schemas — `app/schemas/user.py`
- `UserBase` — shared fields (`name`)
- `UserCreate(UserBase)` — used for POST body
- `UserResponse(UserBase)` — used for responses, must include `id` and `model_config = ConfigDict(from_attributes=True)`

### 2b. CRUD — `app/crud/user.py`
- `create_user(db, user)` — persist a new user
- `get_user_by_id(db, user_id)` — raise `HTTPException 404` if not found

### 2c. Routes — `app/api/routes/user.py`
- `POST /user/` — create a user, return `UserResponse`
- `GET /user/{user_id}` — get a user by id, return `UserResponse`
- Register the router in `app/main.py`

---

## 3. Link `FoodItem` to `User` (relational modeling)

Once `User` is fully wired, add the ownership relationship.

### 3a. Update the `FoodItem` model
- Add a `user_id` foreign key column pointing to `user.id`
- Add a SQLAlchemy `relationship()` on `User` back to `FoodItem`

> Since there are no migrations, you will need to delete `foodwaste.db` and let `create_all` rebuild it.

### 3b. Update schemas
- Add `user_id` to `FoodItemCreate` (required) and `FoodItemResponse`
- Decide: should `FoodItemUpdate` allow changing `user_id`? (probably not)

### 3c. Update CRUD
- `create_food_item` must now accept and store `user_id`
- `get_all_food_items` should accept an optional `user_id` filter to scope items per user

---

## Concepts you will practice

| Step | Concept |
|------|---------|
| 2a | Pydantic schema inheritance |
| 2b | SQLAlchemy session, HTTPException |
| 2c | APIRouter, Depends, response_model |
| 3a | ForeignKey, relationship() |
| 3b | Nested Pydantic models |
| 3c | Scoped queries with filters |
