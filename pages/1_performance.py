import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Performance Analysis", layout="wide")
st.title(" Performance Analysis")

@st.cache_data
def load_data():
    return pd.read_csv('data_outputs/market_performance.csv')

try:
    performance = load_data()
    
    # Header Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        top_performer = performance.loc[performance['total_return_percentage'].idxmax()]
        st.metric("🏆 Top Performer", top_performer['ticker'], f"{top_performer['total_return_percentage']:.1f}%")
    
    with col2:
        market = performance[performance['ticker'] == 'SPY']['total_return_percentage'].iloc[0]
        st.metric(" Market Return", f"{market:.1f}%")
    
    with col3:
        outperformers = len(performance[performance['total_return_percentage'] > market])
        st.metric("🚀 Beat Market", outperformers)
    
    with col4:
        avg_return = performance['total_return_percentage'].mean()
        st.metric(" Average Return", f"{avg_return:.1f}%")

    # Interactive Chart
    st.subheader("Total Returns 2020-2025")
    fig = px.bar(performance, x='ticker', y='total_return_percentage',
                 color='total_return_percentage',
                 color_continuous_scale='Viridis',
                 text_auto='.1f')
    fig.update_layout(height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # HTML Visualization
    st.subheader("Interactive Performance Analysis")
    try:
        with open("visualizations/interactive_performance.html", "r") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=600)
    except:
        st.info("Interactive visualization loading...")
    
    # Data Table
    st.subheader("Performance Data")
    st.dataframe(performance, use_container_width=True)

except Exception as e:
    st.error(f"Error loading data: {e}")
    