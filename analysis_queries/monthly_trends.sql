-- ==========================================
-- BUSINESS QUESTION 4:
-- How do stocks perform by month?
-- Identify seasonal patterns
-- ==========================================

WITH monthly_returns AS (
    SELECT 
        ticker,
        DATE_TRUNC('month', date) as year_month,
        FIRST_VALUE(close_price) OVER w as month_start,
        LAST_VALUE(close_price) OVER w as month_end,
        (LAST_VALUE(close_price) OVER w - FIRST_VALUE(close_price) OVER w) / 
        FIRST_VALUE(close_price) OVER w * 100 as monthly_return_pct
    FROM stock_prices 
    WINDOW w AS (PARTITION BY ticker, DATE_TRUNC('month', date) ORDER BY date)
),
monthly_avg AS (
    SELECT 
        ticker,
        EXTRACT(MONTH FROM year_month) as month_num,
        TO_CHAR(year_month, 'Month') as month_name,
        AVG(monthly_return_pct) as avg_monthly_return
    FROM monthly_returns 
    GROUP BY ticker, year_month, month_num, month_name
)
SELECT 
    ticker,
    month_name,
    ROUND(AVG(avg_monthly_return), 2) as avg_return_pct,
    COUNT(*) as months_analyzed
FROM monthly_avg 
GROUP BY ticker, month_num, month_name
ORDER BY ticker, month_num;