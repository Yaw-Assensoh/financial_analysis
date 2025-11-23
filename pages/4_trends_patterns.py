import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Trends & Patterns",
)

st.title(" Trends & Patterns Analysis")
st.markdown("---")

st.write("""
Technical analysis and market trend identification for comprehensive market understanding.
This section analyzes price patterns, moving averages, and emerging market trends.
""")

# Sample Technical Data
st.subheader(" Technical Indicators")

# Generate sample price data
dates = pd.date_range(start='2020-01-01', periods=1000, freq='D')
base_price = 100
np.random.seed(42)  # For reproducible results
price_data = base_price + np.cumsum(np.random.randn(1000) * 0.5)

technical_df = pd.DataFrame({
    'Date': dates,
    'Price': price_data,
    'MA_50': pd.Series(price_data).rolling(50).mean(),
    'MA_200': pd.Series(price_data).rolling(200).mean()
})

# Technical Analysis Chart
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(technical_df['Date'], technical_df['Price'], 
        label='Price', linewidth=1.5, alpha=0.8)
ax.plot(technical_df['Date'], technical_df['MA_50'], 
        label='50-Day MA', linewidth=2, color='orange')
ax.plot(technical_df['Date'], technical_df['MA_200'], 
        label='200-Day MA', linewidth=2, color='red')

ax.set_title('Price Trends with Moving Averages', fontweight='bold', fontsize=14)
ax.set_ylabel('Price', fontweight='bold')
ax.legend()
ax.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# Market Insights
st.markdown("---")
st.subheader(" Market Pattern Analysis")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    ** Bullish Indicators:**
    - Consistent upward trend in technology sector
    - Strong momentum across major indices
    - Support levels maintaining strength
    - Volume patterns supporting price movements
    """)

with col2:
    st.warning("""
    ** Areas Monitoring:**
    - Market volatility fluctuations
    - Sector rotation patterns
    - Economic indicator correlations
    - Global market influences
    """)

# Additional Analysis
st.markdown("---")
st.subheader(" Pattern Recognition")

st.write("""
**Identified Patterns:**
- **Trend Consistency**: Sustained upward movement in tech stocks
- **Momentum Alignment**: Price and volume trends showing correlation  
- **Support Levels**: Key technical levels holding during pullbacks
- **Sector Strength**: Technology sector demonstrating relative strength
""")