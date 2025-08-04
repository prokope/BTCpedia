import pandas as pd
import plotly.graph_objects as go
from request import btc_last_7_days_price, btc_last_month_price

# BTC Last 7 days Chart
print(btc_last_7_days_price)
btc_last_7_days_chart = go.Figure([go.Scatter(x=btc_last_7_days_price.index.to_list(), y=btc_last_7_days_price)])
btc_last_7_days_chart.update_traces(line_color="#ff6d4d")
btc_last_7_days_chart.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='#e6e6e6'
)
# btc_last_7_days_chart.show()
btc_last_7_days_chart.write_html("btc_7_days_chart.html")

# BTC Last Month Chart
btc_last_month_chart = go.Figure([go.Scatter(x = btc_last_month_price.index.to_list(), y=btc_last_month_price)])
btc_last_month_chart.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='#e6e6e6'
)
btc_last_month_chart.update_traces(line_color="#ff6d4d")
btc_last_month_chart.show()
btc_last_month_chart.write_html("btc_last_month_chart.html")
