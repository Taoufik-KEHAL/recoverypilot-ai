# Contributing

RecoveryPilot AI uses a pull-request workflow. Work should be small, reviewable, and connected to an issue whenever possible.

## Branches

- `main` is stable.
- Use feature branches such as `feat/langgraph-core`, `docs/product-plan`, or `fix/chat-response`.
- Do not commit directly to `main`.

## Commits

Use conventional commits:

- `feat: add case intake node`
- `fix: handle empty assistant messages`
- `docs: describe recovery case model`
- `test: cover chat endpoint`

## Checks

Before opening a pull request, run:

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy apps/api/src packages/assistant_core/src
uv run pytest
```

## Pull Requests

Pull requests should include:

- a concise summary of the change
- a linked issue when one exists
- the checks that were run locally
- any user, data, or operational risk reviewers should consider

## Repository Automation

- CI runs on every pull request and every push to `main`.
- Dependabot opens scheduled dependency update pull requests.
- CODEOWNERS routes review requests for core project areas.
