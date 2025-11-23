import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Risk Analysis",
    layout="wide"
)

def main():
    st.title("Risk Analysis")
    st.markdown("---")
    
    st.write("Comprehensive risk assessment and volatility analysis for portfolio management.")
    
    # Risk metrics data
    risk_data = {
        'Ticker': ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY'],
        'Volatility (%)': [52.3, 28.7, 32.1, 24.5, 26.8, 18.2],
        'Beta': [2.10, 1.05, 1.04, 0.98, 1.21, 1.00],
        'Max Drawdown (%)': [-45.2, -28.7, -35.1, -22.4, -31.5, -19.8],
        'Sharpe Ratio': [0.65, 1.02, 0.79, 1.15, 0.94, 0.82],
        'VaR (95%)': [-12.3, -6.9, -8.2, -5.8, -7.1, -4.5]
    }
    
    risk_df = pd.DataFrame(risk_data)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_vol = risk_df['Volatility (%)'].mean()
        st.metric("Average Volatility", f"{avg_vol:.1f}%")
    
    with col2:
        high_beta = risk_df.loc[risk_df['Beta'].idxmax(), 'Ticker']
        st.metric("Highest Beta", high_beta, "2.10")
    
    with col3:
        best_sharpe = risk_df.loc[risk_df['Sharpe Ratio'].idxmax(), 'Ticker']
        st.metric("Best Risk-Adjusted", best_sharpe, "1.15")
    
    with col4:
        worst_dd = risk_df['Max Drawdown (%)'].min()
        st.metric("Worst Drawdown", f"{worst_dd:.1f}%")
    
    # Volatility Analysis
    st.subheader("Volatility Comparison")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    
    bars = ax.bar(risk_df['Ticker'], risk_df['Volatility (%)'], 
                 color='steelblue', alpha=0.7)
    
    ax.axhline(y=18.2, color='red', linestyle='--', label='Market Volatility')
    ax.set_ylabel('Annual Volatility (%)')
    ax.set_title('Historical Volatility Analysis')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, height + 1,
                f'{height:.1f}%', ha='center', va='bottom')
    
    st.pyplot(fig)
    
    # Risk-Return Scatter
    st.subheader("Risk-Return Profile")
    
    returns = [343.9, 251.0, 210.4, 158.0, 141.8, 100.0]
    
    fig2, ax = plt.subplots(figsize=(10, 6))
    
    scatter = ax.scatter(risk_df['Volatility (%)'], returns, 
                        s=risk_df['Beta'] * 100, alpha=0.7)
    
    for i, ticker in enumerate(risk_df['Ticker']):
        ax.annotate(ticker, (risk_df['Volatility (%)'][i], returns[i]),
                   xytext=(5, 5), textcoords='offset points')
    
    ax.set_xlabel('Volatility (%)')
    ax.set_ylabel('Total Return (%)')
    ax.set_title('Risk-Return Analysis')
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig2)
    
    # Detailed Metrics Table
    st.subheader("Risk Metrics Table")
    st.dataframe(risk_df, use_container_width=True, hide_index=True)
    
    # Risk Insights
    st.subheader("Risk Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Lower Risk Profile:**")
        st.write("- MSFT: Strong risk-adjusted returns")
        st.write("- GOOGL: Moderate volatility with good returns")
        st.write("- SPY: Market-level risk characteristics")
    
    with col2:
        st.write("**Higher Risk Considerations:**")
        st.write("- TSLA: High volatility and beta")
        st.write("- AMZN: Significant drawdown potential")
        st.write("- Sector concentration risk")

if __name__ == "__main__":
    main()