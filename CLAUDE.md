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
- `app/database/models.py` — SQLAlchemy ORM models (`FoodItem`, `User`). Imports enums from `app.core.enums`.
- `app/schemas/food_item.py` — Pydantic schemas for request/response validation (`FoodItemCreate`, `FoodItemResponse`, `FoodItemUpdate`).
- `app/crud/food_item.py` — All database operations. Raises `HTTPException` directly on 404s.
- `app/api/routes/food_item.py` — Route handlers under `/food_item` prefix. Delegates all logic to crud functions.

**Request flow:** Route handler → crud function → SQLAlchemy session → SQLite

**Filtering:** `GET /food_item/` supports `food_name`, `food_category`, and `food_quantity` (minimum quantity) query params, plus `skip`/`limit` for pagination (max limit: 10).

**No migration tool is used** — schema changes require either deleting `foodwaste.db` or manually altering the SQLite file, since `create_all` only creates missing tables.
