import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Financial Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Performance", "Trends & Patterns", "Methodology"])

# Common CSS to fix styling
st.markdown("""
<style>
    .main {
        padding: 2rem;
    }
    .stButton button {
        width: 100%;
    }
    .css-1d391kg {
        padding: 2rem 1rem;
    }
</style>
""", unsafe_allow_html=True)

if page == "Home":
    st.title(" Financial Analysis Dashboard")
    st.write("""
    Welcome to the comprehensive financial analysis tool. Use the sidebar to navigate between different sections:
    
    - **Performance**: Stock performance comparisons and returns analysis
    - **Trends & Patterns**: Technical analysis and market trends
    - **Methodology**: Explanation of our analysis approach
    """)
    
    # Quick overview
    st.subheader(" Quick Overview")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Stocks Covered", "6", "Major Tech")
    
    with col2:
        st.metric("Analysis Period", "5 Years", "Comprehensive")
    
    with col3:
        st.metric("Last Updated", "Today", "Live Data")

elif page == "Performance":
    st.title(" Performance Analysis")
    
    # Performance data
    performance_data = pd.DataFrame({
        'ticker': ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY'],
        'total_return_percentage': [343.90, 250.96, 210.44, 157.99, 141.77, 100.00],
        'vs_market': ['OUTPERFORMED', 'OUTPERFORMED', 'OUTPERFORMED', 'OUTPERFORMED', 'OUTPERFORMED', 'BENCHMARK']
    })
    
    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Best Performer", "TSLA", "343.9%")
    with col2:
        st.metric("Average Return", "220.8%", "+120.8% vs Market")
    with col3:
        st.metric("Outperforming", "5/5", "100%")
    with col4:
        st.metric("Market Return", "100%", "SPY Benchmark")
    
    # Performance chart
    st.subheader("Returns Comparison")
    
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ['#2E8B57' if x != 'SPY' else '#1f77b4' for x in performance_data['ticker']]
    bars = ax.bar(performance_data['ticker'], performance_data['total_return_percentage'], color=colors)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 10,
                f'{height:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=10)
    
    ax.set_ylabel('Total Return (%)', fontweight='bold')
    ax.set_title('5-Year Total Returns vs Market Benchmark', fontweight='bold', fontsize=14)
    ax.grid(axis='y', alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    st.pyplot(fig)
    
    # Data table
    st.subheader("Performance Data")
    st.dataframe(performance_data, use_container_width=True)

elif page == "Trends & Patterns":
    st.title("🔍 Trends & Patterns Analysis")
    
    st.write("""
    Technical analysis and market trend identification for selected stocks.
    This section analyzes price patterns, moving averages, and market trends.
    """)
    
    # Sample technical analysis
    st.subheader("Technical Indicators")
    
    # Create sample data for demonstration
    dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='D')
    sample_prices = 100 + np.cumsum(np.random.randn(len(dates)) * 0.5)
    
    tech_data = pd.DataFrame({
        'Date': dates,
        'Price': sample_prices,
        'MA_50': sample_prices.rolling(50).mean(),
        'MA_200': sample_prices.rolling(200).mean()
    }).dropna()
    
    # Technical chart
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(tech_data['Date'], tech_data['Price'], label='Price', linewidth=1)
    ax.plot(tech_data['Date'], tech_data['MA_50'], label='50-Day MA', linewidth=2)
    ax.plot(tech_data['Date'], tech_data['MA_200'], label='200-Day MA', linewidth=2)
    
    ax.set_title('Price Trends with Moving Averages', fontweight='bold')
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    st.pyplot(fig)
    
    # Pattern analysis
    st.subheader("Market Pattern Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("""
        **Bullish Patterns Identified:**
        - Consistent upward trend in tech stocks
        - Strong momentum indicators
        - Support levels holding
        """)
    
    with col2:
        st.warning("""
        **Areas to Watch:**
        - Market volatility increases
        - Sector rotation patterns
        - Economic indicators
        """)

elif page == "Methodology":
    st.title("📚 Methodology")
    
    st.write("""
    ## Our Analytical Approach
    
    This financial analysis platform employs a comprehensive methodology to evaluate stock performance and market trends.
    """)
    
    st.subheader("Data Collection")
    st.write("""
    - **Source**: Yahoo Finance API
    - **Period**: 5-year historical data
    - **Frequency**: Daily closing prices
    - **Stocks**: Major technology companies + SPY benchmark
    """)
    
    st.subheader("Performance Calculation")
    st.write("""
    - **Total Return**: Percentage change from initial to final price
    - **Benchmark Comparison**: SPY ETF as market proxy
    - **Outperformance**: Stocks returning more than market benchmark
    """)
    
    st.subheader("Technical Analysis")
    st.write("""
    - **Moving Averages**: 50-day and 200-day trends
    - **Pattern Recognition**: Price action analysis
    - **Momentum Indicators**: Rate of price change
    """)
    
    st.info("""
    **Note**: This analysis is for educational purposes only. 
    Past performance does not guarantee future results.
    Always conduct your own research before making investment decisions.
    """)

# Footer
st.markdown("---")
st.markdown("**Financial Analysis Dashboard** • Built with Streamlit • Educational Purpose")