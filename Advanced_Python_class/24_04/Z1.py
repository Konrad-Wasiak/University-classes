import requests
import json
import pandas as pd
import mplfinance as mpl

url = 'https://www.mexc.com/open/api/v2/market/kline?symbol=ARBUZ_USDT&interval=60m&limit=10'
response = requests.get(url)
responseBody = response.text
responseBodyJson = json.loads(responseBody)
candles_data = responseBodyJson["data"]

def process_candles_data(candles_data):
    formatted_candles_data = []
    for candle in candles_data:
        new_candle = {}
        new_candle_elements = [
            ('time', candle[0]), ('open', float(candle[1])), ('close', float(candle[2])), ('high', float(candle[3])), ('low', float(candle[4]))
        ]
        new_candle.update(new_candle_elements)
        formatted_candles_data.append(new_candle)
    return formatted_candles_data


formatted_candles_data = process_candles_data(candles_data)


df = pd.json_normalize(formatted_candles_data) # przetwarzamy dane w formacie json
df.time = pd.to_datetime(df.time, unit='s') # ponieważ oczekiwany format daty w kolumnie "time" jest inny niż oczekiwany przez bibliotekę to musimy go skonwertować
df = df.set_index("time") # ustawiamy index naszych danych na kolumnę "time"
print(df.head())

mpl.plot(
    df, # przekazujemy obiekt z danymi
    type="candle", # określamy typ wykresu.
    title="Candle chart", # nadajemy tytuł naszego wykresu.
    style="binance", # wersja kolorystyczna wykresu.
    mav=(3, 6, 9) # atrybut który włączy automatyczne obliczanie oraz rysowanie średni kroczących.
)
