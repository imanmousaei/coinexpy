# coinexpy - Python wrapper for Coinex APIs
Through coinexpy you can simply buy or sell crypto in your [Coinex](https://www.coinex.com) account

# Features
* place limit order
* place market order
* get balance
* get price

# Install
```bash
pip install coinexpy
```

# Example
You can create API key and get your access_id & secret_key [here](https://www.coinex.com/apikey)
```python
from coinexpy.coinex import Coinex


coinex = Coinex('<your_access_id>', '<your_secret_key>')

balance = coinex.get_balance()
usdt_balance = coinex.get_available('USDT')
btc_price = coinex.get_last_price('BTCUSDT')

coinex.market_buy('BTCUSDT', 100)  # buy 100$ worth of bitcoin with market price
coinex.market_sell('BTCUSDT', 0.01)  # sell 0.01BTC

coinex.limit_buy('BTCUSDT', 100, 50000) # place a limit buy order on bitcoin with amount=100$
result = coinex.limit_sell('BTCUSDT', 0.01, 50000)

coinex.cancel_order(result['id'], result['market'])
```
