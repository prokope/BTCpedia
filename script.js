function chart_changed()
{
    const menu = document.getElementById('chart_options');
    const iframe = document.getElementById('iframe_chart');

    if (menu.value === "btc_last_month_chart")
    {
        iframe.src = "btc_last_month_chart.html";
    }

    else if (menu.value === "btc_7_days_chart")
    {
        iframe.src = "btc_7_days_chart.html";
    }
}