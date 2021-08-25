import os
from binance.client import Client
from dotenv import load_dotenv
import datetime as dt
import pandas as pd
import pandas_ta as ta
from boto.s3.connection import S3Connection


# Connect to API
# api_key = os.getenv("API_KEY")
# api_secret = os.getenv("API_SECRET")
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
print(api_key, api_secret)
# load_dotenv()
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
    print(f'{symbol} loaded.')
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

dates = master_df['date'].unique()

# Filter the data and count Trend of Trends

master_df = master_df.reset_index()
master_df = master_df.drop(columns=['index'])

close_gt_ma20 = master_df['close'] > master_df["MA(20)"]
close_lt_ma20 = master_df['close'] < master_df["MA(20)"]
ma20_gt_ma50 = master_df["MA(20)"] > master_df["MA(50)"]
ma20_lt_ma50 = master_df["MA(20)"] < master_df["MA(50)"]
ma50_gt_ma100 = master_df["MA(50)"] > master_df["MA(100)"]
ma50_lt_ma100 = master_df["MA(50)"] < master_df["MA(100)"]

bluesky = []
retrace = []
reset = []
reversal = []
downtrend = []
lacking_data = []

# Calculate number of trends per day
for date in list(master_df[-30:]['date']):
    current = master_df[master_df['date'] == date]

    bl = len(current[close_gt_ma20 & ma20_gt_ma50 & ma50_gt_ma100])/sym_length
    rt = len(current[close_lt_ma20 & ma20_gt_ma50 & ma50_gt_ma100])/sym_length
    rs = len(current[ma20_lt_ma50 & ma50_gt_ma100])/sym_length
    rv = len(current[ma20_gt_ma50 & ma50_lt_ma100])/sym_length
    d = len(current[close_lt_ma20 & ma20_lt_ma50 & ma50_lt_ma100])/sym_length

    bluesky.append(bl if bl != None else 0)
    retrace.append(rt if rt != None else 0)
    reset.append(rs if rs != None else 0)
    reversal.append(rv if rv != None else 0)
    downtrend.append(d if d != None else 0)


# Only plot above symbols that have above average 2 day and 7 day change
twomean = quant_df['2D Δ'].mean()
sevenmean = quant_df['7D Δ'].mean()
revised = quant_df[(quant_df['2D Δ'] > twomean) &
                   (quant_df['7D Δ'] > sevenmean)]
revised = revised.fillna(0)

print("Data.py succesfully loaded.")
