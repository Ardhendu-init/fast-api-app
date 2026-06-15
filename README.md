# FastAPI User Registration API

## Setup

```bash
cp .env.example .env
# Add your MongoDB Atlas connection string to .env
```

```bash
uv sync
uv run fastapi dev app/main.py
```

API runs at `http://127.0.0.1:8000` — docs at `/docs`

## Endpoint

`POST /users`
