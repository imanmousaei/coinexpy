from requestclient import RequestClient

# todo : function input doc, input validation


class Coinex:
    """
    methods:
    - get_balance()
    - get_available('USDT')
    - limit_buy('BTCUSDT', 0.01, 50000)
    - limit_sell('BTCUSDT', 0.01, 50000)
    - market_buy('BTCUSDT', 0.01)
    - market_sell('BTCUSDT', 0.01)
    - get_last_price('BTCUSDT')

    """

    def __init__(self, access_id, secret_key):
        self.client = RequestClient(access_id, secret_key)

    def get_balance(self):
        response = self.client.request('GET', '/v1/balance/')
        return response

    def get_available(self, coin='USDT'):
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

    def get_last_price(self, market):
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

    # todo : test
    def order_pending(self, market_type):
        params = {
            'market': market_type
        }
        response = self.client.request(
            'GET',
            '/v1/order/pending',
            params=params
        )
        print(response)

    # todo : test
    def order_finished(self, market_type, page, limit):
        params = {
            'market': market_type,
            'page': page,
            'limit': limit
        }
        response = self.client.request(
            'GET',
            '/v1/order/finished',
            params=params
        )
        return response

    def limit_sell(self, market, amount, price):
        """
        :param market: e.g. 'BTCUSDT
        :param amount: amount in source currency
        :param price: price to put limit order
        :return: response of the sell request
        """
        return self.limit_order(market, amount, price, 'sell')

    def limit_buy(self, market, amount, price):
        """
        :param market: e.g. 'BTCUSDT
        :param amount: amount in destination currency
        :param price: price to put limit order
        :return: response of the sell request
        """
        return self.limit_order(market, amount, price, 'buy')

    # todo : test
    def limit_order(self, market, amount, price, type):
        market = market.upper()
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

    def market_sell(self, market, amount):
        return self.market_order(market, amount, 'sell')

    def market_buy(self, market, amount):
        return self.market_order(market, amount, 'buy')

    def market_order(self, market, amount, type):
        market = market.upper()
        amount = round(amount, 8)
        print(amount)

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

    def sell_coin(self, coin, price=None):
        """ sell all of the `coin` you have to USDT in limit price (if you dont input price, it'll use market price) """
        available = self.get_available(coin)
        if price is None:
            self.market_sell(f'{coin}USDT', available)
        else:
            self.limit_sell(f'{coin}USDT', available, price)

    # todo : test
    def cancel_order(self, id, market):
        data = {
            "id": id,
            "market": market,
        }
        print(market)

        response = self.client.request(
            'DELETE',
            '/v1/order/pending',
            params=data,
        )
        return response.data

# sample
# order_data = complex_json.loads(put_limit_order())['data']
# id = order_data['id']
# market = order_data['market']
# cancel_order(id, market)
