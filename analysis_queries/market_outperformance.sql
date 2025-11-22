-- ==========================================
-- BUSINESS QUESTION 1: 
-- Which stocks outperformed the market (SPY)?
-- ==========================================

WITH stock_performance AS (
    SELECT 
        ticker,
        MIN(close_price) as start_price,
        MAX(close_price) as end_price,
        (MAX(close_price) - MIN(close_price)) / MIN(close_price) * 100 as total_return_pct
    FROM stock_prices 
    GROUP BY ticker
)
SELECT 
    ticker,
    ROUND(total_return_pct, 2) as total_return_percentage,
    CASE 
        WHEN ticker = 'SPY' THEN 'BENCHMARK'
        WHEN total_return_pct > (SELECT total_return_pct FROM stock_performance WHERE ticker = 'SPY') 
        THEN 'OUTPERFORMED'
        ELSE 'UNDERPERFORMED'
    END as vs_market
FROM stock_performance 
ORDER BY total_return_pct DESC;