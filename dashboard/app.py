import streamlit as st

st.set_page_config(
    page_title="Stock Analysis Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title(" Stock Market Analysis Dashboard")
st.markdown("""
### Comprehensive Analysis of 6 Major Stocks (2020-2025)
This interactive dashboard presents insights from SQL analysis of stock performance, risk, and correlations.

**Navigate using the sidebar →**
""")

st.sidebar.success("Select a page above.")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | Data Source: Nasdaq | Analysis: PostgreSQL")