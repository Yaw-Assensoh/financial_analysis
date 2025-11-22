import pandas as pd
import streamlit as st

@st.cache_data
def load_performance_data():
    return pd.read_csv('../data_outputs/market_performance.csv')

@st.cache_data
def load_risk_data():
    volatility = pd.read_csv('../data_outputs/volatility_results.csv')
    sharpe = pd.read_csv('../data_outputs/sharp_ratio_results.csv')
    return volatility, sharpe

@st.cache_data
def load_correlation_data():
    return pd.read_csv('../data_outputs/stock_correlationscsv.csv')

@st.cache_data
def load_trends_data():
    monthly = pd.read_csv('../data_outputs/monthly_performance.csv')
    quarterly = pd.read_csv('../data_outputs/quarterly_returns.csv')
    extreme_days = pd.read_csv('../data_outputs/extreme_performace_days.csv')
    return monthly, quarterly, extreme_days

@st.cache_data
def load_technical_data():
    signals = pd.read_csv('../data_outputs/technical_signals.csv')
    volume = pd.read_csv('../data_outputs/high_volume_analysis.csv')
    return signals, volume

@st.cache_data
def load_quality_data():
    return pd.read_csv('../data_outputs/data_quality.csv')