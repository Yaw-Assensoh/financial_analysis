-- ==========================================
-- BUSINESS QUESTION 3:
-- Which stocks have the best risk-adjusted returns?
-- Sharpe Ratio = Average Return / Volatility
-- ==========================================

WITH daily_returns AS (
    SELECT 
        ticker,
        date,
        ROUND(
            (close_price - LAG(close_price) OVER w) / 
            LAG(close_price) OVER w * 100, 
        2) as daily_return_pct
    FROM stock_prices 
    WINDOW w AS (PARTITION BY ticker ORDER BY date)
),
risk_metrics AS (
    SELECT 
        ticker,
        AVG(daily_return_pct) as avg_daily_return,
        STDDEV(daily_return_pct) as daily_volatility,
        AVG(daily_return_pct) / NULLIF(STDDEV(daily_return_pct), 0) as sharpe_ratio
    FROM daily_returns 
    WHERE daily_return_pct IS NOT NULL
    GROUP BY ticker
)
SELECT 
    ticker,
    ROUND(avg_daily_return, 3) as avg_daily_return_pct,
    ROUND(daily_volatility, 3) as daily_volatility_pct,
    ROUND(sharpe_ratio, 3) as sharpe_ratio,
    CASE 
        WHEN sharpe_ratio > 0.2 THEN 'EXCELLENT'
        WHEN sharpe_ratio > 0.1 THEN 'GOOD' 
        WHEN sharpe_ratio > 0 THEN 'FAIR'
        ELSE 'POOR'
    END as risk_adjusted_grade
FROM risk_metrics
ORDER BY sharpe_ratio DESC;