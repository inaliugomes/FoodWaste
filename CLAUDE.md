# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

**Run the API server:**
```bash
uvicorn app.main:app --reload
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Quick DB inspection (ad-hoc script):**
```bash
python tests/basedados.py
```

Interactive API docs are available at `http://localhost:8000/docs` when the server is running.

## Architecture

This is a **FastAPI + SQLAlchemy + SQLite** REST API for tracking food items to reduce food waste.

**Layer structure (strict separation):**

- `app/main.py` — FastAPI app entry point; mounts routers and runs `Base.metadata.create_all` on startup (no migrations, schema is auto-created from models).
- `app/core/enums.py` — `FoodNameEnum` and `CategoryEnum` define the allowed food names and categories. Adding a new food or category means adding a value here first.
- `app/database/base.py` — `DeclarativeBase` used by all models.
- `app/database/connection.py` — SQLite engine + `SessionLocal` + `get_db()` dependency. DB file is `foodwaste.db` at the repo root.
- `app/database/models.py` — SQLAlchemy ORM models (`FoodItem`, `User`). `FoodItem` has a required FK to `User.id` via `user_id`. Deleting a `User` with associated `FoodItem`s is blocked (409).
- `app/schemas/` — Pydantic schemas for request/response validation. Each resource has its own file (`food_item.py`, `user.py`).
- `app/crud/` — All database operations per resource. Raises `HTTPException` directly on 404s/409s.
- `app/api/routes/` — Route handlers per resource. Delegates all logic to crud functions.

**Request flow:** Route handler → crud function → SQLAlchemy session → SQLite

**Resources:**

- `/food_item` — Full CRUD. `POST` requires a valid `user_id`. `GET /` supports `food_name`, `food_category`, and `food_quantity` (minimum quantity) query params, plus `skip`/`limit` pagination (max limit: 10).
- `/user` — Create, list all, get by ID, delete. `UserCreate` requires `name` (min 4 chars) and `unique_Code` (int ≥ 0). A user with associated food items cannot be deleted.

**No migration tool is used** — schema changes require either deleting `foodwaste.db` or manually altering the SQLite file, since `create_all` only creates missing tables.
