import requests
import pandas as pd
from datetime import datetime, timedelta, timezone

# Assigning API URL to a variable
hours_url = "https://data-api.coindesk.com/spot/v1/historical/hours"

# Defining a dictionary of parameters to be used in the GET method
params = {
    "market": "binance",
    "instrument": "BTC-USDT",
    "limit": 168 ,
    "aggregate": 1,
    "fill": "true",
    "apply_mapping": "true",
    "response_format": "JSON",
    "api_key": "8965730f944167b898229a2c2ce7dd7ed6277eb6510df5fe3573a5c839d3e2a1"
}

# Making a GET request and storing the response in a variable
response = requests.get(hours_url, params=params)
data = response.json()

# Converting the returned JSON data into a Pandas DataFrame
df = pd.DataFrame(data["Data"])
df["TIMESTAMP"] = df["TIMESTAMP"].apply(lambda x: datetime.fromtimestamp(x, tz=timezone.utc))

""" Viewing every column name
for _ in range(len(df.columns)):
    print(df.columns[_])
print("-" * 25 + "\n")
"""

# Showing BTC value along last 7 days

btc_last_7_days_price = df.loc[:, "CLOSE"]
btc_last_7_days_price.index = df["TIMESTAMP"]
print(btc_last_7_days_price)

# Showing BTC value along last month
days_url = "https://data-api.coindesk.com/spot/v1/historical/days"
params["limit"] = 60
response = requests.get(days_url, params=params)
data = response.json()
df = pd.DataFrame(data["Data"])

btc_last_month_price = df["CLOSE"]
df["TIMESTAMP"] = df["TIMESTAMP"].apply(lambda x: datetime.fromtimestamp(x, tz=timezone.utc))
btc_last_month_price.index = df["TIMESTAMP"]
print(btc_last_month_price)
