from binance.client import Client

import config
import csv

client = Client(config.API_KEY, config.API_KEY)


historical_data = open('btcusd_data.csv', 'w', newline='')
candlestick_writer = csv.writer(historical_data, delimiter=',')

candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2012", "24 May, 2021")


for candlestick in candlesticks:
    candlestick_writer.writerow(candlestick)

historical_data.close()
