import requests
import pandas as pd
import json
from datetime import datetime, timedelta, timezone
from time import sleep

# Assigning API URL to a variable
hours_url = "https://data-api.coindesk.com/spot/v1/historical/hours"
days_url = "https://data-api.coindesk.com/spot/v1/historical/days"

# Defining a dictionary of parameters to be used in the GET method
params = {
"market": "binance",
"instrument": "BTC-USDT",
"aggregate": 1,
"fill": "true",
"apply_mapping": "true",
"response_format": "JSON",
"api_key": "8965730f944167b898229a2c2ce7dd7ed6277eb6510df5fe3573a5c839d3e2a1"
}

# Making a GET request and storing the response in a variable
params["limit"] = 168
response = requests.get(hours_url, params=params)
data = response.json()

# Converting the returned JSON data into a Pandas DataFrame
df = pd.DataFrame(data["Data"])
df["TIMESTAMP"] = df["TIMESTAMP"].apply(lambda x: datetime.fromtimestamp(x, tz=timezone.utc))

# Viewing every column name

for _ in range(len(df.columns)):
    print(df.columns[_])
print("-" * 25 + "\n")

# Showing BTC value along last 7 days

btc_last_7_days_price = df.loc[:, "CLOSE"]
btc_last_7_days_price.index = df["TIMESTAMP"]

# Showing BTC value along last 2 months
params["limit"] = 60
response = requests.get(days_url, params=params)
data = response.json()
df = pd.DataFrame(data["Data"])

total_trades_last_week = df.loc[53:, "TOTAL_TRADES"]
total_trades_last_week.index = df.loc[53:, "TIMESTAMP"].apply(lambda x: datetime.fromtimestamp(x, tz=timezone.utc))

mean_trades_last_week = total_trades_last_week.sum() / 7
print(total_trades_last_week)
print(mean_trades_last_week)

btc_last_2_months_price = df["CLOSE"]
df["TIMESTAMP"] = df["TIMESTAMP"].apply(lambda x: datetime.fromtimestamp(x, tz=timezone.utc))
btc_last_2_months_price.index = df["TIMESTAMP"]

btc_price_seven_days_ago = df.loc[52, "CLOSE"]
btc_price_today = df.loc[59, "CLOSE"]
btc_price_weekly_change = ((btc_price_today * 100) / btc_price_seven_days_ago) - 100
btc_price_weekly_change = round(btc_price_weekly_change, 2)

data = {
    'btc_price_weekly_change': btc_price_weekly_change,
    'btc_price_today': btc_price_today
}

with open("dashboard_data.json", "w") as f:
    json.dump(data, f)

# print(btc_price_weekly_change)
# print(btc_price_today)
# print(btc_price_seven_days_ago)
# print(btc_last_2_months_price.head(60))

# Showing BTC value along last year
params["limit"] = 365
response = requests.get(days_url, params=params)
data = response.json()
df = pd.DataFrame(data["Data"])

btc_last_year_price = df["CLOSE"]
df["TIMESTAMP"] = df["TIMESTAMP"].apply(lambda x: datetime.fromtimestamp(x, tz=timezone.utc))
btc_last_year_price.index = df["TIMESTAMP"]
print(btc_last_year_price)
