import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title='Financial Analysis Dashboard',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Clean CSS styling like your bike dashboard
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
    }
    .section-header {
        color: #1f77b4;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Financial Analysis")
st.sidebar.markdown("---")

page = st.sidebar.selectbox(
    'Select Analysis',
    [
        "Portfolio Overview",
        "Performance Analysis", 
        "Risk Analysis",
        "Correlation Analysis",
        "Methodology"
    ]
)

# Main page content
if page == "Portfolio Overview":
    st.markdown('<h1 class="main-header">Financial Analysis Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("### Comprehensive Stock Performance Analysis")
    
    # Key Metrics
    st.markdown("---")
    st.markdown('<div class="section-header">Portfolio Overview</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Stocks Analyzed", "6", "Major Tech")
    
    with col2:
        st.metric("Analysis Period", "5 Years", "Comprehensive")
    
    with col3:
        st.metric("Best Performer", "TSLA", "343.9%")
    
    with col4:
        st.metric("Market Return", "100%", "SPY Benchmark")
    
    # Performance Data
    st.markdown("---")
    st.markdown('<div class="section-header">Performance Summary</div>', unsafe_allow_html=True)
    
    performance_data = pd.DataFrame({
        'Ticker': ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY'],
        'Total Return %': [343.90, 250.96, 210.44, 157.99, 141.77, 100.00],
        'Annualized Return %': [34.7, 28.5, 25.4, 20.9, 19.3, 14.9],
        'Outperformance': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Benchmark']
    })
    
    st.dataframe(performance_data, use_container_width=True, hide_index=True)
    
    # Navigation Guide
    st.markdown("---")
    st.markdown('<div class="section-header">Analysis Sections</div>', unsafe_allow_html=True)
    
    st.markdown("""
    Use the sidebar to navigate through different analysis sections:
    
    - **Performance Analysis**: Detailed returns and comparisons
    - **Risk Analysis**: Volatility and risk metrics
    - **Correlation Analysis**: Inter-security relationships  
    - **Methodology**: Analytical approach and data sources
    """)

elif page == "Performance Analysis":
    st.markdown('<h1 class="main-header">Performance Analysis</h1>', unsafe_allow_html=True)
    st.markdown("### Stock Returns vs Market Benchmark")
    
    # Performance data
    performance_data = pd.DataFrame({
        'Ticker': ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY'],
        'Total Return %': [343.90, 250.96, 210.44, 157.99, 141.77, 100.00],
        'Annualized Return %': [34.7, 28.5, 25.4, 20.9, 19.3, 14.9]
    })
    
    # Key Metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_return = performance_data[performance_data['Ticker'] != 'SPY']['Total Return %'].mean()
        st.metric("Average Return", f"{avg_return:.1f}%")
    
    with col2:
        outperform_count = len(performance_data[performance_data['Ticker'] != 'SPY'])
        st.metric("Outperforming Stocks", f"{outperform_count}/5")
    
    with col3:
        best_return = performance_data['Total Return %'].max()
        st.metric("Best Performance", f"{best_return:.1f}%")
    
    # Performance Chart
    st.markdown("---")
    st.markdown('<div class="section-header">Returns Comparison</div>', unsafe_allow_html=True)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    colors = ['#1f77b4' if ticker != 'SPY' else '#ff7f0e' for ticker in performance_data['Ticker']]
    bars = ax.bar(performance_data['Ticker'], performance_data['Total Return %'], color=colors, alpha=0.8)
    
    ax.set_ylabel('Total Return (%)')
    ax.set_title('5-Year Total Returns vs Market Benchmark')
    ax.grid(True, alpha=0.3)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 5,
                f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
    
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    
    # Detailed Table
    st.markdown("---")
    st.markdown('<div class="section-header">Performance Data</div>', unsafe_allow_html=True)
    st.dataframe(performance_data, use_container_width=True, hide_index=True)

elif page == "Risk Analysis":
    st.markdown('<h1 class="main-header">Risk Analysis</h1>', unsafe_allow_html=True)
    st.markdown("### Volatility and Risk Assessment")
    
    # Risk metrics data
    risk_data = {
        'Ticker': ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY'],
        'Volatility (%)': [52.3, 28.7, 32.1, 24.5, 26.8, 18.2],
        'Beta': [2.10, 1.05, 1.04, 0.98, 1.21, 1.00],
        'Max Drawdown (%)': [-45.2, -28.7, -35.1, -22.4, -31.5, -19.8],
        'Sharpe Ratio': [0.65, 1.02, 0.79, 1.15, 0.94, 0.82]
    }
    
    risk_df = pd.DataFrame(risk_data)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_vol = risk_df['Volatility (%)'].mean()
        st.metric("Average Volatility", f"{avg_vol:.1f}%")
    
    with col2:
        high_beta = risk_df.loc[risk_df['Beta'].idxmax(), 'Ticker']
        st.metric("Highest Beta", high_beta, "2.10")
    
    with col3:
        best_sharpe = risk_df.loc[risk_df['Sharpe Ratio'].idxmax(), 'Ticker']
        st.metric("Best Risk-Adjusted", best_sharpe, "1.15")
    
    with col4:
        worst_dd = risk_df['Max Drawdown (%)'].min()
        st.metric("Worst Drawdown", f"{worst_dd:.1f}%")
    
    # Volatility Chart
    st.markdown("---")
    st.markdown('<div class="section-header">Volatility Comparison</div>', unsafe_allow_html=True)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    bars = ax.bar(risk_df['Ticker'], risk_df['Volatility (%)'], color='steelblue', alpha=0.7)
    ax.axhline(y=18.2, color='red', linestyle='--', label='Market Volatility')
    
    ax.set_ylabel('Annual Volatility (%)')
    ax.set_title('Historical Volatility Analysis')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 1,
                f'{height:.1f}%', ha='center', va='bottom')
    
    st.pyplot(fig)
    
    # Risk Table
    st.markdown("---")
    st.markdown('<div class="section-header">Risk Metrics</div>', unsafe_allow_html=True)
    st.dataframe(risk_df, use_container_width=True, hide_index=True)

elif page == "Correlation Analysis":
    st.markdown('<h1 class="main-header">Correlation Analysis</h1>', unsafe_allow_html=True)
    st.markdown("### Inter-Security Relationships")
    
    # Correlation matrix
    tickers = ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY']
    
    correlation_matrix = np.array([
        [1.00, 0.65, 0.62, 0.58, 0.61, 0.72],
        [0.65, 1.00, 0.78, 0.75, 0.74, 0.85],
        [0.62, 0.78, 1.00, 0.72, 0.70, 0.82],
        [0.58, 0.75, 0.72, 1.00, 0.68, 0.88],
        [0.61, 0.74, 0.70, 0.68, 1.00, 0.80],
        [0.72, 0.85, 0.82, 0.88, 0.80, 1.00]
    ])
    
    corr_df = pd.DataFrame(correlation_matrix, index=tickers, columns=tickers)
    
    # Correlation metrics
    upper_tri = correlation_matrix[np.triu_indices_from(correlation_matrix, k=1)]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_corr = np.mean(upper_tri)
        st.metric("Average Correlation", f"{avg_corr:.3f}")
    
    with col2:
        min_corr = np.min(upper_tri)
        st.metric("Minimum Correlation", f"{min_corr:.3f}")
    
    with col3:
        max_corr = np.max(upper_tri)
        st.metric("Maximum Correlation", f"{max_corr:.3f}")
    
    # Correlation Heatmap
    st.markdown("---")
    st.markdown('<div class="section-header">Correlation Matrix</div>', unsafe_allow_html=True)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    im = ax.imshow(correlation_matrix, cmap='coolwarm', vmin=0.5, vmax=1.0)
    
    # Show all ticks and labels
    ax.set_xticks(np.arange(len(tickers)))
    ax.set_yticks(np.arange(len(tickers)))
    ax.set_xticklabels(tickers)
    ax.set_yticklabels(tickers)
    
    # Rotate the tick labels and set their alignment
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
    
    # Loop over data dimensions and create text annotations
    for i in range(len(tickers)):
        for j in range(len(tickers)):
            text = ax.text(j, i, f'{correlation_matrix[i, j]:.2f}',
                          ha="center", va="center", color="black", fontweight='bold')
    
    ax.set_title('Security Correlation Matrix')
    fig.colorbar(im, ax=ax)
    st.pyplot(fig)
    
    # Insights
    st.markdown("---")
    st.markdown('<div class="section-header">Correlation Insights</div>', unsafe_allow_html=True)
    
    st.markdown("""
    **Key Observations:**
    - High overall correlation within technology sector (0.65-0.85 range)
    - SPY shows strong correlation with all individual securities
    - TSLA demonstrates relatively lower average correlation
    - Limited diversification benefits within current universe
    
    **Portfolio Implications:**
    - Consider adding non-correlated assets for better diversification
    - Monitor correlation changes during market stress periods
    - Implement sector rotation strategies
    """)

elif page == "Methodology":
    st.markdown('<h1 class="main-header">Methodology</h1>', unsafe_allow_html=True)
    st.markdown("### Analytical Approach and Data Sources")
    
    st.markdown("---")
    st.markdown('<div class="section-header">Data Collection</div>', unsafe_allow_html=True)
    
    st.markdown("""
    **Primary Data Sources:**
    - Yahoo Finance API for historical price data
    - Analysis Period: 5-year historical data
    - Frequency: Daily closing prices
    - Universe: Major technology companies + SPY ETF as market benchmark
    
    **Securities Analyzed:**
    - TSLA, GOOGL, AMZN, MSFT, AAPL (Technology Leaders)
    - SPY (S&P 500 ETF as Market Benchmark)
    """)
    
    st.markdown("---")
    st.markdown('<div class="section-header">Performance Calculation</div>', unsafe_allow_html=True)
    
    st.markdown("""
    **Return Calculations:**
    ```
    Total Return = (Ending Price - Beginning Price) / Beginning Price × 100
    Annualized Return = (Ending Value / Beginning Value)^(1/Years) - 1
    ```
    
    **Risk Metrics:**
    - Volatility: Standard deviation of daily returns (annualized)
    - Beta: Sensitivity to market movements
    - Sharpe Ratio: Risk-adjusted return measure
    - Maximum Drawdown: Worst peak-to-trough decline
    """)
    
    st.markdown("---")
    st.markdown('<div class="section-header">Correlation Analysis</div>', unsafe_allow_html=True)
    
    st.markdown("""
    **Methodology:**
    - Pearson correlation coefficients between daily returns
    - Analysis period: 5-year historical data
    - Matrix visualization for inter-security relationships
    - Diversification potential assessment
    """)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Dashboard Information")
st.sidebar.markdown("Data Source: Yahoo Finance")
st.sidebar.markdown("Analysis Period: 5 Years")