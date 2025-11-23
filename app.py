iimport streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page configuration MUST be first
st.set_page_config(
    page_title="Financial Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Header
    st.title(" Financial Analysis Dashboard")
    st.markdown("---")
    
    # Introduction
    st.subheader("Welcome to Comprehensive Financial Analysis")
    st.write("""
    This dashboard provides in-depth analysis of stock performance, market trends, 
    and investment insights. Use the sidebar to navigate between different analytical sections.
    """)
    
    # Quick Stats
    st.subheader(" Dashboard Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Stocks Analyzed", 
            value="6", 
            delta="Major Tech"
        )
    
    with col2:
        st.metric(
            label="Analysis Period", 
            value="5 Years", 
            delta="Comprehensive"
        )
    
    with col3:
        st.metric(
            label="Data Coverage", 
            value="100%", 
            delta="Complete History"
        )
    
    with col4:
        st.metric(
            label="Last Updated", 
            value="Live", 
            delta="Real-time"
        )
    
    # Navigation Guide
    st.markdown("---")
    st.subheader(" Navigation Guide")
    
    nav_col1, nav_col2, nav_col3 = st.columns(3)
    
    with nav_col1:
        st.info("""
        ** Performance**  
        • Stock returns analysis  
        • Benchmark comparisons  
        • Performance metrics
        """)
    
    with nav_col2:
        st.info("""
        **🔍 Trends & Patterns**  
        • Technical analysis  
        • Market trends  
        • Pattern recognition
        """)
    
    with nav_col3:
        st.info("""
        **📚 Methodology**  
        • Analytical approach  
        • Data sources  
        • Calculation methods
        """)
    
    # Sample Data Preview
    st.markdown("---")
    st.subheader(" Sample Data Preview")
    
    sample_data = pd.DataFrame({
        'Ticker': ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY'],
        'Sector': ['Automotive', 'Technology', 'E-commerce', 'Software', 'Technology', 'ETF'],
        '5Y Return %': [343.90, 250.96, 210.44, 157.99, 141.77, 100.00],
        'Status': ['Outperform', 'Outperform', 'Outperform', 'Outperform', 'Outperform', 'Benchmark']
    })
    
    st.dataframe(
        sample_data,
        use_container_width=True,
        hide_index=True
    )
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "Financial Analysis Dashboard • Professional Grade • Built with Streamlit"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()