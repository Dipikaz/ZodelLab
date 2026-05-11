Zodel Lab is an AI-powered simulation platform that converts natural language engineering prompts into executable Python simulations with real-time visualization.

Phase 1 focuses on building a reliable “success path” pipeline:
Natural Language → Code Generation → Safe Execution → Visual Output

🚀 Overview

Zodel-Lab is the foundational engine of the Zodel system. It transforms user prompts into structured Python simulations using LLMs and renders results using interactive visualizations.

🛠 Tech Stack
LLM Orchestration: Gemini 2.0 Flash
Backend: FastAPI (Python 3.11)
Frontend: React.js + Plotly.js
Execution Layer: Secure subprocess-based Python execution
Data Format: JSON-based structured simulation output

This project prioritizes reliability, safety, and observability in AI-generated code execution.

1. Structured Code Generation
Enforces JSON-based output schemas
Ensures compatibility between backend execution and frontend visualization
2. Safe Execution Layer
Subprocess isolation for generated Python code
Timeout protection against infinite loops
Captures stdout/stderr for debugging and observability
3. Testing Strategy
Frontend: React Testing Library
Backend: Pytest + AsyncIO
Integration: End-to-end LLM → Execution → Visualization validation
Contract Testing: Ensures Plotly JSON schema compliance


📅 Roadmap
Phase 1: Natural Language → Executable Simulation (Current)
Phase 2: Multi-agent orchestration system
Phase 3: Self-healing execution + error correction loop
Phase 4: Scalable simulation engine for enterprise use cases
