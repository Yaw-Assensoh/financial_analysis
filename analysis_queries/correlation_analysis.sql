-- ==========================================
-- BUSINESS QUESTION 5:
-- How correlated are these stocks?
-- Important for portfolio diversification
-- ==========================================

WITH daily_returns AS (
    SELECT 
        date,
        ticker,
        (close_price - LAG(close_price) OVER (PARTITION BY ticker ORDER BY date)) / 
        LAG(close_price) OVER (PARTITION BY ticker ORDER BY date) as daily_return
    FROM stock_prices 
),
correlation_matrix AS (
    SELECT 
        a.ticker as stock_a,
        b.ticker as stock_b,
        CORR(a.daily_return, b.daily_return) as correlation_coefficient,
        COUNT(*) as overlapping_days
    FROM daily_returns a
    JOIN daily_returns b ON a.date = b.date AND a.ticker < b.ticker
    WHERE a.daily_return IS NOT NULL AND b.daily_return IS NOT NULL
    GROUP BY a.ticker, b.ticker
)
SELECT 
    stock_a,
    stock_b,
    -- FIX: CAST to numeric before rounding
    ROUND(correlation_coefficient::numeric, 3) as correlation,
    overlapping_days,
    CASE 
        WHEN correlation_coefficient > 0.7 THEN 'HIGHLY CORRELATED'
        WHEN correlation_coefficient > 0.3 THEN 'MODERATELY CORRELATED'
        WHEN correlation_coefficient > 0 THEN 'WEAKLY CORRELATED'
        WHEN correlation_coefficient = 0 THEN 'NO CORRELATION'
        ELSE 'NEGATIVELY CORRELATED'
    END as correlation_strength
FROM correlation_matrix
ORDER BY correlation DESC;