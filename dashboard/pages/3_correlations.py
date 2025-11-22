import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Correlation Analysis", layout="wide")
st.title("Correlation Analysis")

@st.cache_data
def load_correlation_data():
    return pd.read_csv('../data_outputs/stock_correlations.csv')

correlation_data = load_correlation_data()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Stock Correlation Matrix")
    
    # Create correlation matrix for heatmap
    corr_pivot = correlation_data.pivot(index='stock_a', columns='stock_b', values='correlation')
    
    fig = px.imshow(corr_pivot, 
                    title="Stock Correlation Heatmap",
                    color_continuous_scale="RdBu_r",
                    aspect="auto")
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Diversification Insights")
    
    # Best diversification pairs (lowest correlation)
    best_diversification = correlation_data.nsmallest(5, 'correlation')
    st.write("**Best Diversification Pairs:**")
    st.dataframe(best_diversification[['stock_a', 'stock_b', 'correlation', 'correlation_strength']])
    
    # Highly correlated pairs
    high_correlation = correlation_data.nlargest(3, 'correlation')
    st.write("**Highly Correlated Pairs:**")
    st.dataframe(high_correlation[['stock_a', 'stock_b', 'correlation', 'correlation_strength']])