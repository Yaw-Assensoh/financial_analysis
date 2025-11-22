import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Performance Analysis", layout="wide")
st.title(" Performance Analysis")

# Load data
@st.cache_data
def load_performance_data():
    return pd.read_csv('../data_outputs/market_performance.csv')

performance = load_performance_data()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Total Returns (2020-2025)")
    fig = px.bar(performance, x='ticker', y='total_return_percentage',
                 title='Stock Performance vs Market Benchmark',
                 color='total_return_percentage',
                 color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Performance Summary")
    st.dataframe(performance, use_container_width=True)
    
    # Key insights
    best_performer = performance.loc[performance['total_return_percentage'].idxmax()]
    st.metric(
        label="🏆 Best Performer", 
        value=best_performer['ticker'],
        delta=f"{best_performer['total_return_percentage']:.1f}%"
    )