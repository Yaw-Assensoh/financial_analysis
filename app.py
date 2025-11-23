import streamlit as st

st.set_page_config(
    page_title="Financial Analysis Dashboard",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2e86ab;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header"> Financial Analysis Dashboard</h1>', unsafe_allow_html=True)

# Hero section
col1, col2, col3 = st.columns([2, 1, 1])

with col1:
    st.markdown("""
    ### Comprehensive Stock Market Analysis Platform
    
    **Analyze 6 major stocks (AAPL, MSFT, GOOGL, AMZN, TSLA, SPY) with:**
    -  **Performance Metrics** - Total returns and benchmarks
    -  **Risk Assessment** - Volatility and Sharpe ratios  
    -  **Correlation Analysis** - Portfolio diversification
    -  **Trend Analysis** - Seasonal and monthly patterns
    -  **Technical Signals** - Trading indicators
    -  **Methodology** - Complete analysis framework
    """)

with col2:
    st.metric("Stocks Analyzed", "6")
    st.metric("Time Period", "2020-2025")
    st.metric("Analysis Types", "10+")

with col3:
    st.metric("Data Points", "30,000+")
    st.metric("SQL Queries", "10")
    st.metric("Visualizations", "15+")

# Quick insights section
st.markdown("---")
st.markdown('<h3 class="sub-header">🚀 Quick Insights</h3>', unsafe_allow_html=True)

insight_col1, insight_col2, insight_col3 = st.columns(3)

with insight_col1:
    with st.container():
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Top Performer", "TSLA", "343.9%")
        st.markdown('</div>', unsafe_allow_html=True)

with insight_col2:
    with st.container():
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Best Risk-Adjusted", "MSFT", "Sharpe: 0.18")
        st.markdown('</div>', unsafe_allow_html=True)

with insight_col3:
    with st.container():
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Market Benchmark", "SPY", "100.0%")
        st.markdown('</div>', unsafe_allow_html=True)

# Navigation guidance
st.markdown("---")
st.markdown("""
###  Navigation Guide
Use the sidebar on the left to explore different analytical perspectives:

1. ** Performance** - Returns and benchmarks
2. ** Risk Analysis** - Volatility and risk-adjusted metrics
3. ** Correlations** - Diversification opportunities  
4. ** Trends & Patterns** - Seasonal analysis
5. ** Technical Signals** - Trading indicators
6. ** Methodology** - Analysis framework
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Built with  using Streamlit | Data Source: Nasdaq | Analysis: PostgreSQL & Python</p>
    <p>Last Updated: December 2024</p>
</div>
""", unsafe_allow_html=True)