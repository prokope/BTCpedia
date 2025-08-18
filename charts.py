import plotly.graph_objects as go
from request import btc_last_7_days_price, btc_last_2_months_price, btc_last_year_price
from time import sleep

while True:
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
    btc_last_2_months_chart = go.Figure([go.Scatter(x = btc_last_2_months_price.index.to_list(), y=btc_last_2_months_price)])
    btc_last_2_months_chart.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='#e6e6e6'
    )
    btc_last_2_months_chart.update_traces(line_color="#ff6d4d")
    btc_last_2_months_chart.write_html("btc_last_2_months_chart.html")

    # BTC Last Year Price
    btc_last_year_chart = go.Figure([go.Scatter(x=btc_last_year_price.index.to_list(), y=btc_last_year_price)])
    btc_last_year_chart.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='#e6e6e6'
    )
    btc_last_year_chart.update_traces(line_color="#ff6d4d")
    btc_last_year_chart.show()
    btc_last_year_chart.write_html("btc_Last_year_chart.html")
    sleep(3600)
