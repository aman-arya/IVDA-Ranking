# IVDA Ranking Demo

This repository contains a minimal demonstration of a ranking application inspired by [RankASco](https://github.com/jenschmid/RankASco). It uses a modern stack consisting of **FastAPI** for the backend, **SQLite** as a relational database and a small **D3.js** front‑end.

## Running the demo

1. Install Python dependencies
   ```bash
   pip install -r backend/requirements.txt
   ```
2. Start the API server
   ```bash
   uvicorn backend.main:app --reload
   ```
3. Open `http://localhost:8000/static/index.html` in your browser to see the ranking visualization.

Weights and items can be modified via the API:
- `GET /items` – list items sorted by score
- `POST /items` – add a new item
- `GET /weights` – current attribute weights
- `POST /weights` – update weights

The front‑end fetches `/items` and draws a simple bar chart using D3.
