import os
from dotenv import load_dotenv
from alpaca_trade_api.rest import REST

load_dotenv()

BASE_URL = "https://paper-api.alpaca.markets"
api = REST(base_url=BASE_URL)  # Uses APCA_API_KEY_ID and APCA_API_SECRET_KEY from .env

def buy_stock(symbol, qty=1):
    print(f"➡️ Buying {symbol}")
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )
    print(f"✅ BUY placed for {symbol}")

def sell_stock(symbol, qty=1):
    position_qty = 0
    try:
        position = api.get_position(symbol)
        position_qty = int(position.qty)
    except Exception as e:
        print(f"🔍 No existing position in {symbol}. Cannot sell.")
        return

    if position_qty < qty:
        print(f"⚠️ You only own {position_qty} shares of {symbol}. Cannot sell {qty}.")
        return

    print(f"➡️ Selling {qty} of {symbol}")
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='market',
        time_in_force='gtc'
    )
    print(f"✅ SELL placed for {symbol}")
