import requests
import streamlit as st
from datetime import date, timedelta

@st.cache_data(ttl=3600)  # Cache results for 1 hour
def fetch_stock_price(symbol, api_key):
    """Fetch the current stock price from Finnhub API."""
    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['c']  # current price

@st.cache_data(ttl=3600)
def fetch_stock_news(symbol, api_key):
    """Fetch top 3 recent news headlines for the stock."""
    today = date.today()
    from_date = (today - timedelta(days=3)).isoformat()
    to_date = today.isoformat()

    url = f"https://finnhub.io/api/v1/company-news?symbol={symbol}&from={from_date}&to={to_date}&token={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    headlines = [article['headline'] for article in data if 'headline' in article]
    return headlines[:3]
