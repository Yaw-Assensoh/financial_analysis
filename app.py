import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Financial Analysis Dashboard",
    layout="wide"
)

st.title("Financial Analysis Dashboard")
st.markdown("---")

st.write("""
### Comprehensive Investment Analysis Platform

This dashboard provides in-depth analysis of stock performance, risk metrics, 
and market trends for major technology companies compared to market benchmarks.
""")

# Quick Overview
st.subheader("Portfolio Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Stocks Analyzed", "6", "Major Tech")

with col2:
    st.metric("Analysis Period", "5 Years", "2019-2024")

with col3:
    st.metric("Best Performer", "TSLA", "343.9%")

with col4:
    st.metric("Market Benchmark", "SPY", "100.0%")

# Navigation Guide
st.markdown("---")
st.subheader("Dashboard Sections")

st.write("""
- **Performance Analysis**: Total returns and annualized performance
- **Risk Analysis**: Volatility, beta, and risk-adjusted returns  
- **Correlation Analysis**: Inter-security relationships and diversification
- **Technical Analysis**: RSI signals and trading indicators
- **Methodology**: Data sources and analytical approach
""")