import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_daily_metrics.csv")

st.title("Trader Behavior vs Market Sentiment Dashboard")

sentiment = st.selectbox("Select Sentiment", sorted(df["classification"].dropna().unique()))
filtered = df[df["classification"] == sentiment]

st.subheader("Summary Statistics")
st.write(filtered[["daily_pnl", "trades_count", "avg_trade_size_usd", "win_rate", "long_short_ratio"]].describe())


st.subheader("Average Metrics")
st.write(filtered.groupby("classification").agg(
    mean_pnl=("daily_pnl", "mean"),
    mean_win_rate=("win_rate", "mean"),
    mean_trades=("trades_count", "mean"),
    mean_size=("avg_trade_size_usd", "mean")
))

st.subheader("PnL Distribution (Gains vs Losses)")

fig, ax = plt.subplots()
ax.hist(filtered["daily_pnl"].dropna(), bins=50)
ax.axvline(0)  # zero line to separate losses and gains
ax.set_xlabel("Daily PnL")
ax.set_ylabel("Frequency")
ax.set_title(f"PnL Distribution for {sentiment}")

st.pyplot(fig)
