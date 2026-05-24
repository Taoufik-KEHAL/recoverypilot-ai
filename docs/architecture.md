# Architecture

RecoveryPilot AI is organized as a backend-first monorepo.

```text
.
├── apps/
│   └── api/
├── packages/
│   └── assistant_core/
├── docs/
├── tests/
└── .github/
```

## Assistant Core

The assistant core owns the LangGraph state machine. It is intentionally independent from FastAPI so it can be tested, evaluated, and reused by future interfaces.

Initial graph:

```text
intake -> planner -> responder
```

The first graph is deterministic. Model-backed reasoning, tools, retrieval, and persistence will be added after the core state contract is stable.

## API

The API exposes operational endpoints:

- `GET /health`
- `POST /chat`

The chat endpoint accepts a user message and optional case state, then returns:

- assistant reply
- updated case state
- risk flags
- next actions

## Future Components

- PostgreSQL for application data
- pgvector for retrieval
- LangSmith or OpenTelemetry for tracing
- Web frontend for case workflows
- Human review queue for high-risk outputs

