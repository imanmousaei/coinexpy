from .requestclient import RequestClient


class Coinex:
    """
    methods:
    - get_balance()
    - get_available('USDT')
    - get_last_price('BTCUSDT')

    - limit_buy('BTCUSDT', 0.01, 50000)
    - limit_sell('BTCUSDT', 0.01, 50000)
    - market_buy('BTCUSDT', 0.01)
    - market_sell('BTCUSDT', 0.01)

    - pending_orders('BTCUSDT', 1, 10)
    - finished_orders('BTCUSDT', 1, 10)

    - sell_coin('BTC')
    - cancel_order

    """

    def __init__(self, access_id, secret_key):
        self.client = RequestClient(access_id, secret_key)

    def get_balance(self):
        """
        :return: dict containing all pf your account
        """
        response = self.client.request('GET', '/v1/balance/')
        return response

    def get_available(self, coin: str = 'USDT'):
        """
        :param coin: coin to get balance for
        :return: available balance for the given coin
        """
        coin = coin.upper()
        all_coins = self.get_balance()
        try:
            return float(all_coins['data'][coin]['available'])
        except:
            # raise ValueError(f'You dont have any {coin} in your account')
            return 0

    def get_last_price(self, market: str):
        """
        get last price traded with this market
        :param market: market to get price
        """
        params = {
            'market': market,
            'last_id': 0,
            'limit': 1,
        }
        response = self.client.request(
            'GET',
            '/v1/market/deals',
            params=params
        )
        return float(response['data'][0]['price'])

    def pending_orders(self, market: str, page, limit):
        """
        Acquire Unexecuted Order List
        :param market: market to get it's orders e.g. BTCUSDT
        :param page: page number(start from 1)
        :param limit: Amount per page(1-100)
        :return: list
        """
        params = {
            'market': market,
            'page': page,
            'limit': limit
        }
        response = self.client.request(
            'GET',
            '/v1/order/pending',
            params=params
        )
        return response

    def finished_orders(self, market, page, limit):
        """
        Acquire Executed Order List
        :param market: market to get it's orders e.g. BTCUSDT
        :param page: page number(start from 1)
        :param limit: Amount per page(1-100)
        :return: list
        """
        params = {
            'market': market,
            'page': page,
            'limit': limit
        }
        response = self.client.request(
            'GET',
            '/v1/order/finished',
            params=params
        )
        return response

    def limit_sell(self, market: str, amount, price):
        """
        :param market: e.g. 'BTCUSDT
        :param amount: amount in 2nd currency
        :param price: price to put limit order
        :return: response of the sell request
        """
        return self.limit_order(market, amount, price, 'sell')

    def limit_buy(self, market: str, amount, price):
        """
        :param market: e.g. 'BTCUSDT
        :param amount: amount in 2nd currency
        :param price: price to put limit order
        :return: response of the buy request
        """
        return self.limit_order(market, amount, price, 'buy')

    def limit_order(self, market: str, amount, price, type: str, amount_in=2):
        """
        :param market: e.g. 'BTCUSDT
        :param amount: amount to buy/sell
        :param price: price to order
        :param type: 'buy' or 'sell'
        :param amount_in: if =2 amount is calculated in 2nd currency in pair. else, in 1st
        """

        if amount_in == 2:
            market = market.upper()
            amount = amount / price
            amount = round(amount, 8)

        if type != 'buy' and type != 'sell':
            raise ValueError('type should either be "buy" or "sell" ')

        data = {
            "amount": amount,
            "price": price,
            "type": type,
            "market": market
        }

        response = self.client.request(
            'POST',
            '/v1/order/limit',
            json=data,
        )
        return response

    def market_sell(self, market: str, amount):
        """
        :param market: e.g. 'BTCUSDT
        :param amount: amount in 2nd currency
        :return: response of the sell request
        """
        price = self.get_last_price(market)
        amount = amount / price
        return self.market_order(market, amount, 'sell')

    def market_buy(self, market: str, amount):
        """
        :param market: e.g. 'BTCUSDT
        :param amount: amount in 2nd currency
        :return: response of the buy request
        """
        return self.market_order(market, amount, 'buy')

    def market_order(self, market: str, amount, type: str, amount_in=2):
        """
        :param market: e.g. 'BTCUSDT
        :param amount: amount to buy/sell
        :param type: 'buy' or 'sell'
        :param amount_in: if =1 amount is calculated in 1st currency in pair. else, in 2nd
        """
        market = market.upper()
        amount = round(amount, 8)

        if amount_in == 1:
            price = self.get_last_price(market)
            amount = amount * price
            amount = round(amount, 8)

        if type != 'buy' and type != 'sell':
            raise ValueError('type should either be "buy" or "sell" ')

        data = {
            "amount": amount,
            "type": type,
            "market": market
        }

        response = self.client.request(
            'POST',
            '/v1/order/market',
            json=data,
        )
        return response

    def sell_coin(self, coin: str, price=None):
        """
        sell all of the `coin` you have to USDT
        :param coin: coin to sell
        :param price: price to sell the coin in(if not given, use market price)
        """
        available = self.get_available(coin)
        market = f'{coin}USDT'
        if price is None:
            result = self.market_order(market, available, 'sell')
        else:
            result = self.limit_order(market, available, price, 'sell', 1)
        return result

    def cancel_order(self, market: str, id):
        """
        cancels the unexecuted order
        :param market: e.g. BTCUDST
        :param id: order id
        """
        data = {
            "id": id,
            "market": market,
        }

        response = self.client.request(
            'DELETE',
            '/v1/order/pending',
            params=data,
        )
        return response
