-- ==========================================
-- BUSINESS QUESTION 6:
-- Moving Average Crossover Signals
-- Technical analysis for buy/sell signals
-- ==========================================

WITH moving_averages AS (
    SELECT 
        ticker,
        date,
        close_price,
        -- 50-day moving average
        AVG(close_price) OVER (
            PARTITION BY ticker 
            ORDER BY date 
            ROWS BETWEEN 49 PRECEDING AND CURRENT ROW
        ) as ma_50,
        -- 200-day moving average  
        AVG(close_price) OVER (
            PARTITION BY ticker 
            ORDER BY date 
            ROWS BETWEEN 199 PRECEDING AND CURRENT ROW
        ) as ma_200
    FROM stock_prices
),
crossover_signals AS (
    SELECT 
        *,
        LAG(ma_50) OVER (PARTITION BY ticker ORDER BY date) as prev_ma_50,
        LAG(ma_200) OVER (PARTITION BY ticker ORDER BY date) as prev_ma_200,
        CASE 
            WHEN ma_50 > ma_200 AND LAG(ma_50) OVER w <= LAG(ma_200) OVER w 
            THEN 'BUY SIGNAL'
            WHEN ma_50 < ma_200 AND LAG(ma_50) OVER w >= LAG(ma_200) OVER w 
            THEN 'SELL SIGNAL'
            ELSE 'HOLD'
        END as signal
    FROM moving_averages
    WINDOW w AS (PARTITION BY ticker ORDER BY date)
)
SELECT 
    ticker,
    date,
    ROUND(close_price, 2) as price,
    ROUND(ma_50, 2) as moving_avg_50,
    ROUND(ma_200, 2) as moving_avg_200,
    signal,
    CASE 
        WHEN signal != 'HOLD' THEN 'TRADE'
        ELSE 'NO ACTION'
    END as action
FROM crossover_signals
WHERE signal != 'HOLD'
ORDER BY ticker, date DESC
LIMIT 20;