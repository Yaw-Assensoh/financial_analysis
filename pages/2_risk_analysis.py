import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Risk Analysis", layout="wide")
st.title(" Risk Analysis")

@st.cache_data
def load_data():
    volatility = pd.read_csv('data_outputs/volatility_results.csv')
    sharpe = pd.read_csv('data_outputs/sharp_ratio_results.csv')
    return volatility, sharpe

try:
    volatility, sharpe = load_data()
    
    st.subheader("Risk-Return Profile")
    
    # Merge data for scatter plot
    merged_data = volatility.merge(sharpe, on='ticker')
    sharpe_col = 'sharpe_ratio' if 'sharpe_ratio' in sharpe.columns else 'sharp_ratio'
    
    fig = px.scatter(merged_data, x='daily_volatility', y=sharpe_col,
                     size='daily_volatility', color='ticker',
                     title='Risk vs Return Analysis',
                     hover_data=['risk_adjusted_grade'])
    st.plotly_chart(fig, use_container_width=True)
    
    # HTML Visualization
    st.subheader("Interactive Risk Analysis")
    try:
        with open("visualizations/risk_return_profile.html", "r") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=600)
    except:
        st.info("Interactive risk visualization loading...")
    
    # Metrics
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Volatility Analysis")
        st.dataframe(volatility, use_container_width=True)
    
    with col2:
        st.subheader("Risk-Adjusted Returns")
        st.dataframe(sharpe, use_container_width=True)

except Exception as e:
    st.error(f"Error loading data: {e}")