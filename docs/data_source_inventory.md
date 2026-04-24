# Data Source Inventory

**Project:** ConstructionMate — Construction Cost Intelligence Pipeline  
**Phase:** 1 — Data Discovery  
**Version:** 1.0 — April 2026  
**Status:** ✅ Complete

---

## Summary

| Source | Role | Streaming | Verdict |
|---|---|---|---|
| yfinance | Primary — real-time prices | ✅ Yes | ✅ Confirmed |
| FRED | Secondary — historical context | ❌ No | ✅ Confirmed |
| Alpha Vantage | — | ❌ No | ⚠️ Discarded |
| BLS | — | ❌ No | ⚠️ Discarded |

---

## 1. yfinance (Yahoo Finance)

**Role:** Primary source — real-time streaming  
**Verdict:** ✅ Confirmed

| Field | Detail |
|---|---|
| Update frequency | 1 minute (market hours only: 9:30–16:00 ET) |
| Serves for streaming | ✅ Yes |
| Free tier limit | No official limit (unofficial wrapper) |
| Format | Pandas DataFrame — OHLCV columns |
| Authentication | None — no API key required |
| Cost for more volume | Free — no paid tiers |

### Tickers

| Commodity | Ticker | Type | Exchange | Unit |
|---|---|---|---|---|
| Copper | `HG=F` | Futures (direct) | COMEX | USD/lb |
| Aluminum | `ALI=F` | Futures (direct) | COMEX | USD/lb |
| Lumber | `LBR=F` | Futures (direct) | CME | USD/MBF |
| Steel | `MT` | Equity proxy (ArcelorMittal) | NYSE | USD/share |
| Cement | `EXP` | Equity proxy (Eagle Materials) | NYSE | USD/share |
| Glass | `OC` | Equity proxy (Owens Corning) | NYSE | USD/share |

### Notes

- Copper, Aluminum, and Lumber have direct futures contracts available.
- Steel, Cement, and Glass have no free direct futures on Yahoo Finance. Equity proxies are used instead — leading companies whose stock prices correlate strongly with the underlying commodity price. This decision is documented explicitly in the README and reflected in the dashboard labeling.
- `LBS=F` (original Lumber ticker) is delisted. Replaced by `LBR=F`.
- Data flows only during US market hours. The pipeline is designed to handle this gap gracefully.

---

## 2. FRED (Federal Reserve Economic Data)

**Role:** Secondary source — historical context and official indices  
**Verdict:** ✅ Confirmed

| Field | Detail |
|---|---|
| Update frequency | Monthly (PPI series) / Quarterly (wage index) |
| Serves for streaming | ❌ No |
| Free tier limit | 100,000 results per request — practically unlimited |
| Format | JSON / XML |
| Authentication | Free API key (registration required at fred.stlouisfed.org) |
| Cost for more volume | Free — no paid tiers |

### Series IDs

| Commodity | Series ID | Full Name | Frequency |
|---|---|---|---|
| Copper | `WPUSI019011` | PPI: Special Indexes: Copper and Copper Products | Monthly |
| Aluminum | `PCU331315331315` | PPI by Industry: Aluminum Sheet, Plate, and Foil Manufacturing | Monthly |
| Lumber | `WPS081` | PPI by Commodity: Lumber and Wood Products: Lumber | Monthly |
| Steel | `WPU10170502` | PPI by Commodity: Metals: Steel Wire, Stainless Steel | Monthly |
| Cement | `PCU32733273` | PPI by Industry: Cement and Concrete Product Manufacturing | Monthly |
| Construction labor | `ECICONWAG` | Employment Cost Index: Wages and Salaries: Construction | Quarterly |

### Notes

- FRED data is used for historical benchmarking alongside real-time yfinance data. Example use case: "Is today's copper price historically high or low?"
- `ECICONWAG` tracks construction labour wages, not material costs. Included as a complementary cost indicator.
- PPI series may lag 4–6 weeks from the current date — this is expected behavior from the BLS publication schedule.

---

## 3. Alpha Vantage — Discarded

**Verdict:** ⚠️ Discarded — superseded by yfinance + FRED

| Field | Detail |
|---|---|
| Commodities available | Copper, Aluminum only (4 of 6 missing) |
| Update frequency | Monthly / Quarterly / Annual |
| Serves for streaming | ❌ No |
| Free tier limit | 25 requests/day |
| Format | JSON / CSV |
| Authentication | Free API key |

**Reason for discarding:** Only 2 of 6 required commodities available. Monthly frequency incompatible with streaming requirements. 25 requests/day limit too restrictive for a continuous pipeline. All relevant data is fully covered by yfinance (real-time) and FRED (historical).

---

## 4. BLS (Bureau of Labor Statistics) — Discarded

**Verdict:** ⚠️ Discarded — superseded by FRED

| Field | Detail |
|---|---|
| Update frequency | Monthly |
| Serves for streaming | ❌ No |
| Free tier limit | 500 requests/day |
| Format | JSON |
| Authentication | None (or free key) |

**Reason for discarding:** FRED re-publishes all relevant BLS PPI series directly through a better API with no practical rate limits. Maintaining a separate BLS integration adds complexity with no additional value.

---

## Architecture Decisions

### Decision 1 — Primary streaming source

| | |
|---|---|
| **Options considered** | Alpha Vantage, yfinance, Quandl, paid APIs (Bloomberg, Refinitiv) |
| **Decision** | yfinance |
| **Rationale** | Only option covering all 6 commodities at 1-minute frequency with no API key and no cost |
| **Trade-offs** | Unofficial wrapper — Yahoo may change the underlying API without notice. Acceptable risk for MVP. |

### Decision 2 — Steel, Cement, and Glass data

| | |
|---|---|
| **Options considered** | Direct commodity futures (unavailable for free), equity proxies, paid industrial APIs |
| **Decision** | Equity proxies: `MT` (Steel), `EXP` (Cement), `OC` (Glass) |
| **Rationale** | No free direct futures available. Leading sector companies show strong price correlation with the underlying commodity. |
| **Trade-offs** | Proxies reflect company performance, not purely commodity price. Labeled explicitly in dashboard and README. |

### Decision 3 — Historical context source

| | |
|---|---|
| **Options considered** | BLS direct API, Alpha Vantage, FRED |
| **Decision** | FRED |
| **Rationale** | Re-publishes all relevant BLS PPI series. Better API, no practical rate limits, free API key. |
| **Trade-offs** | Data lags 4–6 weeks. Monthly frequency only. Used purely for historical context, not streaming. |

---

*Next phase: [Architecture Design](architecture.md)*