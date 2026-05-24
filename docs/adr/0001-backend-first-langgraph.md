# ADR 0001: Backend-First LangGraph Foundation

## Status

Accepted

## Context

RecoveryPilot AI needs a reliable assistant workflow before investing in a broader product interface. Asset recovery casework can involve sensitive, high-risk information, so the graph state and behavior should be testable before model-backed complexity is introduced.

## Decision

Start with a backend-first architecture:

- LangGraph for workflow orchestration
- LangChain Core message types for assistant state
- FastAPI for HTTP access
- deterministic graph nodes for the first milestone
- tests and CI from the beginning

## Consequences

This keeps the first milestone reviewable and avoids coupling the assistant logic to a specific frontend. It also gives the project a clean path to add persistence, retrieval, model providers, and human review later.

