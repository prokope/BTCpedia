const carousel = document.querySelector(".carousel");
const nextBtn = document.querySelector(".next");
const prevBtn = document.querySelector(".prev");
const section_h1 = document.getElementById("section_h1");

var active_section = 'News';

if (!carousel) {
  console.error("Elemento .carousel/#carousel não encontrado");
}

// Funções para mudar diretamente para cada seção
function showDashboard() {

    prevBtn.removeAttribute("id");
    nextBtn.id = 'active_btn';

    if (active_section == 'News')
    {
        carousel.style.transform = `translateX(-100%)`; // dashboard é a segunda section
        section_h1.classList.add('h1_fade_out');
        setTimeout(() =>
        {
            section_h1.classList.remove("h1_fade_out")
            section_h1.textContent = "Dashboard";
        }, 450)
        active_section = 'Dashboard';
    }
}

function showNews() {

    nextBtn.removeAttribute("id");
    prevBtn.id = "active_btn";

    if (active_section == 'Dashboard')
    {
        carousel.style.transform = `translateX(0%)`; // news é a primeira section
        section_h1.classList.add('h1_fade_out');

        setTimeout(() =>
        {
            section_h1.classList.remove("h1_fade_out")
            section_h1.textContent = "Relevant News";
        }, 450)
        active_section = 'News';
    }
}

// Eventos dos botões
nextBtn?.addEventListener("click", showDashboard);
prevBtn?.addEventListener("click", showNews);


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

fetch("https://newsdata.io/api/1/latest?apikey=pub_b042edecf45a4e6b8f029bdcbc20392c&q=bitcoin&language=en")

.then(response => {
    if (!response.ok)
    {
        console.log("Error while requesting API" + response.status);
    }

    else
    {
        console.log("Data from NewsData API successfully loaded!");
        return response.json();
    }
})

.then(data => {
    console.log(data.results);
    var news = data.results;

    for(var i = 0; i < 3; i++)
    {
        if ((news[i].description.length) > 175)
        {
            news[i].description = news[i].description.substring(0, 175) + "...";
        }

        if (news[i].title.length > 40)
        {
            news[i].title = news[i].title.substring(0, 40) + "...";
        }
    }
    
    const first_news_title = document.getElementById('first_news_title');
    first_news_title.textContent = news[0].title;

    const first_news_description = document.getElementById('first_news_description');
    first_news_description.textContent = news[0].description;

    const second_news_title = document.getElementById('second_news_title');
    second_news_title.textContent = news[1].title;

    const second_news_description = document.getElementById('second_news_description');
    second_news_description.textContent = news[1].description;

    const third_news_title = document.getElementById('third_news_title');
    third_news_title.textContent = news[2].title;

    const third_news_description = document.getElementById('third_news_description');
    third_news_description.textContent = news[2].description;
})


