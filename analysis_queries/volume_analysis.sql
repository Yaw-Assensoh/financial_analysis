-- ==========================================
-- BUSINESS QUESTION 9:
-- High Volume Days Analysis
-- Identify unusual trading activity
-- ==========================================

WITH volume_stats AS (
    SELECT 
        ticker,
        AVG(volume) as avg_volume,
        STDDEV(volume) as std_volume
    FROM stock_prices
    GROUP BY ticker
),
high_volume_days AS (
    SELECT 
        p.ticker,
        p.date,
        p.close_price,
        p.volume,
        ROUND(p.volume / s.avg_volume, 2) as volume_ratio,
        ROUND((p.volume - s.avg_volume) / s.std_volume, 2) as volume_z_score
    FROM stock_prices p
    JOIN volume_stats s ON p.ticker = s.ticker
    WHERE p.volume > s.avg_volume + (s.std_volume * 2)  -- 2 standard deviations above average
)
SELECT *
FROM high_volume_days
ORDER BY volume_z_score DESC
LIMIT 20;
