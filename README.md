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

## Project Structure
```
Automobile_Sales_Analysis/
├── data/
│   ├── Automobile_raw.csv          # Original uploaded dataset
│   └── Automobile_cleaned.csv      # Cleaned & feature-engineered dataset
├── python/
│   ├── 01_data_cleaning.py         # Cleaning, type-fixing, feature engineering
│   └── 02_eda_analysis.py          # EDA + chart generation
├── sql/
│   ├── 01_create_and_load.sql      # Table schema + data load
│   └── 02_analysis_queries.sql     # 10 business-question queries
├── powerbi/
│   ├── Automobile_cleaned.csv      # Data source for Power BI
│   └── PowerBI_Setup_Guide.md      # Step-by-step dashboard build guide + DAX
├── outputs/
│   ├── 01_revenue_by_zone.png
│   ├── 02_units_by_car_model.png
│   ├── 03_monthly_revenue_trend.png
│   ├── 04_revenue_share_by_category.png
│   ├── 05_revenue_by_dealer.png
│   ├── 06_price_tier_distribution.png
│   ├── 07_avg_revenue_by_profession.png
│   └── summary_kpis.csv
├── docs/
│   └── key_findings.md             # Written insights/report
├── requirements.txt
└── README.md
```

## How to Run
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the cleaning script
cd python
python 01_data_cleaning.py

# 3. Run EDA & generate charts
python 02_eda_analysis.py

# 4. Load into SQL (MySQL/PostgreSQL) and run analysis queries
#    See sql/01_create_and_load.sql and sql/02_analysis_queries.sql

# 5. Build the Power BI dashboard
#    See powerbi/PowerBI_Setup_Guide.md
```

## Key Findings
See `docs/key_findings.md` for the full write-up. Headline numbers:
- **Total Revenue:** ₹312.5 crore across 900 transactions
- **Total Units Sold:** 9,673
- **Top Zone:** West (₹117.2 crore — the single largest contributor)
- **Top Dealer:** Bulward, narrowly ahead of Nike and Autocat

## Resume Bullet Points (ready to use)
- Built an end-to-end sales analytics pipeline (Python, SQL, Power BI)
  analyzing 900+ automobile dealership transactions across 6 regional zones.
- Automated data cleaning and feature engineering in Python (pandas),
  reducing manual prep time and producing a reusable, analysis-ready dataset.
- Wrote 10+ SQL queries using window functions, CTEs, and subqueries to
  surface dealer performance, regional trends, and customer segmentation.
- Designed an interactive 3-page Power BI dashboard with custom DAX measures
  (YoY growth, revenue per unit, brand loyalty %) for executive reporting.

## Author
<Your Name> — Final Year B.Tech CSE (AI & ML), GITAM University
