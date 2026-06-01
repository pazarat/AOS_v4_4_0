# Pazarat Project Entrypoint

This file is the compulsory entrypoint for any Pazarat-specific work inside the Mind_Ai executable tunnel agent.

The agent must not jump directly into Pazarat dashboards, web, mobile, implementation, UI, PRD, or module artifacts.

## Required Pazarat entry sequence

1. Read `01_PROJECT_CONTRACT.yaml`.
2. Read `02_PROJECT_TRUTH_INDEX.yaml`.
3. Enter `03_PROJECT_COGNITIVE_TUNNEL/_PROJECT_COGNITIVE_TUNNEL_GATE.yaml`.
4. Traverse the numbered files in `03_PROJECT_COGNITIVE_TUNNEL/` in numeric order as needed by task depth.
5. Only then enter `04_PROJECT_ARTIFACTS/` or implementation targets.

## Operating principle

The agent kernel decides how to execute.
The Pazarat project cognitive tunnel decides how Pazarat must be understood.
The Pazarat artifacts contain the actual project content.

No Pazarat-specific output is valid if it bypasses the project cognitive tunnel.
