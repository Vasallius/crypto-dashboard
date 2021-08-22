![Tab 1](https://github.com/Vasallius/crypto-dashboard/blob/master/media/tab-1.png)
# 📈 Crypto Dashboard

![GitHub last commit](https://img.shields.io/github/last-commit/Vasallius/crypto-dashboard) ![GitHub issues](https://img.shields.io/github/issues-raw/Vasallius/crypto-dashboard)


## 🔶 Project Overview

This project is used to analyze cryptocurrency coins listed at [Binance](https://www.binance.com/en) by showing the outliers based on relative 2 Day and 7 Day change along with other technical indicators such as Relative Strength Index (RSI), Choppiness Index (CHOP), Stochastics (STOCH). It also aims to leverage the RCS system byproving semi-realtime signals coupled with a risk score to aid traders in making a decision.


## 🔶 Getting Started

In order to fetch coin data yo need to create a [Binance](https://www.binance.com/en) account and perform basic verification. Next, we need to create our own api key and secret.

![How to create API Key](https://github.com/Vasallius/crypto-dashboard/blob/master/media/create_api.gif)

I use python's `dot-env` module to store these api details on environment variable and later access them via `os.getenv()`. 
Create a `.env` file in the root directory that looks exactly like this (don't change the variable names, don't wrap in quotation `"` marks):

```py
.env

API_KEY = h6QBbfGT0OIyPJLTHcua57Zrl5dxZqrKshPMbyTH1SIPCHiQv9Og4kNLrS58LkId
API_SECRET = wbz17g5uWRzZ1C2vJsEH7Qvkdi3aNxVpggYJqm1Xl3k70dnWebLB3l1NM9K2f9BB
```

Install the necessary dependencies by running:
```py
pip install -r requirements.txt
```

The project is currently ran on Jupyter Notebooks, so open up your favorite text editor and run the notebook there. Follow the link and the website should open in your local browser.


## 🔶 Support

If there are any concerns or problems, please don't hesistate to raise an issue!

## 🔶 Contributing

If you would like to contribute, do the following: 

1. Fork it (https://github.com/Vasallius/crypto-dashboard/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request


## 🔶 Roadmap and Pending Features

- Implement Figma Layout
- Use external database 
- External script to self-populate & maintain database
- Alerts Section
- Position Size Calculator
