# RecoveryPilot AI Product Plan

## Product Positioning

RecoveryPilot AI is a professional assistant for asset recovery casework. It helps users structure facts, identify missing information, organize evidence, and produce clear recovery plans.

## MVP

The first version focuses on a reliable backend foundation:

- Case-oriented assistant state
- LangGraph workflow with deterministic nodes
- FastAPI chat endpoint
- Risk flags and next-action generation
- Tests and CI
- Documentation for future GitHub issues and milestones

## Target Users

The exact recovery domain is still open. The initial architecture supports:

- financial asset recovery
- crypto or digital asset recovery
- lost or stolen physical assets
- IT or disaster recovery assets
- legal or insurance recovery cases
- general recovery case management

## Guardrails

The assistant should:

- avoid pretending to provide legal or financial advice
- ask for missing information before making strong claims
- separate facts from assumptions
- preserve an auditable case trail
- cite retrieved sources when RAG is introduced
- route high-risk recommendations to human review in later milestones

## Milestones

### Milestone 1: Repository Foundation

- Initialize project as RecoveryPilot AI
- Add Python workspace
- Add CI
- Add GitHub templates
- Add documentation
- Add tested LangGraph skeleton

### Milestone 2: Case Management Core

- Define persistent case model
- Add assets, evidence, contacts, timeline, and action items
- Add storage layer
- Add case update tools

### Milestone 3: Retrieval-Augmented Guidance

- Add document ingestion
- Add pgvector or another production vector store
- Add cited answers
- Add retrieval evaluation tests

### Milestone 4: Product Interface

- Add web frontend
- Add authentication
- Add case dashboard
- Add document upload and generated reports

### Milestone 5: Production Readiness

- Add observability
- Add audit logs
- Add deployment configuration
- Add stronger security controls

