import requests
import pandas as pd
from datetime import datetime, timedelta

# Assigning API URL to a variable
url = "https://data-api.coindesk.com/spot/v1/historical/days"

# Defining a dictionary of parameters to be used in the GET method
params = {
    "market": "binance",
    "instrument": "BTC-USDT",
    "limit": 7 ,
    "aggregate": 1,
    "fill": "true",
    "apply_mapping": "true",
    "response_format": "JSON",
    "api_key": "8965730f944167b898229a2c2ce7dd7ed6277eb6510df5fe3573a5c839d3e2a1"
}

# Making a GET request and storing the response in a variable
response = requests.get(url, params=params)
data = response.json()

# Converting the returned JSON data into a Pandas DataFrame
df = pd.DataFrame(data["Data"])

# Viewing every column name
# print("Columns:")
for _ in range(len(df.columns)):
    # print(df.columns[_])
    pass

# print("-" * 25 + "\n")

# Showing BTC value along last 7 days
seven_days_ago = datetime.today() - timedelta(days=6)
date = pd.date_range(start=seven_days_ago.date(), end=datetime.today(), freq='D')
btc_last_7_days_price = df.loc[:, "CLOSE"]
btc_last_7_days_price.index = date
# print(f"Last Week BTC Value:\n{btc_last_7_days_price}")
