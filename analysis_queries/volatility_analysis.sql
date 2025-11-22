-- ==========================================
-- BUSINESS QUESTION 2:
-- Which stocks are most volatile? 
-- Risk analysis for investment decisions
-- ==========================================

WITH daily_returns AS (
    SELECT 
        ticker,
        date,
        close_price,
        LAG(close_price) OVER (PARTITION BY ticker ORDER BY date) as prev_close,
        ROUND(
            (close_price - LAG(close_price) OVER (PARTITION BY ticker ORDER BY date)) / 
            LAG(close_price) OVER (PARTITION BY ticker ORDER BY date) * 100, 
        2) as daily_return_pct
    FROM stock_prices 
)
SELECT 
    ticker,
    ROUND(AVG(daily_return_pct), 3) as avg_daily_return,
    ROUND(STDDEV(daily_return_pct), 3) as daily_volatility,
    ROUND(MIN(daily_return_pct), 2) as worst_day_pct,
    ROUND(MAX(daily_return_pct), 2) as best_day_pct,
    COUNT(*) as trading_days
FROM daily_returns 
WHERE daily_return_pct IS NOT NULL
GROUP BY ticker
ORDER BY daily_volatility DESC;