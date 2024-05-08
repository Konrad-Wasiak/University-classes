import requests
import json
import pandas as pd
import mplfinance as mpl
def get_candles_data(interval: int, limit: int):
    url = ('https://www.mexc.com/open/api/v2/market/kline?symbol=ARBUZ_USDT&interval=' +
           str(interval) + 'm&limit=' + str(limit))
    response = requests.get(url)
    responseBody = response.text
    responseBodyJson = json.loads(responseBody)
    candles_data = responseBodyJson["data"]
    return candles_data


def process_candles_data(candles_data):
    formatted_candles_data = []
    for candle in candles_data:
        new_candle = {}
        new_candle_elements = [
            ('time', candle[0]), ('open', float(candle[1])), ('close', float(candle[2])),
            ('high', float(candle[3])), ('low', float(candle[4]))
        ]
        new_candle.update(new_candle_elements)
        formatted_candles_data.append(new_candle)
    return formatted_candles_data


def plot_candles(formatted_candles_data):
    df = pd.json_normalize(formatted_candles_data)  # przetwarzamy dane w formacie json
    df.time = pd.to_datetime(df.time,
                             unit='s')  # ponieważ oczekiwany format daty w kolumnie "time" jest inny niż oczekiwany przez bibliotekę to musimy go skonwertować
    df = df.set_index("time")  # ustawiamy index naszych danych na kolumnę "time"

    mpl.plot(
        df,  # przekazujemy obiekt z danymi
        type="candle",  # określamy typ wykresu.
        title="Candle chart",  # nadajemy tytuł naszego wykresu.
        style="binance",  # wersja kolorystyczna wykresu.
        mav=(3, 6, 9)  # atrybut który włączy automatyczne obliczanie oraz rysowanie średni kroczących.
    )

# A function responsible for finding a similar pattern to the one occurring in the last 10 candles,
# in the range of 1,000 candles.
def find_similar_candles():
    candles_data = get_candles_data(1, 1000)
    formatted_candles_data = process_candles_data(candles_data)
    last_ten_candles = formatted_candles_data[-11:-1]

    # Variable storing 'open' and 'close' differences
    # between neighbours from the last 10 candles.
    last_10_candles_difference_list = []

    # Comparing candles with their right-side neighbours;
    # omitting the last candle, since it has no neighbours on the right.
    for candle_index in range(0,9):
        variation = last_ten_candles[candle_index]["open"] - last_ten_candles[candle_index]["close"]
        variation_neighbour = last_ten_candles[candle_index+1]["open"] - last_ten_candles[candle_index+1]["close"]
        neighbour_candles_difference = variation - variation_neighbour
        last_10_candles_difference_list.append(neighbour_candles_difference)

    # Removing last 10 candles from the downloaded data.
    formatted_candles_data = formatted_candles_data[0:990]

    # Variable storing differences for the other candles, grouped by 10.
    other_candles_difference_list = []

    # List storing groups of 10 candles, to compare these groups later with the last 10 from the whole 1,000.
    groups_of_10_candles = []

    # 99 times * 10 candles
    for candle_group_index in range(1, 100):
        group_of_10_candles = []

        for candle_index in range(0, 9):
            variation = (
                (formatted_candles_data[candle_index*candle_group_index]["open"] -
                 formatted_candles_data[candle_index*candle_group_index]["close"])
            )
            variation_neighbour = (
                (formatted_candles_data[(candle_index*candle_group_index)+1]["open"] -
                 formatted_candles_data[(candle_index*candle_group_index)+1]["close"])
            )
            neighbouring_candles_difference = abs(variation - variation_neighbour)
            group_of_10_candles.append(neighbouring_candles_difference)

        groups_of_10_candles.append(group_of_10_candles)


    # A list storing these differences between a group of 10 candles and the last 10 downloaded candles.
    differences_between_candle_groups = []

    # Loop comparing these groups.
    for group in groups_of_10_candles:
        # Variable storing a difference between corresponding elements between two groups of 10 candles
        # (with one of them being always the same - the last 10 candles downloaded via API).

        # Difference is going to be calculated here as a sum of variability between corresponding elements in the
        # compared groups.
        difference_between_candle_groups = 0
        for difference_index in range(0, 9):
            difference_between_candle_groups += (
                    group[difference_index] - last_10_candles_difference_list[difference_index]
            )
        differences_between_candle_groups.append(difference_between_candle_groups)

    # Minimal difference.
    min_difference_between_groups = min(differences_between_candle_groups)

    # Finding the earliest group of 10 candles with such difference.

    # Finding index of a group of candles in the groups_of_10_candles variable.
    for difference_index in range(0, len(differences_between_candle_groups)):
        if differences_between_candle_groups[difference_index] == min_difference_between_groups:
            min_difference_index = difference_index

    # Calculating the indices of the corresponding elements in formatted_candles_data, to access other variables
    # not stored in the lists created by me later.
    start_index = min_difference_index * 10
    end_index = min_difference_index * 10 + 10

    # Variable storing candles with a similar pattern to this of the last 10 downloaded candles.
    similar_candles = formatted_candles_data[start_index:end_index]

    # Plotting charts.
    plot_candles(last_ten_candles)
    plot_candles(similar_candles)

find_similar_candles()