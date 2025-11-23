import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Technical Analysis",
    layout="wide"
)

def main():
    st.title("Technical Analysis")
    st.markdown("---")
    
    st.write("Technical indicators and market signal analysis.")
    
    # Technical data
    tech_data = {
        'Ticker': ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY'],
        'RSI': [45.2, 52.8, 38.7, 58.9, 49.3, 53.1],
        'Trend': ['Neutral', 'Bullish', 'Bearish', 'Bullish', 'Neutral', 'Neutral'],
        '50D vs 200D MA': ['Above', 'Above', 'Below', 'Above', 'Above', 'Above'],
        'Signal': ['Hold', 'Buy', 'Sell', 'Buy', 'Hold', 'Hold']
    }
    
    tech_df = pd.DataFrame(tech_data)
    
    # Signal Overview
    st.subheader("Current Signals")
    
    cols = st.columns(6)
    for i, (_, row) in enumerate(tech_df.iterrows()):
        with cols[i]:
            signal_color = {'Buy': 'green', 'Sell': 'red', 'Hold': 'gray'}[row['Signal']]
            st.metric(
                label=row['Ticker'],
                value=row['Signal'],
                delta=f"RSI: {row['RSI']}"
            )
    
    # RSI Analysis
    st.subheader("RSI Analysis")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    colors = ['red' if rsi > 70 else 'green' if rsi < 30 else 'steelblue' 
             for rsi in tech_df['RSI']]
    
    bars = ax.bar(tech_df['Ticker'], tech_df['RSI'], color=colors, alpha=0.7)
    
    ax.axhline(y=70, color='red', linestyle='--', alpha=0.7, label='Overbought')
    ax.axhline(y=30, color='green', linestyle='--', alpha=0.7, label='Oversold')
    ax.axhline(y=50, color='gray', linestyle='-', alpha=0.5)
    
    ax.set_ylabel('RSI Value')
    ax.set_title('Relative Strength Index (14-period)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 1,
                f'{height:.1f}', ha='center', va='bottom')
    
    st.pyplot(fig)
    
    # Moving Average Analysis
    st.subheader("Trend Analysis")
    
    trend_summary = pd.crosstab(tech_df['50D vs 200D MA'], tech_df['Trend'])
    st.dataframe(trend_summary, use_container_width=True)
    
    # Detailed Technical Table
    st.subheader("Technical Indicators")
    st.dataframe(tech_df, use_container_width=True, hide_index=True)
    
    # Trading Signals
    st.subheader("Trading Recommendations")
    
    buy_signals = tech_df[tech_df['Signal'] == 'Buy']
    sell_signals = tech_df[tech_df['Signal'] == 'Sell']
    
    col1, col2 = st.columns(2)
    
    with col1:
        if not buy_signals.empty:
            st.write("**Buy Recommendations:**")
            for _, stock in buy_signals.iterrows():
                st.write(f"- {stock['Ticker']}: RSI {stock['RSI']}, Trend: {stock['Trend']}")
        else:
            st.write("No strong buy signals at this time.")
    
    with col2:
        if not sell_signals.empty:
            st.write("**Sell Recommendations:**")
            for _, stock in sell_signals.iterrows():
                st.write(f"- {stock['Ticker']}: RSI {stock['RSI']}, Trend: {stock['Trend']}")
        else:
            st.write("No sell signals at this time.")
    
    # Market Outlook
    st.subheader("Market Outlook")
    
    bullish_count = len(tech_df[tech_df['Trend'] == 'Bullish'])
    bearish_count = len(tech_df[tech_df['Trend'] == 'Bearish'])
    
    if bullish_count > bearish_count:
        st.info("Overall market bias: **Bullish**")
        st.write("Majority of securities show positive momentum and trend alignment.")
    elif bearish_count > bullish_count:
        st.warning("Overall market bias: **Bearish**")
        st.write("Caution advised as several securities show negative momentum.")
    else:
        st.info("Overall market bias: **Neutral**")
        st.write("Mixed signals across the universe, suggesting range-bound conditions.")

if __name__ == "__main__":
    main()