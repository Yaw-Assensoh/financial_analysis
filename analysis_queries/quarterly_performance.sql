-- ==========================================
-- BUSINESS QUESTION 8:
-- Quarterly Performance Trends
-- Seasonal patterns and business cycle analysis
-- ==========================================

WITH quarterly_data AS (
    SELECT 
        ticker,
        EXTRACT(YEAR FROM date) as year,
        EXTRACT(QUARTER FROM date) as quarter,
        FIRST_VALUE(close_price) OVER w as quarter_start,
        LAST_VALUE(close_price) OVER w as quarter_end
    FROM stock_prices
    WINDOW w AS (PARTITION BY ticker, EXTRACT(YEAR FROM date), EXTRACT(QUARTER FROM date) ORDER BY date)
)
SELECT 
    ticker,
    year,
    quarter,
    ROUND(quarter_start, 2) as start_price,
    ROUND(quarter_end, 2) as end_price,
    ROUND((quarter_end - quarter_start) / quarter_start * 100, 2) as quarterly_return_pct
FROM quarterly_data
GROUP BY ticker, year, quarter, quarter_start, quarter_end
ORDER BY ticker, year, quarter;
