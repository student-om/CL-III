from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def index(request):
    # Securely fetch API key from environment variables
    api_key = os.getenv('NEWS_API_KEY', '751bb6faabfc47f9a43aecd73f80b0fb')

    url = f'https://newsapi.org/v2/everything?q=Cryptocurrency&from=2021-09-08&sortBy=popularity&apiKey={api_key}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an error if request fails
        crypto_news = response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching news:", e)
        return render(request, 'index.html', {'error': 'Failed to fetch news'})

    # Ensure 'articles' key exists
    articles = crypto_news.get('articles', [])

    desc = []
    title = []
    img = []

    for article in articles:
        title.append(article.get('title', 'No title available'))
        desc.append(article.get('description', 'No description available'))
        img.append(article.get('urlToImage', 'default_image_url.jpg'))  # Fallback image

    mylist = list(zip(title, desc, img))  # Convert zip to list

    context = {'mylist': mylist}
    return render(request, 'index.html', context)
