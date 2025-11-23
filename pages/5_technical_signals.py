import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Technical Signals",
    layout="wide"
)

def main():
    st.title(" Technical Analysis & Trading Signals")
    st.markdown("---")
    
    st.write("""
    This section provides comprehensive technical analysis using multiple indicators and generates 
    actionable trading signals based on proven technical analysis methodologies.
    """)
    
    # Technical Signals Data
    technical_data = {
        'Ticker': ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY'],
        'RSI (14)': [58.2, 62.7, 45.3, 68.9, 52.1, 55.8],
        'MACD Signal': ['Bullish', 'Neutral', 'Bearish', 'Bullish', 'Neutral', 'Neutral'],
        'Moving Avg (50/200)': ['Above', 'Above', 'Below', 'Above', 'Above', 'Above'],
        'Bollinger Position': ['Upper', 'Middle', 'Lower', 'Upper', 'Middle', 'Middle'],
        'Support Level': [210.5, 135.2, 145.8, 335.4, 175.6, 435.2],
        'Resistance Level': [245.8, 152.7, 162.3, 368.9, 195.4, 465.8],
        'Volume Trend': ['Increasing', 'Neutral', 'Decreasing', 'Increasing', 'Neutral', 'Neutral'],
        'Overall Signal': ['BUY', 'HOLD', 'SELL', 'BUY', 'HOLD', 'HOLD']
    }
    
    tech_df = pd.DataFrame(technical_data)
    
    # Signal Overview
    st.header("🎯 Current Technical Signals Overview")
    
    # Create signal cards
    cols = st.columns(6)
    signal_colors = {'BUY': 'green', 'SELL': 'red', 'HOLD': 'orange'}
    
    for i, (_, row) in enumerate(tech_df.iterrows()):
        with cols[i]:
            color = signal_colors[row['Overall Signal']]
            st.markdown(f"""
            <div style='
                background-color: {color}20;
                border: 2px solid {color};
                border-radius: 10px;
                padding: 15px;
                text-align: center;
                margin: 5px;
            '>
                <h3 style='color: {color}; margin: 0;'>{row['Ticker']}</h3>
                <h2 style='color: {color}; margin: 10px 0;'>{row['Overall Signal']}</h2>
                <p style='margin: 5px 0; font-size: 12px;'>RSI: {row['RSI (14)']}</p>
                <p style='margin: 5px 0; font-size: 12px;'>{row['Moving Avg (50/200)']}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # RSI Analysis
    st.header("Relative Strength Index (RSI) Analysis")
    
    fig1, ax = plt.subplots(figsize=(12, 6))
    
    # Color code RSI values
    colors_rsi = []
    for rsi in tech_df['RSI (14)']:
        if rsi > 70:
            colors_rsi.append('red')  # Overbought
        elif rsi < 30:
            colors_rsi.append('green')  # Oversold
        else:
            colors_rsi.append('orange')  # Neutral
    
    bars = ax.bar(tech_df['Ticker'], tech_df['RSI (14)'], color=colors_rsi, alpha=0.8)
    
    # Add RSI reference lines
    ax.axhline(y=70, color='red', linestyle='--', alpha=0.7, label='Overbought (70)')
    ax.axhline(y=30, color='green', linestyle='--', alpha=0.7, label='Oversold (30)')
    ax.axhline(y=50, color='gray', linestyle='-', alpha=0.5, label='Neutral (50)')
    
    ax.set_title('Relative Strength Index (RSI) - 14 Period', fontweight='bold', fontsize=14)
    ax.set_ylabel('RSI Value')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{height:.1f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    st.pyplot(fig1)
    
    # Moving Average Analysis
    st.header(" Moving Average Analysis")
    
    fig2, ax = plt.subplots(figsize=(12, 6))
    
    # Generate sample price and moving average data
    days = 100
    dates = [datetime.now() - timedelta(days=x) for x in range(days)][::-1]
    
    # Sample price data with trends
    np.random.seed(42)
    prices = 100 + np.cumsum(np.random.randn(days) * 2)
    ma_50 = pd.Series(prices).rolling(50).mean()
    ma_200 = pd.Series(prices).rolling(200).mean()
    
    # Trim to available data
    valid_dates = dates[199:]
    valid_prices = prices[199:]
    valid_ma_50 = ma_50[199:]
    valid_ma_200 = ma_200[199:]
    
    ax.plot(valid_dates, valid_prices, label='Price', linewidth=2, color='blue')
    ax.plot(valid_dates, valid_ma_50, label='50-Day MA', linewidth=2, color='orange')
    ax.plot(valid_dates, valid_ma_200, label='200-Day MA', linewidth=2, color='red')
    
    ax.set_title('Price vs Moving Averages (Sample Data)', fontweight='bold', fontsize=14)
    ax.set_ylabel('Price')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    st.pyplot(fig2)
    
    # Technical Indicators Table
    st.header(" Comprehensive Technical Indicators")
    
    # Color the dataframe
    def color_signal(val):
        if val == 'BUY': return 'background-color: #90EE90'
        elif val == 'SELL': return 'background-color: #FFB6C1'
        elif val == 'HOLD': return 'background-color: #FFFACD'
        return ''
    
    def color_macd(val):
        if val == 'Bullish': return 'background-color: #90EE90'
        elif val == 'Bearish': return 'background-color: #FFB6C1'
        return 'background-color: #FFFACD'
    
    styled_df = tech_df.style.applymap(color_signal, subset=['Overall Signal'])\
                            .applymap(color_macd, subset=['MACD Signal'])
    
    st.dataframe(styled_df, use_container_width=True, hide_index=True)
    
    # Support and Resistance Analysis
    st.header("🛡️ Support & Resistance Levels")
    
    fig3, ax = plt.subplots(figsize=(12, 6))
    
    x_pos = np.arange(len(tech_df))
    width = 0.35
    
    bars1 = ax.bar(x_pos - width/2, tech_df['Support Level'], width, 
                  label='Support', color='green', alpha=0.7)
    bars2 = ax.bar(x_pos + width/2, tech_df['Resistance Level'], width, 
                  label='Resistance', color='red', alpha=0.7)
    
    ax.set_xlabel('Ticker')
    ax.set_ylabel('Price Level')
    ax.set_title('Key Support & Resistance Levels', fontweight='bold', fontsize=14)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(tech_df['Ticker'])
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 5,
                   f'{height:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    st.pyplot(fig3)
    
    # Trading Signals Breakdown
    st.header(" Detailed Signal Analysis")
    
    for _, row in tech_df.iterrows():
        with st.expander(f" {row['Ticker']} - {row['Overall Signal']} Signal", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Indicator Status")
                st.write(f"**RSI (14):** {row['RSI (14)']}")
                st.write(f"**MACD:** {row['MACD Signal']}")
                st.write(f"**Moving Averages:** {row['Moving Avg (50/200)']}")
                st.write(f"**Bollinger Band:** {row['Bollinger Position']}")
                st.write(f"**Volume Trend:** {row['Volume Trend']}")
            
            with col2:
                st.subheader("Key Levels")
                st.write(f"**Support:** {row['Support Level']}")
                st.write(f"**Resistance:** {row['Resistance Level']}")
                st.write(f"**Signal Strength:** {'Strong' if row['Overall Signal'] != 'HOLD' else 'Weak'}")
                
                # Signal reasoning
                if row['Overall Signal'] == 'BUY':
                    st.success("**Rationale:** Multiple bullish indicators aligning")
                elif row['Overall Signal'] == 'SELL':
                    st.error("**Rationale:** Bearish momentum and weak technicals")
                else:
                    st.warning("**Rationale:** Mixed signals, awaiting clarity")
    
    # Market Sentiment & Recommendations
    st.header("Trading Recommendations & Market Outlook")
    
    recommendation_col1, recommendation_col2 = st.columns(2)
    
    with recommendation_col1:
        st.success("""
        **🟢 Strong Buy Signals:**
        - **TSLA**: Bullish RSI, above moving averages, strong volume
        - **MSFT**: Positive MACD, support levels holding, institutional accumulation
        
        **Key Actions:**
        - Consider entry on pullbacks to support
        - Implement trailing stops for risk management
        - Monitor earnings and fundamental catalysts
        """)
    
    with recommendation_col2:
        st.error("""
        **🔴 Caution Required:**
        - **AMZN**: Bearish MACD, below key moving averages
        - Watch for breakdown below support levels
        
        **Risk Management:**
        - Avoid new long positions in bearish signals
        - Consider hedging strategies
        - Wait for technical confirmation of reversal
        """)
    
    # Technical Strategy Framework
    st.header("🛠️ Technical Trading Framework")
    
    st.info("""
    **Trading Strategy Implementation:**
    
    1. **Entry Criteria**:
       - RSI between 30-70 (avoid extremes)
       - Moving average alignment (50 > 200 for bullish)
       - MACD bullish crossover confirmation
       - Volume confirmation of price moves
    
    2. **Exit Strategy**:
       - RSI > 70 (overbought) for profit taking
       - Moving average breakdown for stop-loss
       - Support level breach for risk management
       - Target: 2:1 reward-to-risk ratio minimum
    
    3. **Position Management**:
       - Scale-in approach for entries
       - Dynamic stop-loss adjustment
       - Regular technical review (weekly)
       - Correlation consideration for portfolio impact
    """)

if __name__ == "__main__":
    main()