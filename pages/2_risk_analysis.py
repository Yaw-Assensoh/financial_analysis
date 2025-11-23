import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Correlation Analysis",
    layout="wide"
)

def main():
    st.title(" Correlation & Diversification Analysis")
    st.markdown("---")
    
    st.write("""
    This section analyzes inter-security correlations and diversification benefits. 
    Understanding correlation patterns is essential for effective portfolio construction and risk management.
    """)
    
    # Generate correlation matrix
    tickers = ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY']
    
    # Realistic correlation matrix (based on typical tech stock correlations)
    correlation_matrix = np.array([
        [1.00, 0.65, 0.62, 0.58, 0.61, 0.72],  # TSLA
        [0.65, 1.00, 0.78, 0.75, 0.74, 0.85],  # GOOGL
        [0.62, 0.78, 1.00, 0.72, 0.70, 0.82],  # AMZN
        [0.58, 0.75, 0.72, 1.00, 0.68, 0.88],  # MSFT
        [0.61, 0.74, 0.70, 0.68, 1.00, 0.80],  # AAPL
        [0.72, 0.85, 0.82, 0.88, 0.80, 1.00]   # SPY
    ])
    
    corr_df = pd.DataFrame(correlation_matrix, index=tickers, columns=tickers)
    
    # Correlation Overview
    st.header(" Correlation Matrix Overview")
    
    # Create heatmap
    fig1, ax = plt.subplots(figsize=(10, 8))
    
    mask = np.triu(np.ones_like(corr_df, dtype=bool))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    
    sns.heatmap(corr_df, mask=mask, cmap=cmap, vmax=1.0, vmin=0.4, 
                center=0.7, annot=True, fmt='.2f',
                square=True, linewidths=0.5, cbar_kws={"shrink": 0.8})
    
    ax.set_title('Security Correlation Matrix\n(Daily Returns Correlation)', 
                 fontweight='bold', fontsize=16, pad=20)
    plt.tight_layout()
    st.pyplot(fig1)
    
    # Correlation Statistics
    st.header(" Correlation Statistics & Insights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_correlation = np.mean(correlation_matrix[np.triu_indices(6, k=1)])
        st.metric("Average Correlation", f"{avg_correlation:.3f}", "High")
    
    with col2:
        min_correlation = np.min(correlation_matrix[np.triu_indices(6, k=1)])
        st.metric("Lowest Correlation", f"{min_correlation:.3f}", "TSLA-MSFT")
    
    with col3:
        max_correlation = np.max(correlation_matrix[np.triu_indices(6, k=1)])
        st.metric("Highest Correlation", f"{max_correlation:.3f}", "MSFT-SPY")
    
    # Pairwise Correlation Analysis
    st.header(" Detailed Pairwise Analysis")
    
    # Extract pairwise correlations
    pairs = []
    correlations = []
    
    for i in range(len(tickers)):
        for j in range(i+1, len(tickers)):
            pairs.append(f"{tickers[i]}-{tickers[j]}")
            correlations.append(correlation_matrix[i, j])
    
    pair_df = pd.DataFrame({
        'Pair': pairs,
        'Correlation': correlations,
        'Strength': ['Very High' if c > 0.8 else 'High' if c > 0.6 else 'Moderate' for c in correlations]
    }).sort_values('Correlation', ascending=False)
    
    # Display top and bottom correlations
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(" Highest Correlations")
        st.dataframe(pair_df.head(6), use_container_width=True, hide_index=True)
    
    with col2:
        st.subheader(" Lowest Correlations")
        st.dataframe(pair_df.tail(6), use_container_width=True, hide_index=True)
    
    # Correlation Distribution
    st.header(" Correlation Distribution Analysis")
    
    fig2, ax = plt.subplots(figsize=(12, 6))
    
    # Plot correlation distribution
    upper_triangular = correlation_matrix[np.triu_indices(6, k=1)]
    
    ax.hist(upper_triangular, bins=10, alpha=0.7, color='skyblue', edgecolor='black')
    ax.axvline(np.mean(upper_triangular), color='red', linestyle='--', 
               linewidth=2, label=f'Mean: {np.mean(upper_triangular):.3f}')
    
    ax.set_xlabel('Correlation Coefficient', fontweight='bold')
    ax.set_ylabel('Frequency', fontweight='bold')
    ax.set_title('Distribution of Pairwise Correlations', fontweight='bold', fontsize=14)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    st.pyplot(fig2)
    
    # Diversification Benefits
    st.header("🎯 Diversification Analysis")
    
    diversification_metrics = {
        'Ticker': tickers,
        'Avg Correlation with Peers': [np.mean([correlation_matrix[i, j] for j in range(6) if j != i]) 
                                      for i in range(6)],
        'Diversification Score': [1 - np.mean([correlation_matrix[i, j] for j in range(6) if j != i]) 
                                for i in range(6)],
        'Market Correlation': [correlation_matrix[i, 5] for i in range(6)]  # SPY is index 5
    }
    
    div_df = pd.DataFrame(diversification_metrics)
    
    fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Diversification Score
    colors_div = ['green' if score > 0.35 else 'orange' for score in div_df['Diversification Score']]
    bars1 = ax1.bar(div_df['Ticker'], div_df['Diversification Score'], color=colors_div, alpha=0.8)
    ax1.set_title('Diversification Score\n(Higher = Better Diversification)', fontweight='bold')
    ax1.set_ylabel('Diversification Score')
    ax1.grid(True, alpha=0.3)
    
    for bar in bars1:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.2f}', ha='center', va='bottom', fontweight='bold')
    
    # Market Correlation
    colors_mkt = ['red' if corr > 0.8 else 'orange' for corr in div_df['Market Correlation']]
    bars2 = ax2.bar(div_df['Ticker'], div_df['Market Correlation'], color=colors_mkt, alpha=0.8)
    ax2.axhline(y=1.0, color='red', linestyle='--', alpha=0.5, label='Perfect Correlation')
    ax2.set_title('Correlation with Market (SPY)', fontweight='bold')
    ax2.set_ylabel('Correlation Coefficient')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    for bar in bars2:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.01,
                f'{height:.2f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    st.pyplot(fig3)
    
    # Portfolio Construction Insights
    st.header(" Portfolio Construction Insights")
    
    insight_col1, insight_col2 = st.columns(2)
    
    with insight_col1:
        st.success("""
        **🟢 Diversification Opportunities:**
        - TSLA shows relatively lower average correlation
        - Technology subsector variations provide some diversification
        - Consider adding non-tech assets for better diversification
        - International exposure could further reduce correlations
        """)
    
    with insight_col2:
        st.warning("""
        **🔴 Concentration Risks:**
        - High overall correlation within technology sector
        - Strong market beta across all holdings
        - Limited diversification within current universe
        - Sector-specific risk remains elevated
        """)
    
    # Advanced Correlation Analysis
    st.header(" Advanced Correlation Metrics")
    
    st.subheader("Correlation Clustering")
    
    # Create clustered heatmap
    fig4, ax = plt.subplots(figsize=(10, 8))
    
    g = sns.clustermap(corr_df, cmap=cmap, annot=True, fmt='.2f',
                      figsize=(10, 8), center=0.7)
    g.ax_heatmap.set_title('Hierarchically Clustered Correlation Matrix', 
                          fontweight='bold', fontsize=14, pad=20)
    
    st.pyplot(g.fig)
    
    # Correlation Strategy Recommendations
    st.header("🎯 Strategic Recommendations")
    
    st.info("""
    **Portfolio Optimization Strategies:**
    
    1. **Diversification Enhancement**:
       - Add assets with correlation < 0.5 to current holdings
       - Consider different sectors (Healthcare, Utilities, Consumer Staples)
       - Explore international markets for geographic diversification
    
    2. **Risk Management**:
       - Monitor correlation changes during market stress
       - Implement dynamic correlation-based position sizing
       - Use correlation analysis for hedge ratio calculations
    
    3. **Rebalancing Framework**:
       - Quarterly correlation review and portfolio rebalancing
       - Correlation threshold-based rebalancing triggers
       - Sector rotation based on correlation patterns
    """)

if __name__ == "__main__":
    main()