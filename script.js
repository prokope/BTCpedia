function body_transition()
{
    document.body.style.opacity = 1;
}

function chart_changed()
{
    const menu = document.getElementById('chart_options');
    const iframe = document.getElementById('iframe_chart');

    iframe.classList.add('fade-out');

    setTimeout (() =>
    {
        if (menu.value === "btc_last_2_months_chart")
        {
            iframe.src = "btc_last_2_months_chart.html";
        }

        else if (menu.value === "btc_7_days_chart")
        {
            iframe.src = "btc_7_days_chart.html";
        }

        else if (menu.value == "btc_last_year_chart")
        {
            iframe.src = "btc_last_year_chart.html";
        }

        iframe.onload = () =>
        {
            iframe.classList.remove("fade-out");
        }
    }, 350);
}
