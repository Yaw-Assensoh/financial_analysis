-- ==========================================
-- DATA VALIDATION & CLEANING
-- Business Need: Ensure data quality before analysis
-- ==========================================

-- Check for duplicates
SELECT ticker, date, COUNT(*) as duplicate_count
FROM stock_prices 
GROUP BY ticker, date
HAVING COUNT(*) > 1;

-- Validate date ranges and record counts
SELECT 
    ticker,
    COUNT(*) as total_records,
    MIN(date) as start_date,
    MAX(date) as end_date
FROM stock_prices 
GROUP BY ticker;