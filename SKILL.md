---
name: genpark-personal-agent-longevity-biomarker-velocity-skill
version: "1.0.0"
description: "Zero-dependency Morgan Levine PhenoAge biological age acceleration estimator, aging velocity calculator, and actionable longevity intervention prioritization engine."
license: MIT
dependencies:
  - python>=3.10
  - mcp>=1.0.0
entrypoint: client.py
---

# Personal Agent Longevity Biomarker Velocity Skill

Designed for **OpenClaw**, **Hermes**, and autonomous personal AI agents to accurately calculate biological age (PhenoAge), quantify chronological vs. phenotypic drift, and prioritize targeted clinical and nutritional longevity protocols.

## Agent In-Context Capabilities

- **Levine PhenoAge Regression**: Implements the validated 9-biomarker Gompertz mortality hazard model without external statistical packages.
- **Aging Velocity Ratio**: Accurately tracks rate of biological aging (e.g., 0.85x for decelerated longevity vs. 1.25x for accelerated aging).
- **Clinical Intervention Prioritization**: Converts laboratory blood panels into a ranked, weighted matrix of actionable lifestyle, nutritional, and physical training protocols.

## Tools Summary

1. `calculate_phenotypic_age`: Computes PhenoAge, age delta, 10-year mortality hazard, and overall aging velocity ratio.
2. `prioritize_biomarker_interventions`: Ranks biomarker outliers against optimal longevity reference corridors.
