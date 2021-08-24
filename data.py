import os
from binance.client import Client
from dotenv import load_dotenv
import datetime as dt
import pandas as pd
import pandas_ta as ta


# Connect to API
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
load_dotenv()
client = Client(api_key, api_secret)


# Get all binance supported pairs except untradeable tokens
err_tokens = ['BULL', 'BEAR', 'DOWN', 'UP']
symbols_list = list(info['symbol']
                    for info in client.get_exchange_info()["symbols"] if (info['symbol'].endswith("USDT") and all(lev not in info['symbol'] for lev in err_tokens)))
sym_length = len(symbols_list)


# Fetch 200 days worth of data
d_start = (dt.datetime.now() - dt.timedelta(days=200)).strftime("%m-%d-%Y")
d_end = dt.datetime.now().strftime("%m-%d-%Y")


# Master_df holds 30 days worth of data and technical indicators
# Quant_df holds 2 day and 7 day changes

master_df = pd.DataFrame([])
quant_df = pd.DataFrame([], columns=["Symbol", "2D Δ", "7D Δ"])
sentiment = {
    'bullish': 0,
    'bearish': 0
}

err_symbols = []
for symbol in symbols_list:

    # Gets OHLCV values
    d_klines = [[float(num) for num in dta[:6]] for dta in client.get_historical_klines(
        symbol, Client.KLINE_INTERVAL_1DAY, d_start, d_end)]

    # Convert to readable time
    for x in d_klines:
        x[0] = dt.datetime.fromtimestamp(int(x[0]/1000)).strftime("%m-%d-%Y")

    df = pd.DataFrame(
        d_klines, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
    df['Symbol'] = symbol

    # some pairs don't have enough data
    try:
        rsi = round(df.ta.rsi(length=14), 3)
        chop = round(df.ta.chop(length=28), 3)
        stoch = df.ta.stoch()
        ma_20 = round(df.ta.sma(length=20), 4)
        ma_50 = round(df.ta.sma(length=50), 4)
        ma_100 = round(df.ta.sma(length=100), 4)
    except Exception as e:
        print(symbol, e)
        continue

    close = df['close']

    df['RSI(14)'] = rsi
    df['CHOP(28)'] = chop
    df['STOCH_K'] = round(stoch['STOCHk_14_3_3'], 2)
    df['STOCH_D'] = round(stoch['STOCHd_14_3_3'], 2)
    df['MA(20)'] = ma_20
    df['MA(50)'] = ma_50
    df['MA(100)'] = ma_100

    # TODO: #4 change method of counting trend of trends
    try:
        bluesky = (close > ma_20) & (ma_20 > ma_50) & (ma_50 > ma_100)
        retrace = (close < ma_20) & (ma_20 > ma_50) & (ma_50 > ma_100)
        reset = (ma_20 < ma_50) & (ma_50 > ma_100)
        reversal = (ma_20 > ma_50) & (ma_50 < ma_100)
        downtrend = (ma_100 > ma_50) & (ma_50 > ma_20)
        df['bluesky'] = bluesky
        df['retrace'] = retrace
        df['reset'] = reset
        df['reversal'] = reversal
        df['downtrend'] = downtrend
    except Exception as e:
        print(symbol, e)
        continue

    # Calculate changes and append to dataframe
    try:
        D1chg = (df.iloc[-1].close - df.iloc[-2].open) / df.iloc[-2].open
        D2chg = (df.iloc[-1].close - df.iloc[-3].open) / df.iloc[-3].open
        D7chg = (df.iloc[-1].close - df.iloc[-8].open) / df.iloc[-8].open

        quant_row = pd.DataFrame([[symbol, D2chg, D7chg, df.iloc[-1]['RSI(14)']]],
                                 columns=["Symbol", "2D Δ", "7D Δ", "RSI"])
        quant_df = pd.concat([quant_df, quant_row], ignore_index=True)
    except Exception as e:
        err_symbols.append(symbol)

    # Determine sentiment gauge
    bias = "bullish" if df.iloc[-1]['RSI(14)'] > df.iloc[-1]['CHOP(28)'] else "bearish"
    sentiment[bias] += 1

    # Only get last 30 trading days for ToT
    master_df = master_df.append(df.iloc[len(df.index)-30:])


# Keep track of trends for Trend of Trends
bluesky = []
retrace = []
reset = []
reversal = []
downtrend = []
lacking_data = []

# Calculate number of trends per day
for date in list(master_df[-30:]['date']):
    current = master_df[master_df['date'] == date]

    bluesky.append(current['bluesky'].value_counts().get(
        True)/sym_length if current['bluesky'].value_counts().get(True) != None else 0)

    retrace.append(current['retrace'].value_counts().get(
        True)/sym_length if current['retrace'].value_counts().get(True) != None else 0)

    reset.append(current['reset'].value_counts().get(
        True)/sym_length if current['reset'].value_counts().get(True) != None else 0)

    reversal.append(current['reversal'].value_counts().get(
        True)/sym_length if current['reversal'].value_counts().get(True) != None else 0)

    downtrend.append(current['downtrend'].value_counts().get(
        True)/sym_length if current['downtrend'].value_counts().get(True) != None else 0)


# Only plot above symbols that have above average 2 day and 7 day change
twomean = quant_df['2D Δ'].mean()
sevenmean = quant_df['7D Δ'].mean()
revised = quant_df[(quant_df['2D Δ'] > twomean) &
                   (quant_df['7D Δ'] > sevenmean)]
revised = revised.fillna(0)

print("Data.py succesfully loaded.")
