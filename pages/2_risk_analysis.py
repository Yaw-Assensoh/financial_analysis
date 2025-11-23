import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Risk Analysis", layout="wide")
st.title(" Risk Analysis")

@st.cache_data
def load_risk_data():
    volatility = pd.read_csv('../data_outputs/volatility_results.csv')
    sharpe = pd.read_csv('../data_outputs/sharpe_ratio_results.csv')
    return volatility, sharpe

volatility, sharpe = load_risk_data()

tab1, tab2, tab3 = st.tabs(["Volatility", "Risk-Adjusted Returns", "Comparison"])

with tab1:
    st.subheader("Daily Volatility Analysis")
    fig = px.bar(volatility, x='ticker', y='daily_volatility',
                 title='Stock Volatility (Standard Deviation of Daily Returns)')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Sharpe Ratio - Risk Adjusted Returns")
    fig = px.bar(sharpe, x='ticker', y='sharpe_ratio',
                 title='Sharpe Ratio (Higher = Better Risk-Adjusted Returns)',
                 color='risk_adjusted_grade')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Risk-Return Profile")
    merged = volatility.merge(sharpe, on='ticker')
    fig = px.scatter(merged, x='daily_volatility', y='sharpe_ratio',
                     size='daily_volatility', color='ticker',
                     title='Risk vs Return Analysis',
                     hover_data=['risk_adjusted_grade'])
    st.plotly_chart(fig, use_container_width=True)