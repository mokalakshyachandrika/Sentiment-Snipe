# 🤖 Sentiment Snipe – AI-Powered Stock Trading Dashboard

**Sentiment Snipe** is a smart and interactive dashboard that fetches **real-time stock prices and news headlines**, performs **sentiment analysis using FinBERT**, and allows users to **BUY/SELL stocks** instantly using the **Alpaca API** — all inside a beautifully styled **Streamlit web app**.

---

## 🚀 Features

- 📈 Real-time stock price display (Finnhub API)
- 📰 Live news headlines (latest 3) for selected stocks
- 💬 Sentiment analysis on headlines using **FinBERT**
- 🟢 BUY and 🔴 SELL buttons powered by **Alpaca Trading API**
- 🎨 Custom themed Streamlit interface with emojis and highlights

---


## 🛠️ Tech Stack

| Tool             | Purpose                               |
|------------------|----------------------------------------|
| Python 3.x       | Core language                          |
| Streamlit        | Web app/dashboard                      |
| Finnhub API      | Real-time stock data and news          |
| FinBERT (HuggingFace) | Sentiment analysis on headlines  |
| Alpaca API       | Place real trades (paper mode)         |
| Requests         | API calls                              |
| Dotenv           | Secure API key handling                |
| Pandas           | DataFrame display                      |

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/sentiment-snipe.git
cd sentiment-snipe
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 API Configuration

Create a `.env` file in the root folder and add the following:

```env
FINNHUB_API_KEY=your_finnhub_api_key
APCA_API_KEY_ID=your_alpaca_api_key
APCA_API_SECRET_KEY=your_alpaca_secret_key
```

✅ **Make sure not to upload this file to GitHub.**

---

## 🚦 Run the App

```bash
streamlit run main.py
```

It will open in your browser at: [http://localhost:8501](http://localhost:8501)

---

## 🧠 How It Works

1. **User selects stock symbols** (AAPL, TSLA, etc.)
2. App fetches:
   - Latest stock price from Finnhub
   - Top 3 news headlines
3. Each headline is analyzed using **FinBERT** to label as:
   - 🟢 Positive
   - 🔴 Negative
   - ⚪ Neutral
4. User can press **BUY** or **SELL** buttons
   - Automatically places order using Alpaca API
   - You can view orders in your Alpaca dashboard

---

## ✅ Example Use Cases

- 🔍 Monitor stock price + live news before making a trade
- 🧠 Use AI to assess market sentiment instantly
- 💸 Execute trades with 1 click (on Alpaca paper trading)

---

## 🚧 Roadmap

- [ ] Add quantity input for buying/selling
- [ ] Show order history in dashboard
- [ ] Deploy to Streamlit Cloud or HuggingFace Spaces
- [ ] Sentiment history chart for each stock

---

## 📂 Folder Structure

```
📦 sentiment_snipe/
├── main.py                 # Streamlit dashboard
├── .env                   # API keys (excluded from GitHub)
├── requirements.txt       # All dependencies
├── test_broker.py         # Script to test Alpaca orders
├── README.md              # This file
├── /src
│   ├── broker.py          # Alpaca buy/sell functions
│   ├── config.py          # .env loader
│   ├── news_fetcher.py    # Get prices + headlines
│   └── sentiment.py       # FinBERT analysis
└── /assets
    ├── screenshot1.png    # Dashboard UI
    └── screenshot2.png    # Summary Table
```

---

## 📄 License

MIT – Feel free to use, remix, and share. Attribution appreciated.

---

## 🙋‍♂️ Author

Made with ❤️ by **Lakshya**  
🔗 [LinkedIn](https://www.linkedin.com/in/moka-lakshya/)

---

> ⭐ If you like this project, drop a star!




