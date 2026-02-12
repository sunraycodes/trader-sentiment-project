# Trader Behavior vs Market Sentiment

This project analyzes how trader performance and behavior change across different market sentiment regimes
(Fear, Neutral, Greed) using historical trading data and a sentiment index. It combines data analysis,
feature engineering, segmentation, clustering, and a simple predictive model, and includes an interactive
Streamlit dashboard for exploration.

---

## 📌 Project Overview

We:
- Clean and align sentiment and trade data at the daily level
- Engineer key metrics:
  - Daily PnL
  - Trade count
  - Average trade size (USD)
  - Win rate
  - Long/short ratio
- Analyze:
  - Performance differences across sentiment regimes
  - Behavior changes with sentiment
- Build trader segments:
  - Frequent vs Infrequent traders
  - Consistent vs Inconsistent traders
  - Large vs Small position size traders
- Cluster traders into behavioral archetypes using KMeans
- Train a simple predictive model to predict next-day profitability
- Build a Streamlit dashboard to explore results interactively

---

## 🧠 Key Insights

- Performance differs significantly across sentiment regimes, with Greed showing deeper drawdowns and
  Extreme Greed showing higher win rates.
- Trader behavior (trade frequency, position size, long/short bias) changes systematically with sentiment.
- Frequent traders and large-size traders strongly outperform infrequent and small-size traders.
- Clustering reveals three archetypes: conservative/consistent, low-activity low-edge, and aggressive
  high-risk/high-reward traders.

---

## 🧭 Strategy Recommendations

1. **Adaptive Risk by Sentiment and Trader Type**  
   Reduce risk exposure for high-risk segments during Greed regimes and allow moderate risk expansion during
   Extreme Greed periods.

2. **Activity and Position Sizing Filters**  
   Restrict trading during Extreme Fear to higher-performing segments and cap trade frequency. During Fear,
   allow larger positions selectively for traders with stronger historical win rates.

---

## 📂 Repository Structure

