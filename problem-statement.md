# Problem Statement — Construction Cost Intelligence Pipeline
**Version 1.0 — April 2026**

---

## The Problem

Construction budgeting is inherently time-sensitive. Material costs — steel, copper, lumber, aluminum, cement, and glass — fluctuate continuously based on global commodity markets, supply chain disruptions, and macroeconomic conditions. The gap between when a budget is estimated and when materials are actually purchased can range from weeks to months.

Today, most construction professionals handle this in one of two ways: they inflate budgets with a contingency margin (making them less competitive), or they absorb the loss when prices move against them. Neither is a sustainable solution.

There is currently no tool that provides real-time tracking of construction-relevant commodity prices, cross-referenced with regional impact analysis and automated alerts — specifically designed for construction industry professionals.

---

## The Users

**Primary users** are construction cost managers, project managers, architects, and real estate developers who manage project budgets ranging from USD 100K to USD 10M+. These are professionals who make procurement and budgeting decisions regularly and need to know — before their client does — when a material cost is about to change significantly.

**Secondary users** include construction consultancies and quantity surveyors who manage multiple projects simultaneously and need portfolio-level visibility into cost exposure.

---

## The Value

When this pipeline is running, the user gains what we call a **"spider sense" for construction costs**: continuous, automated awareness of market movements that directly affect their projects — without manual monitoring.

### Quantified impact examples

| Event | Detail | Estimated Impact |
|---|---|---|
| Lumber volatility (2021) | 400% price increase over 6 months | USD 15,000–25,000 per residential project |
| Copper cycles | 20–30% swings every 18 months | USD 15,000 on a USD 500K project |
| Steel shock (2022) | 45% increase in 4 months | USD 18,000–36,000 per mid-size steel structure |

---

## What This Is Not

This system is **not** an architectural design tool, a construction management platform, a CRM, or a procurement system. It does not handle logistics, structural calculations, resource planning, or project scheduling.

The scope is strictly:

- Real-time tracking of international construction commodity prices
- Automated anomaly detection and alerting
- Regional impact analysis for the construction sector

---

## MVP Scope

### In scope

- Real-time price tracking for **6 commodities**: Steel, Copper, Lumber, Aluminum, Cement (via index), Glass
- Automated alerts on significant price movements (configurable thresholds)
- Dashboard with price evolution, trends, and commodity-specific construction insights
- Free tier with global commodity data

### Future tiers *(out of MVP scope)*

- Regional and city-level price adaptation
- ML-powered budget impact analysis from user-uploaded data
- Material quantity calculator integrated with commodity prices
- API access for third-party integrations