import streamlit as st
import pandas as pd
from src.news_fetcher import fetch_stock_price, fetch_stock_news
from src.config import FINNHUB_API_KEY
from src.sentiment import analyze_sentiment
from src.broker import buy_stock, sell_stock

def main():
    st.set_page_config(page_title="Sentiment Snipe", layout="wide")

    st.markdown("""
        <div style='text-align: center; padding: 10px 0 5px;'>
            <h1 style='font-size: 4.0em; color:#00BFFF;'>🤖 Sentiment Snipe</h1>
            <h4 style='color: #DDDDDD; font-size: 2.0em;'>AI-Powered News Sentiment Based Stock Trader</h4>
        </div>
        <hr style='border: 1px solid #444;' />
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='font-size:1.9em; color:#FFFFFF;'>📊 <b>Select Stocks</b></h4>", unsafe_allow_html=True)
    symbols = st.multiselect("", ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"])

    if not symbols:
        st.warning("⚠️ Please select at least one stock.")
        return

    prices = []

    for symbol in symbols:
        try:
            with st.spinner(f"Fetching {symbol} data..."):
                price = fetch_stock_price(symbol, FINNHUB_API_KEY)
                prices.append(price)

                st.markdown(
                    f"<h2 style='color:#00BFFF; font-size:2.1em;'>🚀 {symbol}: ${price}</h2>",
                    unsafe_allow_html=True
                )

                news = fetch_stock_news(symbol, FINNHUB_API_KEY)[:3]

                if news:
                    st.markdown("<h5 style='color:#AAAAAA;'>📰 Top Headlines & Sentiment</h5>", unsafe_allow_html=True)

                for headline in news:
                    sentiment = analyze_sentiment(headline)
                    emoji = "🟢" if sentiment == "positive" else "🔴" if sentiment == "negative" else "⚪"
                    st.markdown(f"<div style='font-size:1.1em;'>{emoji} <b>{sentiment.capitalize()}</b>: {headline}</div>", unsafe_allow_html=True)

                buy_col, sell_col = st.columns(2)
                with buy_col:
                    if st.button(f"💸 BUY {symbol}", key=f"buy_{symbol}"):
                        buy_stock(symbol)
                        st.success(f"✅ BUY order placed for {symbol}")
                with sell_col:
                    if st.button(f"📉 SELL {symbol}", key=f"sell_{symbol}"):
                        sell_stock(symbol)
                        st.success(f"❌ SELL order placed for {symbol}")

                st.markdown("""
                    <style>
                        button[kind="secondary"] {
                            font-size: 1.2em !important;
                            padding: 0.7em 1.5em !important;
                        }
                    </style>
                """, unsafe_allow_html=True)

                st.markdown("<hr style='border: 1px solid #333;' />", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"⚠️ Error for {symbol}: {e}")
            prices.append("N/A")

    while len(prices) < len(symbols):
        prices.append("N/A")

    st.markdown("<h4 style='font-size:1.8em;'>🗂️ <b>Stock Summary</b></h4>", unsafe_allow_html=True)
    df = pd.DataFrame({"Symbol": symbols, "Price": prices})
    st.dataframe(df, use_container_width=True)

if __name__ == "__main__":
    main()
