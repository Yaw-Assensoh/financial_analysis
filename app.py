import streamlit as st
import pandas as pd

# Configure page FIRST
st.set_page_config(
    page_title="Financial Analysis",
    page_icon="📈",
    layout="wide"
)

st.title(" FINANCIAL ANALYSIS DASHBOARD")
st.markdown("---")

# Test basic functionality first
try:
    # Test pandas
    performance_data = pd.DataFrame({
        'Ticker': ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY'],
        'Return %': [343.90, 250.96, 210.44, 157.99, 141.77, 100.00],
        'Status': ['OUTPERFORM', 'OUTPERFORM', 'OUTPERFORM', 'OUTPERFORM', 'OUTPERFORM', 'BENCHMARK']
    })
    
    st.success(" PANDAS WORKING!")
    
    # Display metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Best Performer", "TSLA", "343.9%")
    with col2:
        st.metric("Stocks Analyzed", "6")
    with col3:
        st.metric("Outperforming", "5/5")
    
    # Show data
    st.subheader(" PERFORMANCE DATA")
    st.dataframe(performance_data, use_container_width=True)
    
    # Try matplotlib with error handling
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        
        st.success("MATPLOTLIB WORKING!")
        
        # Create simple chart
        fig, ax = plt.subplots(figsize=(10, 6))
        
        colors = ['#00FF00' if ticker != 'SPY' else '#1f77b4' 
                 for ticker in performance_data['Ticker']]
        
        bars = ax.bar(performance_data['Ticker'], performance_data['Return %'], 
                     color=colors, alpha=0.8)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 10,
                   f'{height:.1f}%', ha='center', va='bottom', 
                   fontweight='bold', fontsize=10)
        
        ax.set_ylabel('Total Return (%)', fontweight='bold', fontsize=12)
        ax.set_title('STOCK PERFORMANCE vs MARKET BENCHMARK', 
                    fontweight='bold', fontsize=14)
        ax.grid(axis='y', alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        st.subheader(" PERFORMANCE CHART")
        st.pyplot(fig)
        
    except ImportError as e:
        st.error(f" MATPLOTLIB ERROR: {e}")
        st.info("Using Streamlit native charts instead...")
        st.bar_chart(performance_data.set_index('Ticker')['Return %'])
    
    # Additional sections
    st.markdown("---")
    st.subheader(" QUICK ANALYSIS")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Top Performers:**")
        st.write("1. TSLA: 343.9%")
        st.write("2. GOOGL: 251.0%") 
        st.write("3. AMZN: 210.4%")
    
    with col2:
        st.write("**Key Insights:**")
        st.write("• All tech stocks outperformed SPY")
        st.write("• Average return: 220.8%")
        st.write("• Strong sector performance")
        
except Exception as e:
    st.error(f"🚨 CRITICAL ERROR: {e}")
    st.write("Please check requirements.txt and deployment settings")

# Footer
st.markdown("---")
st.markdown("**Financial Analysis Dashboard** • Built with Streamlit")