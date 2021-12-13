# account
get_balance = '/perpetual/v1/asset/query'
acquire_unexecuted_order_list = '/perpetual/v1/order/pending'
acquire_executed_order_list = '/perpetual/v1/order/finished'
acquire_order_status = '/perpetual/v1/order/status'
adjust_leverage = '/perpetual/v1/market/adjust_leverage'


# market
get_market_deals = '/perpetual/v1/market/deals'


# order
place_limit_order = '/perpetual/v1/order/put_limit'
close_limit_order = '/perpetual/v1/order/close_limit'

place_market_order = '/perpetual/v1/order/put_market'
close_market_order = '/perpetual/v1/order/close_market'

place_stop_limit_order = '/perpetual/v1/order/put_stop_limit'
place_stop_market_order = '/perpetual/v1/order/put_stop_market'

cancel_pending_order = '/perpetual/v1/order/cancel'
cancel_all_pending_orders = '/perpetual/v1/order/cancel_all'
