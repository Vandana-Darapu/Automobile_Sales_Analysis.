import pandas as pd
import matplotlib.pyplot as plt
import os

CLEAN_PATH = os.path.join("..", "data", "Automobile_cleaned.csv")
OUT_DIR = os.path.join("..", "outputs")

plt.rcParams["figure.figsize"] = (9, 5)
plt.rcParams["axes.titlesize"] = 13
plt.rcParams["axes.titleweight"] = "bold"


def save_chart(fig, name):
    path = os.path.join(OUT_DIR, name)
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)
    print(f"Saved chart -> {path}")


def main():
    df = pd.read_csv(CLEAN_PATH, parse_dates=["date"])
    os.makedirs(OUT_DIR, exist_ok=True)

    print("=" * 60)
    print("BASIC STATS")
    print("=" * 60)
    print(df[["qty_sold", "sold_price", "total_revenue", "net_revenue"]].describe())

    total_revenue = df["total_revenue"].sum()
    total_units = df["qty_sold"].sum()
    print(f"\nTotal Revenue: ₹{total_revenue:,.0f}")
    print(f"Total Units Sold: {total_units:,.0f}")
    print(f"Average Selling Price: ₹{df['sold_price'].mean():,.0f}")

    # 1. Revenue by Zone
    rev_by_zone = df.groupby("zone")["total_revenue"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    rev_by_zone.plot(kind="bar", color="#4C72B0", ax=ax)
    ax.set_title("Total Revenue by Zone")
    ax.set_ylabel("Revenue (₹)")
    ax.set_xlabel("Zone")
    save_chart(fig, "01_revenue_by_zone.png")

    # 2. Units sold by car model (top 10)
    units_by_car = df.groupby("cars")["qty_sold"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots()
    units_by_car.plot(kind="barh", color="#55A868", ax=ax)
    ax.set_title("Total Units Sold by Car Model")
    ax.set_xlabel("Units Sold")
    ax.invert_yaxis()
    save_chart(fig, "02_units_by_car_model.png")

    # 3. Monthly sales trend
    monthly = df.groupby(df["date"].dt.to_period("M"))["total_revenue"].sum()
    fig, ax = plt.subplots()
    monthly.plot(kind="line", marker="o", color="#C44E52", ax=ax)
    ax.set_title("Monthly Revenue Trend")
    ax.set_ylabel("Revenue (₹)")
    ax.set_xlabel("Month")
    save_chart(fig, "03_monthly_revenue_trend.png")

    # 4. Revenue share by category
    rev_by_cat = df.groupby("category")["total_revenue"].sum()
    fig, ax = plt.subplots()
    ax.pie(rev_by_cat, labels=rev_by_cat.index, autopct="%1.1f%%", startangle=90)
    ax.set_title("Revenue Share by Category")
    save_chart(fig, "04_revenue_share_by_category.png")

    # 5. Dealer performance
    dealer_perf = df.groupby("dealer").agg(
        total_revenue=("total_revenue", "sum"),
        total_units=("qty_sold", "sum"),
    ).sort_values("total_revenue", ascending=False)
    fig, ax = plt.subplots()
    dealer_perf["total_revenue"].plot(kind="bar", color="#8172B2", ax=ax)
    ax.set_title("Total Revenue by Dealer")
    ax.set_ylabel("Revenue (₹)")
    save_chart(fig, "05_revenue_by_dealer.png")

    # 6. Price tier distribution
    tier_counts = df["price_tier"].value_counts()
    fig, ax = plt.subplots()
    tier_counts.plot(kind="bar", color="#CCB974", ax=ax)
    ax.set_title("Transactions by Price Tier")
    ax.set_ylabel("Number of Transactions")
    save_chart(fig, "06_price_tier_distribution.png")

    # 7. Consumer profession vs avg revenue
    prof_rev = df.groupby("consumer_profession")["total_revenue"].mean().sort_values(ascending=False)
    fig, ax = plt.subplots()
    prof_rev.plot(kind="bar", color="#64B5CD", ax=ax)
    ax.set_title("Average Revenue per Transaction by Consumer Profession")
    ax.set_ylabel("Avg Revenue (₹)")
    save_chart(fig, "07_avg_revenue_by_profession.png")

    # Save a summary table as CSV too (useful for the report / resume screenshot)
    summary = pd.DataFrame({
        "Total Revenue": [total_revenue],
        "Total Units Sold": [total_units],
        "Average Selling Price": [df["sold_price"].mean()],
        "Number of Transactions": [len(df)],
        "Number of Dealers": [df["dealer"].nunique()],
        "Number of Zones": [df["zone"].nunique()],
    })
    summary.to_csv(os.path.join(OUT_DIR, "summary_kpis.csv"), index=False)
    print(f"\nSaved KPI summary -> {os.path.join(OUT_DIR, 'summary_kpis.csv')}")

    print("\nEDA complete. Check the /outputs folder for all charts.")


if __name__ == "__main__":
    main()
