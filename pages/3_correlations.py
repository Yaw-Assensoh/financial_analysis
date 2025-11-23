import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Correlation Analysis",
)

st.title("Correlation Analysis")
st.markdown("---")

# Correlation Data
@st.cache_data
def load_correlation_data():
    tickers = ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY']
    
    correlation_matrix = np.array([
        [1.00, 0.65, 0.62, 0.58, 0.61, 0.72],
        [0.65, 1.00, 0.78, 0.75, 0.74, 0.85],
        [0.62, 0.78, 1.00, 0.72, 0.70, 0.82],
        [0.58, 0.75, 0.72, 1.00, 0.68, 0.88],
        [0.61, 0.74, 0.70, 0.68, 1.00, 0.80],
        [0.72, 0.85, 0.82, 0.88, 0.80, 1.00]
    ])
    
    return pd.DataFrame(correlation_matrix, index=tickers, columns=tickers)

corr_df = load_correlation_data()

# Correlation Statistics
st.subheader("Correlation Overview")

upper_tri = corr_df.values[np.triu_indices_from(corr_df.values, k=1)]

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

# Correlation Matrix Display
st.markdown("---")
st.subheader("Correlation Matrix")

fig, ax = plt.subplots(figsize=(8, 6))

im = ax.imshow(corr_df.values, cmap='coolwarm', vmin=0.5, vmax=1.0)

ax.set_xticks(np.arange(len(corr_df.columns)))
ax.set_yticks(np.arange(len(corr_df.index)))
ax.set_xticklabels(corr_df.columns)
ax.set_yticklabels(corr_df.index)

plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

for i in range(len(corr_df.index)):
    for j in range(len(corr_df.columns)):
        text = ax.text(j, i, f'{corr_df.values[i, j]:.2f}',
                      ha="center", va="center", color="black", fontweight='bold')

ax.set_title('Security Correlation Matrix', fontweight='bold', fontsize=14)
fig.colorbar(im, ax=ax)
st.pyplot(fig)

# Detailed Data Table
st.markdown("---")
st.subheader("Correlation Data")

st.dataframe(corr_df, use_container_width=True)

# Correlation Insights
st.markdown("---")
st.subheader("Diversification Analysis")

insight_col1, insight_col2 = st.columns(2)

with insight_col1:
    st.success("""
    **Diversification Opportunities:**
    - TSLA shows relatively lower average correlation
    - Technology subsector variations provide some diversification
    - Consider adding non-tech assets for better diversification
    """)

with insight_col2:
    st.warning("""
    **Concentration Risks:**
    - High overall correlation within technology sector
    - Strong market beta across all holdings
    - Limited diversification within current universe
    """)