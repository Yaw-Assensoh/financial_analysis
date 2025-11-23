import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Correlation Analysis", layout="wide")
st.title(" Correlation Analysis")

@st.cache_data
def load_data():
    return pd.read_csv('data_outputs/stock_correlationscsv.csv')

try:
    correlation = load_data()
    
    st.subheader("Stock Correlation Matrix")
    
    # Create correlation matrix
    if 'stock_a' in correlation.columns and 'stock_b' in correlation.columns:
        corr_matrix = correlation.pivot(index='stock_a', columns='stock_b', values='correlation')
    else:
        corr_matrix = correlation.pivot(index=correlation.columns[0], 
                                      columns=correlation.columns[1], 
                                      values=correlation.columns[2])
    
    # Plotly heatmap
    fig = px.imshow(corr_matrix, 
                    title="Stock Correlation Heatmap",
                    color_continuous_scale="RdBu_r",
                    aspect="auto")
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
    
    # HTML Visualization
    st.subheader("Interactive Correlation Network")
    try:
        with open("visualizations/correlation_network.html", "r") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=600)
    except:
        st.info("Interactive correlation visualization loading...")
    
    # Insights
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Best Diversification Pairs")
        low_corr = correlation.nsmallest(5, 'correlation')
        st.dataframe(low_corr, use_container_width=True)
    
    with col2:
        st.subheader("Highly Correlated Pairs")
        high_corr = correlation.nlargest(5, 'correlation')
        st.dataframe(high_corr, use_container_width=True)

except Exception as e:
    st.error(f"Error loading data: {e}")