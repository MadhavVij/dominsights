# dominsights

A lightweight CLI + API microservice for ingesting and analyzing
Dominion Energy usage data using DuckDB.

------------------------------------------------------------------------

## Overview

`dominsights` is designed as:

- A standalone microservice
- CLI-first for ingestion and management
- FastAPI-based API for serving data
- DuckDB as the analytics engine
- Future-ready for Natural Language + LLM integration

The UI layer is intentionally lightweight and separate.

------------------------------------------------------------------------

## Architecture

CLI → Ingestion → DuckDB\
API → Reads from DuckDB → Returns JSON\
Future → NL endpoint + LLM hook

------------------------------------------------------------------------

## Tech Stack

- Python 3.12+
- DuckDB
- FastAPI
- Typer (CLI)
- dompower (Dominion Energy client)
- uv (package manager)

------------------------------------------------------------------------

## Installation

``` bash
git clone <your-repo>
cd dominsights

uv venv
source .venv/bin/activate

uv pip install -e .
```

------------------------------------------------------------------------

## Setup

Create `.env` file:

    ACCOUNT_NUMBER=your_account
    METER_NUMBER=your_meter
    TOKEN_FILE=tokens.json

Login once to generate tokens:

``` bash
dompower login --token-file tokens.json
```

Verify accounts:

``` bash
dompower --token-file tokens.json accounts --json
```

------------------------------------------------------------------------

## Initialize Database

``` bash
dominsights init
```

Creates DuckDB file and required tables.

------------------------------------------------------------------------

## Ingest Usage Data

``` bash
dominsights ingest --days 30
```

Pulls last N days of usage and stores in DuckDB.

------------------------------------------------------------------------

## Run API Server

``` bash
uvicorn dominsights.api.main:app --reload
```

API available at:

    http://127.0.0.1:8000

Example:

``` bash
curl http://127.0.0.1:8000/usage/daily
```

------------------------------------------------------------------------

## 📊 Example Output

``` json
[
  {"date": "2026-02-01", "kwh": 103.368},
  {"date": "2026-02-02", "kwh": 95.504}
]
```

------------------------------------------------------------------------

## Future Release (Planned)

- /nl/query endpoint
- LLM integration hook
- Cost analysis
- Anomaly detection
- Forecasting
- Minimal UI dashboard

Endpoints marked for future release will be tagged accordingly.

------------------------------------------------------------------------

## Project Structure

    dominsights/
        analytics/
            insights.py
            usage.py
        api/
            main.py
        auth/
            manager.py
        models/
            schemas.py
        services/
            ingestion.py
        storage/
            database.py
        cli.py
        config.py

------------------------------------------------------------------------

## Development Workflow

Initialize:

    dominsights init

Ingest:

    dominsights ingest --days 7

Run API:

    uvicorn dominsights.api.main:app --reload

------------------------------------------------------------------------

## Design Philosophy

- Keep ingestion separate from serving
- Keep UI separate from core service
- Keep database embedded and analytics-first
- Prepare for LLM expansion without coupling it to core logic

------------------------------------------------------------------------

## Database

DuckDB file: `dominsights.duckdb`

Designed for: - Fast aggregation - Columnar analytics - Zero external
dependencies
