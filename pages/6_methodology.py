import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Methodology & Approach",
    page_icon="📚",
    layout="wide"
)

def main():
    st.title(" Methodology & Analytical Approach")
    st.markdown("---")
    
    # Introduction
    st.write("""
    This section details the comprehensive methodology and analytical framework employed in our financial analysis platform. 
    We maintain transparency in our processes to ensure reproducible and credible insights.
    """)
    
    # Data Collection Section
    st.header(" Data Collection & Sources")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Primary Data Sources")
        st.markdown("""
        - **Yahoo Finance API**: Historical price data and market information
        - **Analysis Period**: 5-year historical data (2019-2024)
        - **Frequency**: Daily closing prices adjusted for splits
        - **Coverage**: End-of-day prices, volume, market capitalization
        """)
        
    with col2:
        st.subheader("Securities Analyzed")
        st.markdown("""
        - **Technology Leaders**: TSLA, GOOGL, AMZN, MSFT, AAPL
        - **Market Benchmark**: SPY (S&P 500 ETF Trust)
        - **Sector Coverage**: Technology, Automotive, E-commerce, Software
        - **Market Representation**: Large-cap US equities
        """)
    
    # Performance Calculation Methodology
    st.header(" Performance Calculation Methodology")
    
    st.subheader("Return Calculations")
    st.markdown("""
    **Total Return Formula:**
    ```
    Total Return = (Ending Price - Beginning Price) / Beginning Price × 100
    ```
    
    **Annualized Return (CAGR):**
    ```
    CAGR = (Ending Value / Beginning Value)^(1/Years) - 1
    ```
    """)
    
    # Metrics Explanation
    st.subheader("Key Performance Metrics")
    
    metrics_data = {
        'Metric': ['Total Return', 'Annualized Return', 'Volatility', 'Outperformance', 'Maximum Drawdown'],
        'Calculation': [
            'Simple percentage return over entire period',
            'Compound Annual Growth Rate (CAGR)',
            'Standard deviation of daily returns (annualized)',
            'Return comparison against SPY benchmark',
            'Maximum peak-to-trough decline during period'
        ],
        'Purpose': [
            'Overall performance measurement',
            'Standardized annual performance',
            'Risk and variability assessment',
            'Relative performance analysis',
            'Risk management indicator'
        ]
    }
    
    metrics_df = pd.DataFrame(metrics_data)
    st.dataframe(metrics_df, use_container_width=True, hide_index=True)
    
    # Technical Analysis Framework
    st.header(" Technical Analysis Framework")
    
    tech_col1, tech_col2 = st.columns(2)
    
    with tech_col1:
        st.subheader("Technical Indicators")
        st.markdown("""
        **Trend Analysis:**
        - 50-day Moving Average (Medium-term trend)
        - 200-day Moving Average (Long-term trend)
        - Price momentum and direction
        
        **Volatility Measures:**
        - Standard deviation of returns
        - Beta relative to market
        - Historical volatility patterns
        """)
    
    with tech_col2:
        st.subheader("Analytical Methods")
        st.markdown("""
        **Comparative Analysis:**
        - Cross-security performance comparison
        - Sector-relative strength analysis
        - Benchmark-relative positioning
        
        **Pattern Recognition:**
        - Support and resistance levels
        - Trend consistency evaluation
        - Momentum confirmation signals
        """)
    
    # Risk Management & Assumptions
    st.header(" Risk Management & Assumptions")
    
    st.subheader("Key Assumptions")
    st.markdown("""
    - **Dividend Treatment**: Total return calculations exclude dividends for consistency
    - **Transaction Costs**: Analysis excludes brokerage fees and transaction costs
    - **Liquidity**: Assumes sufficient market liquidity for all positions
    - **Tax Considerations**: Returns calculated on pre-tax basis
    - **Reinvestment**: Does not assume dividend or return reinvestment
    """)
    
    st.subheader("Risk Considerations")
    st.markdown("""
    - **Historical Limitation**: Past performance doesn't guarantee future results
    - **Market Conditions**: Analysis reflects specific historical market environment
    - **Concentration Risk**: Technology sector concentration in current analysis
    - **Volatility Impact**: Higher returns often correlate with higher volatility
    """)
    
    # Data Quality & Validation
    st.header(" Data Quality & Validation")
    
    st.markdown("""
    **Quality Assurance Processes:**
    - Automated data validation checks
    - Outlier detection and handling
    - Missing data interpolation
    - Cross-verification with alternative sources
    
    **Validation Methods:**
    - Price data consistency verification
    - Return calculation cross-checks
    - Statistical significance testing
    - Peer comparison validation
    """)
    
    # Implementation Details
    st.header(" Technical Implementation")
    
    impl_col1, impl_col2 = st.columns(2)
    
    with impl_col1:
        st.subheader("Technology Stack")
        st.markdown("""
        - **Platform**: Streamlit for web application framework
        - **Data Analysis**: Pandas for data manipulation and analysis
        - **Visualization**: Matplotlib for charting and graphics
        - **Data Source**: yFinance for market data retrieval
        - **Computing**: NumPy for numerical computations
        """)
    
    with impl_col2:
        st.subheader("Architecture")
        st.markdown("""
        - **Modular Design**: Separate components for data, analysis, presentation
        - **Caching**: Optimized data loading and computation caching
        - **Responsive Design**: Mobile-friendly interface adaptation
        - **Real-time Capability**: Framework supports live data integration
        """)
    
    # Disclaimer Section
    st.markdown("---")
    st.header(" Important Disclosures & Limitations")
    
    st.warning("""
    **Educational Purpose Disclaimer:**
    This analysis is provided strictly for educational and informational purposes. 
    The content represents analytical exercises and should not be construed as 
    investment advice or recommendations.
    
    **Key Limitations:**
    - Historical analysis may not predict future performance
    - Results are specific to the analyzed time period
    - Individual investment circumstances vary significantly
    - Market conditions change over time
    
    **Professional Advice:**
    Always consult with qualified financial professionals and conduct 
    independent research before making investment decisions. 
    Consider your individual risk tolerance, investment objectives, 
    and financial situation.
    """)
    
    # Contact & References
    st.markdown("---")
    st.header(" Additional Information")
    
    info_col1, info_col2 = st.columns(2)
    
    with info_col1:
        st.subheader("Documentation References")
        st.markdown("""
        - Yahoo Finance API Documentation
        - Streamlit Framework Documentation  
        - Pandas Library Documentation
        - Modern Portfolio Theory References
        """)
    
    with info_col2:
        st.subheader("Update Information")
        st.markdown("""
        - **Last Updated**: Current deployment date
        - **Data Freshness**: End-of-day updates
        - **Methodology Version**: 1.0
        - **Next Review**: Periodic methodology assessment
        """)

if __name__ == "__main__":
    main()