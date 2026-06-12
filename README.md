# DnD Companion — Backend

A small backend service for a Dungeons & Dragons companion app. It lets users create accounts, manage their characters, assign character classes, and attach spells to characters.

This project was built primarily as a portfolio piece to explore **Clean Architecture** and **CQRS** patterns in a Python/FastAPI codebase.

## Tech Stack

- **FastAPI** — HTTP layer / routing
- **mediatr** — CQRS-style request/handler dispatching (one Request + handler per use case)
- **dependency-injector** — dependency injection container for swapping infrastructure implementations (e.g. in tests)
- **SQLModel** + **SQLAlchemy (async)** — ORM and database access
- **PostgreSQL** — primary datastore
- **py-automapper** — mapping between persistence models (DTOs) and domain models
- **Docker / docker-compose** — local development environment
- **Render** — deployment target (see `render.yaml`)

## Architecture

The codebase follows a layered/Clean Architecture approach:

```
src/
├── app/                  # Presentation layer (FastAPI routes, request/response DTOs)
│   ├── character/        # API-level handlers (create, edit) wired into routes
│   ├── utils/             # DI container
│   └── run_api.py         # FastAPI app, routes, auth middleware
│
├── business/
│   └── domain/            # Application/domain layer
│       ├── character/         # Character domain model + use cases (CRUD, spell management)
│       ├── character_class/   # Character class domain model + use cases
│       ├── spell/              # Spell domain model + use cases
│       └── user/               # User use cases (create/delete account)
│
└── infrastructure/
    └── data/
        ├── DataService.py    # Async DB access (SQLModel/SQLAlchemy)
        └── dtos.py             # SQLModel table definitions + relationships
```

Each use case (e.g. `CreateCharacterRequest`, `ReadSpellRequest`) is a small, self-contained module with:
1. A **Request** class — the input data for the operation
2. A **handler** — the actual business logic, with infrastructure injected via `dependency_injector`
3. A **mediator wrapper** (`@Mediator.handler`) — registers the handler with `mediatr` so it can be dispatched from the API layer via `mediator.send_async(...)`

Domain models (`Character`, `Spell`, `CharacterClass`) are separate from the persistence models in `infrastructure/data/dtos.py`, and `automapper` is used to convert between them.

## Authentication

Authentication is intentionally minimal: a custom `X-DND-AUTH` header is used as a stand-in for a user/session token, checked by middleware in `run_api.py`. Only `/api/auth/*` routes are exempt. This is **not** production-grade auth — it's a placeholder to keep the focus on the architecture rather than auth implementation.

## API Overview

| Method | Path | Description |
|---|---|---|
| `POST` | `/api/auth/sign-up` | Create a new user, returns a token (`X-DND-AUTH` value) |
| `DELETE` | `/api/users/me` | Delete the current user |
| `GET` | `/api/characters/` | List the current user's characters |
| `POST` | `/api/characters/` | Create a character |
| `GET` | `/api/characters/{character_id}` | Get a character (with class & spells) |
| `PUT` | `/api/characters/` | Edit a character |
| `DELETE` | `/api/characters/{character_id}` | Delete a character |
| `GET` | `/api/character-classes/` | List available character classes |
| `GET` | `/api/spells/` | List all spells |
| `GET` | `/api/spells/{spell_id}` | Get a single spell |
| `POST` | `/api/characters/{character_id}/spells/{spell_id}` | Add a spell to a character |
| `DELETE` | `/api/characters/{character_id}/spells/{spell_id}` | Remove a spell from a character |

## Running Locally

### With Docker (recommended)

```bash
docker compose -f deploy/docker-compose.yml up --build
```

This starts the API on `http://localhost:8000` and a Postgres instance.

### Manually

```bash
pip install -r deploy/requirements.txt

export DB_URL=postgresql+psycopg://admin:123@localhost:5432/dnd_db

# create tables + seed sample data (Jaskier, Yennefer, etc.)
python -m src.infrastructure.data.dtos

uvicorn src.app.run_api:app --host 0.0.0.0 --port 8000 --reload
```

## Testing

A small set of end-to-end tests against the live deployment lives in `test_e2e/run.py`:

```bash
pytest test_e2e/run.py
```

Most of the CRUD/spell-management e2e tests are currently commented out and serve more as documented examples of expected request/response shapes.

## Known Limitations / Possible Improvements

This project is kept as-is for portfolio purposes, but a few things worth noting:

- **Auth** is a placeholder header, not a real auth flow (JWT, sessions, etc.)
- Several endpoints have `# TODO: check auth` — ownership checks on spell management aren't enforced
- No migration tooling (Alembic); schema is created via `SQLModel.metadata.create_all`
- `CharacterEditDto.user_id` is passed as a raw string from the header rather than cast to `UUID`, unlike `CharacterCreateDto`
- Most e2e tests are commented out / incomplete
- No automated unit test suite for the use-case layer

## License

No license specified — portfolio project, feel free to read through the code for reference.
