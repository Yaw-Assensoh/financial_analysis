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
    st.title("Correlation Analysis")
    st.markdown("---")
    
    st.write("Analysis of inter-security relationships and diversification potential.")
    
    # Correlation matrix data
    tickers = ['TSLA', 'GOOGL', 'AMZN', 'MSFT', 'AAPL', 'SPY']
    
    correlation_matrix = np.array([
        [1.00, 0.65, 0.62, 0.58, 0.61, 0.72],
        [0.65, 1.00, 0.78, 0.75, 0.74, 0.85],
        [0.62, 0.78, 1.00, 0.72, 0.70, 0.82],
        [0.58, 0.75, 0.72, 1.00, 0.68, 0.88],
        [0.61, 0.74, 0.70, 0.68, 1.00, 0.80],
        [0.72, 0.85, 0.82, 0.88, 0.80, 1.00]
    ])
    
    corr_df = pd.DataFrame(correlation_matrix, index=tickers, columns=tickers)
    
    # Correlation Heatmap
    st.subheader("Correlation Matrix")
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    sns.heatmap(corr_df, annot=True, cmap='coolwarm', center=0, 
                square=True, fmt='.2f', cbar_kws={"shrink": .8})
    
    ax.set_title('Security Correlation Matrix')
    st.pyplot(fig)
    
    # Correlation Statistics
    st.subheader("Correlation Statistics")
    
    # Calculate statistics
    upper_tri = correlation_matrix[np.triu_indices_from(correlation_matrix, k=1)]
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_corr = np.mean(upper_tri)
        st.metric("Average Correlation", f"{avg_corr:.3f}")
    
    with col2:
        min_corr = np.min(upper_tri)
        st.metric("Minimum Correlation", f"{min_corr:.3f}")
    
    with col3:
        max_corr = np.max(upper_tri)
        st.metric("Maximum Correlation", f"{max_corr:.3f}")
    
    # Pairwise Analysis
    st.subheader("Pairwise Correlations")
    
    # Get top and bottom correlations
    pairs = []
    corr_values = []
    
    for i in range(len(tickers)):
        for j in range(i+1, len(tickers)):
            pairs.append(f"{tickers[i]} - {tickers[j]}")
            corr_values.append(correlation_matrix[i,j])
    
    pair_df = pd.DataFrame({'Pair': pairs, 'Correlation': corr_values})
    pair_df = pair_df.sort_values('Correlation', ascending=False)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Highest Correlations:**")
        st.dataframe(pair_df.head(5), use_container_width=True, hide_index=True)
    
    with col2:
        st.write("**Lowest Correlations:**")
        st.dataframe(pair_df.tail(5), use_container_width=True, hide_index=True)
    
    # Diversification Analysis
    st.subheader("Diversification Assessment")
    
    # Calculate average correlation for each stock
    avg_correlations = []
    for i in range(len(tickers)):
        other_corrs = [correlation_matrix[i,j] for j in range(len(tickers)) if j != i]
        avg_correlations.append(np.mean(other_corrs))
    
    diversification_df = pd.DataFrame({
        'Ticker': tickers,
        'Avg Correlation': avg_correlations,
        'Diversification Potential': [1 - corr for corr in avg_correlations]
    })
    
    st.dataframe(diversification_df, use_container_width=True, hide_index=True)
    
    # Insights
    st.subheader("Portfolio Insights")
    
    st.write("""
    **Key Observations:**
    - High overall correlation within technology sector (0.65-0.85 range)
    - SPY shows strong correlation with all individual securities
    - TSLA demonstrates relatively lower average correlation
    - Limited diversification benefits within current universe
    
    **Recommendations:**
    - Consider adding non-correlated assets (bonds, commodities, international)
    - Monitor correlation changes during market stress periods
    - Implement sector rotation strategies for diversification
    """)

if __name__ == "__main__":
    main()