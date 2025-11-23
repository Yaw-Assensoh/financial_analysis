import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Trends & Patterns", layout="wide")
st.title(" Trends & Patterns")

@st.cache_data
def load_trends_data():
    monthly = pd.read_csv('../data_outputs/monthly_performance.csv')
    quarterly = pd.read_csv('../data_outputs/quarterly_returns.csv')
    extreme_days = pd.read_csv('../data_outputs/extreme_performance_days.csv')
    return monthly, quarterly, extreme_days

monthly, quarterly, extreme_days = load_trends_data()

tab1, tab2, tab3 = st.tabs(["Monthly Trends", "Quarterly Performance", "Extreme Days"])

with tab1:
    st.subheader("Monthly Performance Patterns")
    
    selected_stock = st.selectbox("Select Stock:", monthly['ticker'].unique())
    stock_data = monthly[monthly['ticker'] == selected_stock]
    
    fig = px.line(stock_data, x='month_name', y='avg_return_pct',
                  title=f'{selected_stock} - Average Monthly Returns',
                  markers=True)
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Quarterly Performance Analysis")
    
    fig = px.box(quarterly, x='ticker', y='quarterly_return_pct',
                 title='Quarterly Return Distribution by Stock')
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.subheader("Best & Worst Performing Days")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Best Single Days:**")
        best_days = extreme_days[extreme_days['performance_type'] == 'BEST DAY']
        st.dataframe(best_days.nlargest(5, 'daily_change_pct'))
    
    with col2:
        st.write("**Worst Single Days:**")
        worst_days = extreme_days[extreme_days['performance_type'] == 'WORST DAY']
        st.dataframe(worst_days.nsmallest(5, 'daily_change_pct'))