const BASE_URL = 'http://localhost:5000';

async function fetchNews() {
    try {
        const response = await fetch(`${BASE_URL}/news`);
        if (!response.ok) throw new Error('Error al obtener noticias');
        const news = await response.json();
        const newsContainer = document.getElementById('newsContainer');
        newsContainer.innerHTML = '';
        news.forEach(item => {
            const newsCard = document.createElement('div');
            newsCard.classList.add('news-card');
            newsCard.innerHTML = `
                <h3>${item.title}</h3>
                <p>${item.content}</p>
                <p><small>${new Date(item.date_posted).toLocaleDateString()}</small></p>
                ${item.image_url ? `<img src="${item.image_url}" alt="${item.title}" />` : ''}
            `;
            newsContainer.appendChild(newsCard);
        });
    } catch (error) {
        console.error('Error fetching news:', error);
        const newsContainer = document.getElementById('newsContainer');
        newsContainer.innerHTML = '<p>Hubo un problema al cargar las noticias.</p>';
    }
}

document.addEventListener('DOMContentLoaded', fetchNews);
