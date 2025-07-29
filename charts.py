import pandas as pd
import plotly.graph_objects as go
from request import btc_last_7_days_price

print(btc_last_7_days_price)
fig = go.Figure([go.Scatter(x=btc_last_7_days_price.index.to_list(), y=btc_last_7_days_price)])
fig.update_traces(line_color="#ff6d4d")
fig.update_layout(
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='#e6e6e6'
)
fig.show()
fig.write_html("btc_7_days_chart")