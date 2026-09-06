/* ==========================================================================
   AUTOMOBILE SALES ANALYSIS - SQL SCHEMA & DATA LOAD
   ==========================================================================
   Works on MySQL / PostgreSQL with minor tweaks (noted inline).
   Load the CLEANED file: data/Automobile_cleaned.csv
   ========================================================================== */

-- 1. Create database (MySQL syntax; for Postgres just `CREATE DATABASE ...;`
--    then connect to it before running the rest)
CREATE DATABASE IF NOT EXISTS automobile_sales;
USE automobile_sales;

-- 2. Create the main sales fact table
DROP TABLE IF EXISTS sales;
CREATE TABLE sales (
    id                      INT AUTO_INCREMENT PRIMARY KEY,   -- Postgres: SERIAL PRIMARY KEY
    series_model            VARCHAR(50),
    dealer                  VARCHAR(50),
    category                VARCHAR(50),
    cars                    VARCHAR(50),
    manager                 VARCHAR(50),
    zone                    VARCHAR(50),
    sale_date               DATE,
    sale_month              VARCHAR(10),
    state                   VARCHAR(10),
    city                    VARCHAR(50),
    qty_sold                INT,
    sold_price              DECIMAL(12,2),
    car_insurance           DECIMAL(12,2),
    state_tax               DECIMAL(12,2),
    consumer_family_status  VARCHAR(30),
    consumer_profession     VARCHAR(30),
    other_brand_preferred   VARCHAR(5),
    sale_year               INT,
    month_num               INT,
    total_revenue           DECIMAL(14,2),
    total_cost_per_unit     DECIMAL(12,2),
    total_cost              DECIMAL(14,2),
    net_revenue             DECIMAL(14,2),
    price_tier              VARCHAR(20)
);

-- 3. Bulk load the cleaned CSV
--    MySQL example (adjust path, and enable local_infile if needed):
LOAD DATA LOCAL INFILE '../data/Automobile_cleaned.csv'
INTO TABLE sales
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(series_model, dealer, category, cars, manager, zone, sale_date, sale_month,
 state, city, qty_sold, sold_price, car_insurance, state_tax,
 consumer_family_status, consumer_profession, other_brand_preferred,
 sale_year, month_num, total_revenue, total_cost_per_unit, total_cost,
 net_revenue, price_tier);

-- Postgres alternative:
-- \copy sales(series_model, dealer, category, cars, manager, zone, sale_date,
--   sale_month, state, city, qty_sold, sold_price, car_insurance, state_tax,
--   consumer_family_status, consumer_profession, other_brand_preferred,
--   sale_year, month_num, total_revenue, total_cost_per_unit, total_cost,
--   net_revenue, price_tier)
-- FROM '../data/Automobile_cleaned.csv' WITH (FORMAT csv, HEADER true);

-- 4. Quick sanity check
SELECT COUNT(*) AS total_rows FROM sales;
SELECT * FROM sales LIMIT 5;
