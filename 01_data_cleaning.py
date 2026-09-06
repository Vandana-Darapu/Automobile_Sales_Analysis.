"""
==========================================================================
 AUTOMOBILE SALES ANALYSIS - STEP 1: DATA CLEANING
==========================================================================
Project   : Automobile Sales Performance Analysis (SQL + Python + Power BI)
Author    : <Your Name>
Purpose   : Load the raw dealership sales export, clean it, engineer a
            few useful columns, and save an analysis-ready CSV that is
            used by:
              - the Python EDA script (02_eda_analysis.py)
              - the SQL database load (sql/01_create_and_load.sql)
              - the Power BI dashboard (powerbi/Automobile_cleaned.csv)
==========================================================================
"""

import pandas as pd
import numpy as np
import os

RAW_PATH = os.path.join("..", "data", "Automobile_raw.csv")
CLEAN_PATH = os.path.join("..", "data", "Automobile_cleaned.csv")

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Loaded raw data: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names to snake_case for SQL / Python friendliness."""
    df = df.copy()
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Strip whitespace from all text/object columns
    text_cols = df.select_dtypes(include="object").columns
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip()

    # Standardize the zone column (some entries have inconsistent casing/spacing)
    df["zone"] = df["zone"].str.upper().str.replace(r"\s+", " ", regex=True)

    # Parse the date column (format like "19-Jan-19")
    df["date"] = pd.to_datetime(df["date"], format="%d-%b-%y", errors="coerce")
    df["year"] = df["date"].dt.year
    df["month_num"] = df["date"].dt.month

    # Drop exact duplicate rows if any
    before = len(df)
    df = df.drop_duplicates()
    print(f"Removed {before - len(df)} duplicate rows")

    # Drop rows with missing critical fields
    critical = ["qty_sold", "sold_price", "dealer", "zone", "date"]
    before = len(df)
    df = df.dropna(subset=critical)
    print(f"Removed {before - len(df)} rows with missing critical fields")

    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Total revenue per transaction line
    df["total_revenue"] = df["qty_sold"] * df["sold_price"]

    # Total cost burden per unit (insurance + tax) and total for the line
    df["total_cost_per_unit"] = df["car_insurance"] + df["state_tax"]
    df["total_cost"] = df["total_cost_per_unit"] * df["qty_sold"]

    # Net revenue after insurance/tax overhead
    df["net_revenue"] = df["total_revenue"] - df["total_cost"]

    # Simple price tier bucket for segmentation analysis
    df["price_tier"] = pd.cut(
        df["sold_price"],
        bins=[0, 250000, 400000, np.inf],
        labels=["Budget", "Mid-Range", "Premium"],
    )

    return df


def main():
    df = load_data(RAW_PATH)
    df = clean_columns(df)
    df = clean_data(df)
    df = engineer_features(df)

    df.to_csv(CLEAN_PATH, index=False)
    print(f"\nSaved cleaned dataset -> {CLEAN_PATH}")
    print(f"Final shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print("\nColumn overview:")
    print(df.dtypes)


if __name__ == "__main__":
    main()
