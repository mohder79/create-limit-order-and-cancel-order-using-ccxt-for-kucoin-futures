import ccxt
from pprint import pprint
exchange = ccxt.kucoinfutures({
    'adjustForTimeDifference': True,
    'apiKey': '628b5b6184217c000119672f',
    'secret': 'a29b5823-ee2f-4edb-b921-bc067a9f41b0',
    'password': 'MOHder1379',
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
