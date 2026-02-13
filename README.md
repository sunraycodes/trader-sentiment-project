# Trader Behavior vs Market Sentiment

This research investigates the differences in the performance and activities of traders during different market sentiment phases, namely Fear, Neutral, and Greed, using historical trading data and a sentiment index. It combines data analysis, feature development, segmentation, clustering, and a simple predictive model, and it also includes an interactive dashboard using Streamlit.

---

##  Project Overview

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

##  Key Insights

- There is large performance variation across regimes of sentiment, with Greed corresponding to greater drawdowns and Extreme Greed to greater win rates.
- Trader behavior, including trade frequency, size, and long vs. short positions, varies in a systematic fashion with sentiment.
- Frequent traders and traders with large positions perform much better than infrequent and small-position traders.
- Clustering reveals three types: conservative/consistent, low-activity/low-edge, and aggressive high-risk/high-reward traders.

---

##  Strategy Recommendations

1. **Adaptive Risk by Sentiment and Trader Type**  
   Reduce risk exposure for high-risk segments during Greed regimes and allow moderate risk expansion during
   Extreme Greed periods.

2. **Activity and Position Sizing Filters**  
   Restrict trading during Extreme Fear to higher-performing segments and cap trade frequency. During Fear,
   allow larger positions selectively for traders with stronger historical win rates.

---

##  Repository Structure
```bash
trader-sentiment-project/
├── Data_intern_project.ipynb # Main analysis notebook
├── app.py # Streamlit dashboard
├── clean_daily_metrics.csv # Processed dataset used by the dashboard
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

---

##  Setup Instructions

1. Clone the repository:
```
    git clone https://github.com/your-username/trader-sentiment-project.git
    cd trader-sentiment-project
```
2. Install dependencies:
```
    pip install -r requirements.txt
```
3. Run the Jupyter notebook:
```
    jupyter notebook Data_intern_project.ipynb
```

5. Run the Streamlit dashboard:
```
    streamlit run app.py
```


Created  By Samruddhi Amol Shah
