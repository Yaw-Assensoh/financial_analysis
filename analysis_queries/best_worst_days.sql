-- ==========================================
-- BUSINESS QUESTION 7:
-- Best & Worst Performing Days for Each Stock
-- ==========================================

WITH daily_changes AS (
    SELECT 
        ticker,
        date,
        close_price,
        LAG(close_price) OVER (PARTITION BY ticker ORDER BY date) as prev_close,
        ROUND((close_price - LAG(close_price) OVER (PARTITION BY ticker ORDER BY date)) / 
              LAG(close_price) OVER (PARTITION BY ticker ORDER BY date) * 100, 2) as daily_change_pct
    FROM stock_prices
),
ranked_days AS (
    SELECT 
        *,
        RANK() OVER (PARTITION BY ticker ORDER BY daily_change_pct DESC) as best_rank,
        RANK() OVER (PARTITION BY ticker ORDER BY daily_change_pct ASC) as worst_rank
    FROM daily_changes
    WHERE daily_change_pct IS NOT NULL
)
SELECT 
    ticker,
    date,
    close_price,
    daily_change_pct,
    CASE 
        WHEN best_rank = 1 THEN 'BEST DAY'
        WHEN worst_rank = 1 THEN 'WORST DAY'
    END as performance_type
FROM ranked_days
WHERE best_rank = 1 OR worst_rank = 1
ORDER BY ticker, performance_type DESC;
