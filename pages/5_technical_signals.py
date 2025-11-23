import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Technical Signals", layout="wide")
st.title(" Technical Signals")

@st.cache_data
def load_data():
    signals = pd.read_csv('data_outputs/technical_signals.csv')
    volume = pd.read_csv('data_outputs/high_volume_analysis.csv')
    return signals, volume

try:
    signals, volume = load_data()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Recent Trading Signals")
        
        if not signals.empty:
            fig = px.scatter(signals.head(20), x='date', y='ticker',
                             color='signal',
                             title='Recent Trading Signals Timeline',
                             hover_data=['price', 'moving_avg_50', 'moving_avg_200'])
            st.plotly_chart(fig, use_container_width=True)
            
            st.subheader("Signal Summary")
            signal_counts = signals['signal'].value_counts()
            fig_pie = px.pie(values=signal_counts.values, names=signal_counts.index,
                             title="Signal Distribution")
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.info("No trading signals data available")
    
    with col2:
        st.subheader("High Volume Analysis")
        
        if not volume.empty:
            st.dataframe(volume.head(10), use_container_width=True)
            
            volume_by_stock = volume.groupby('ticker').size().reset_index(name='high_volume_days')
            fig_vol = px.bar(volume_by_stock, x='ticker', y='high_volume_days',
                             title="High Volume Days by Stock")
            st.plotly_chart(fig_vol, use_container_width=True)
        else:
            st.info("No volume analysis data available")
    
    # HTML Visualization
    st.subheader("Interactive Trading Signals")
    try:
        with open("visualizations/trading_signals.html", "r") as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=600)
    except:
        st.info("Interactive trading signals visualization loading...")

except Exception as e:
    st.error(f"Error loading data: {e}")