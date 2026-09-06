SELECT
    SUM(total_revenue)  AS total_revenue,
    SUM(qty_sold)        AS total_units_sold,
    ROUND(AVG(sold_price), 2) AS avg_selling_price
FROM sales;

-- 2. Revenue and units by zone, ranked
SELECT
    zone,
    SUM(total_revenue) AS zone_revenue,
    SUM(qty_sold)       AS zone_units,
    RANK() OVER (ORDER BY SUM(total_revenue) DESC) AS revenue_rank
FROM sales
GROUP BY zone
ORDER BY zone_revenue DESC;

-- 3. Top 5 best-selling car models by total units
SELECT
    cars,
    SUM(qty_sold) AS total_units
FROM sales
GROUP BY cars
ORDER BY total_units DESC
LIMIT 5;

-- 4. Monthly revenue trend (year-over-year comparable)
SELECT
    sale_year,
    month_num,
    sale_month,
    SUM(total_revenue) AS monthly_revenue
FROM sales
GROUP BY sale_year, month_num, sale_month
ORDER BY sale_year, month_num;

-- 5. Dealer performance leaderboard with running total (window function)
SELECT
    dealer,
    SUM(total_revenue) AS dealer_revenue,
    SUM(qty_sold)       AS dealer_units,
    SUM(SUM(total_revenue)) OVER (ORDER BY SUM(total_revenue) DESC) AS running_total_revenue
FROM sales
GROUP BY dealer
ORDER BY dealer_revenue DESC;

-- 6. Category-wise average net revenue after cost overhead
SELECT
    category,
    ROUND(AVG(net_revenue), 2) AS avg_net_revenue,
    ROUND(AVG(total_cost), 2)  AS avg_total_cost
FROM sales
GROUP BY category
ORDER BY avg_net_revenue DESC;

-- 7. Consumer profession segmentation: who buys the most premium cars?
SELECT
    consumer_profession,
    price_tier,
    COUNT(*) AS transactions,
    SUM(qty_sold) AS units_sold
FROM sales
GROUP BY consumer_profession, price_tier
ORDER BY consumer_profession, price_tier;

-- 8. State-level performance (top 10 states by revenue)
SELECT
    state,
    SUM(total_revenue) AS state_revenue,
    COUNT(*) AS transactions
FROM sales
GROUP BY state
ORDER BY state_revenue DESC
LIMIT 10;

-- 9. Above-average performing dealers (subquery / CTE)
WITH dealer_avg AS (
    SELECT dealer, SUM(total_revenue) AS revenue
    FROM sales
    GROUP BY dealer
)
SELECT dealer, revenue
FROM dealer_avg
WHERE revenue > (SELECT AVG(revenue) FROM dealer_avg)
ORDER BY revenue DESC;

-- 10. Brand loyalty check: % of customers open to other brands, by zone
SELECT
    zone,
    ROUND(100.0 * SUM(CASE WHEN other_brand_preferred = 'YES' THEN 1 ELSE 0 END)
          / COUNT(*), 1) AS pct_open_to_other_brands
FROM sales
GROUP BY zone
ORDER BY pct_open_to_other_brands DESC;
