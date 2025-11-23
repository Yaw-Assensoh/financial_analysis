import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Performance Analysis",
    
)

st.title(" Performance Analysis")
st.markdown("---")

# Performance Data
@st.cache_data
def load_performance_data():
    return pd.DataFrame({
        'Ticker': ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY'],
        'Total Return %': [343.90, 250.96, 210.44, 157.99, 141.77, 100.00],
        'Annualized Return %': [34.7, 28.5, 25.4, 20.9, 19.3, 14.9],
        'Volatility %': [52.3, 28.7, 32.1, 24.5, 26.8, 18.2],
        'Outperformance': ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Benchmark']
    })

performance_data = load_performance_data()

# Key Metrics
st.subheader(" Key Performance Metrics")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    avg_return = performance_data[performance_data['Ticker'] != 'SPY']['Total Return %'].mean()
    st.metric("Average Return", f"{avg_return:.1f}%")

with metric_col2:
    outperform_count = len(performance_data[performance_data['Outperformance'] == 'Yes'])
    st.metric("Outperforming Stocks", f"{outperform_count}/5")

with metric_col3:
    best_performer = performance_data.loc[performance_data['Total Return %'].idxmax(), 'Ticker']
    best_return = performance_data['Total Return %'].max()
    st.metric("Best Performer", best_performer, f"{best_return:.1f}%")

with metric_col4:
    market_return = performance_data[performance_data['Ticker'] == 'SPY']['Total Return %'].iloc[0]
    st.metric("Market Return", f"{market_return:.1f}%")

# Performance Chart
st.markdown("---")
st.subheader("Returns Comparison")

fig, ax = plt.subplots(figsize=(12, 6))

# Create bars with conditional coloring
colors = ['#2E8B57' if ticker != 'SPY' else '#1f77b4' 
          for ticker in performance_data['Ticker']]

bars = ax.bar(performance_data['Ticker'], 
              performance_data['Total Return %'], 
              color=colors, 
              alpha=0.8)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 10,
            f'{height:.1f}%', 
            ha='center', va='bottom',
            fontweight='bold', fontsize=11)

ax.set_ylabel('Total Return (%)', fontweight='bold', fontsize=12)
ax.set_title('5-Year Total Returns vs Market Benchmark (SPY)', 
             fontweight='bold', fontsize=14)
ax.grid(axis='y', alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# Detailed Data Table
st.markdown("---")
st.subheader(" Detailed Performance Data")

st.dataframe(
    performance_data,
    use_container_width=True,
    hide_index=True
)

# Performance Insights
st.markdown("---")
st.subheader(" Performance Insights")

insight_col1, insight_col2 = st.columns(2)

with insight_col1:
    st.success("""
    **Strengths:**
    - All analyzed stocks significantly outperformed the market
    - Technology sector showing strong growth momentum
    - Consistent performance across major tech companies
    """)

with insight_col2:
    st.info("""
    **Considerations:**
    - Higher returns often correlate with higher volatility
    - Past performance doesn't guarantee future results
    - Diversification remains important
    """)