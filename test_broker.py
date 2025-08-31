import os
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST

# ✅ Load keys from .env
load_dotenv()

# ✅ Use correct base URL (no /v2)
BASE_URL = "https://paper-api.alpaca.markets"
api = REST(base_url=BASE_URL)  # Automatically uses env vars: APCA_API_KEY_ID + APCA_API_SECRET_KEY

# ✅ Function to place a BUY order
def buy_stock(symbol, qty=1):
    print(f"➡️ Placing BUY order for {symbol}")
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    print(f"✅ Order placed for {symbol}!")

# ✅ Call the function
if __name__ == "__main__":
    print("📦 Sending test order...")
    buy_stock("AAPL")
    print("🧾 Done! Check your Alpaca orders dashboard.")
