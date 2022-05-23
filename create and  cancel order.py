import ccxt
from pprint import pprint
exchange = ccxt.kucoinfutures({
    'adjustForTimeDifference': True,
    'apiKey': '******',
    'secret': '*****',
    'password': '********',
})


symbol = 'LUNA/USDT:USDT'
amount = 3000
price = 0.0001
type = 'limit'
side = 'buy'

exchange.verbose = True


order = exchange.create_limit_buy_order(
    symbol, amount, price)
pprint(order)

#cancel_order = exchange.cancel_all_orders(symbol)  # for cancel orders uncoment this and coment order
#pprint(cancel_order)
