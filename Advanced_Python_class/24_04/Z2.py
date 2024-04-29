from Z1 import process_candles_data
import requests
import json
import pandas as pd
import mplfinance as mpl

url = 'https://www.mexc.com/open/api/v2/market/kline?symbol=ARBUZ_USDT&interval=1m&limit=1000'
response = requests.get(url)
responseBody = response.text
responseBodyJson = json.loads(responseBody)
candles_data = responseBodyJson["data"]

def