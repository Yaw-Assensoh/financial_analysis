import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Technical Signals", layout="wide")
st.title("⚡ Technical Trading Signals")

@st.cache_data
def load_technical_data():
    signals = pd.read_csv('../data_outputs/technical_signals.csv')
    volume = pd.read_csv('../data_outputs/high_volume_analysis.csv')
    return signals, volume

signals, volume = load_technical_data()

col1, col2 = st.columns(2)

with col1:
    st.subheader("Moving Average Signals")
    
    # Recent signals
    recent_signals = signals.head(10)
    st.dataframe(recent_signals, use_container_width=True)
    
    # Signal summary
    signal_counts = signals['signal'].value_counts()
    fig = px.pie(values=signal_counts.values, names=signal_counts.index,
                 title="Signal Distribution")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("High Volume Analysis")
    
    st.write("**Recent High Volume Days:**")
    recent_volume = volume.head(10)
    st.dataframe(recent_volume[['ticker', 'date', 'volume_ratio', 'volume_z_score']])
    
    # Volume analysis by stock
    volume_by_stock = volume.groupby('ticker').size().reset_index(name='high_volume_days')
    fig = px.bar(volume_by_stock, x='ticker', y='high_volume_days',
                 title="High Volume Days by Stock")
    st.plotly_chart(fig, use_container_width=True)