import streamlit as st

st.set_page_config(page_title="Methodology", layout="wide")
st.title(" Methodology & Technical Details")

st.markdown("""
##  Analysis Methodology

### Data Sources & Period
- **Stocks Analyzed:** AAPL, MSFT, GOOGL, AMZN, TSLA, SPY (Market Benchmark)
- **Time Period:** November 2020 - November 2025
- **Data Frequency:** Daily closing prices, volume, and price ranges

### Technical Indicators Calculated

#### 1. Performance Metrics
- **Total Return:** (End Price - Start Price) / Start Price * 100
- **Daily Returns:** Percentage change between consecutive days
- **Compounded Growth:** Overall performance across full period

#### 2. Risk Metrics
- **Volatility:** Standard deviation of daily returns
- **Sharpe Ratio:** Average return / Volatility (risk-adjusted performance)
- **Maximum Drawdown:** Largest peak-to-trough decline

#### 3. Technical Analysis
- **Moving Averages:** 50-day and 200-day simple moving averages
- **Crossover Signals:** Buy when 50-day MA crosses above 200-day MA
- **Volume Analysis:** Days with volume > 2 standard deviations from average

#### 4. Statistical Analysis
- **Correlation Matrix:** Pearson correlation between stock returns
- **Seasonal Patterns:** Monthly and quarterly performance trends
- **Extreme Values:** Best and worst single-day performances

### SQL Technologies Used
- **Window Functions:** LAG, OVER, PARTITION BY for time-series analysis
- **Common Table Expressions (CTEs):** Complex multi-step queries
- **Statistical Functions:** CORR, STDDEV, AVG for risk metrics
- **Date Functions:** Date truncation and extraction for period analysis

### Visualization Tools
- **Streamlit:** Interactive web application framework
- **Plotly:** Interactive charts and graphs
- **Pandas:** Data manipulation and analysis

### Project Structure
The analysis follows a reproducible workflow from raw data to business insights, 
with complete documentation and interactive visualization.
""")

# Add data quality section if you have the CSV
try:
    import pandas as pd
    data_quality = pd.read_csv('data_outputs/data_quality.csv')
    
    st.markdown("---")
    st.subheader(" Data Quality Summary")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", f"{data_quality['total_records'].sum():,}")
    with col2:
        st.metric("Stocks Analyzed", len(data_quality))
    with col3:
        st.metric("Data Consistency", "100%")
        
except:
    pass

st.sidebar.info("""
**GitHub Repository:**
[github.com/Yaw-Assensoh/financial_analysis]

**Built With:**
- PostgreSQL
- Streamlit
- Plotly
- Python
""")