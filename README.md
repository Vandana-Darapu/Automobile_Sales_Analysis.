# 🚗 Automobile Sales Performance Analysis
### End-to-End Data Analytics Project | SQL + Python + Power BI

## Overview
This project analyzes 900 automobile dealership sales transactions across
6 zones, 4 dealers, 8 car models, and multiple consumer segments to uncover
revenue trends, top-performing dealers/regions, and customer buying patterns.
It's built as a complete, portfolio-ready analytics pipeline:

**Raw CSV → Python cleaning → SQL database & queries → Power BI dashboard**

## Business Questions Answered
- Which zones and dealers generate the most revenue?
- Which car models and categories sell the best?
- How does revenue trend month over month?
- What price tiers and professions drive the most transactions?
- Which dealers are performing above the network average?
- How brand-loyal are customers, and does this vary by region?

## Tech Stack
| Layer | Tool | What it does |
|---|---|---|
| Data Cleaning & EDA | Python (pandas, matplotlib) | Cleans raw data, engineers features, generates 7 charts + KPI summary |
| Data Storage & Querying | SQL (MySQL/PostgreSQL) | Schema design, aggregations, window functions, CTEs |
| Visualization | Power BI | Interactive 3-page dashboard with DAX measures |



## Key Findings
See `docs/key_findings.md` for the full write-up. Headline numbers:
- **Total Revenue:** ₹312.5 crore across 900 transactions
- **Total Units Sold:** 9,673
- **Top Zone:** West (₹117.2 crore — the single largest contributor)
- **Top Dealer:** Bulward, narrowly ahead of Nike and Autocat
