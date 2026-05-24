# RecoveryPilot AI

RecoveryPilot AI is a LangGraph and LangChain assistant for structured asset recovery casework. The product is designed as a professional, case-oriented assistant that helps collect facts, identify gaps, organize evidence, generate next steps, and preserve an auditable recovery plan.

The first milestone is backend-first: a typed LangGraph core, a FastAPI API surface, tests, CI, and documentation that make future product work easy to review through GitHub pull requests.

## Current Status

This repository contains the initial professional foundation:

- LangGraph assistant core in `packages/assistant_core`
- FastAPI application in `apps/api`
- GitHub issue and pull request templates
- GitHub Actions CI for formatting, linting, type checking, and tests
- Product, architecture, and ADR documentation

## Tech Stack

- Python 3.11+
- LangGraph
- LangChain Core
- FastAPI
- Pydantic
- uv
- Ruff
- mypy
- pytest

## Local Development

Install dependencies:

```bash
uv sync --all-packages --group dev
```

Run tests:

```bash
uv run pytest
```

Run quality checks:

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy apps/api/src packages/assistant_core/src
```

Start the API:

```bash
uv run uvicorn recoverypilot_api.main:app --app-dir apps/api/src --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

## Example Request

```bash
curl -X POST http://127.0.0.1:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"I need help recovering access to a digital asset account."}'
```

## GitHub Workflow

RecoveryPilot AI uses a professional GitHub workflow:

- `main` is the stable branch
- feature branches for all work
- pull requests for every change
- GitHub Issues and Milestones for planning
- GitHub Actions for CI
- conventional commits
- no direct commits to `main`

