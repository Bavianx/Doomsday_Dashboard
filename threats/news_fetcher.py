import requests
from .models import NewsItem
from decouple import config

NEWS_API_KEY = config('NEWS_API_KEY')


THREAT_CATEGORIES = {
    "nuclear": "nuclear weapons OR nuclear threat OR missile",
    "geopolitical": "war OR conflict OR NATO OR military",
    "economic": "recession OR inflation OR market crash OR economic crisis",
    "cyber": "cyberattack OR data breach OR hacking OR ransomware"
}

def fetch_news():
    for category, query in THREAT_CATEGORIES.items():
        url = f"https://newsapi.org/v2/everything?q={query}&pageSize=5&apiKey={NEWS_API_KEY}"
        
        response = requests.get(url)
        data = response.json()
        
        if data["status"] == "ok":          
            for article in data["articles"]:    
                NewsItem.objects.get_or_create( #Prevents duplicate news items being created.
                    headline=article["title"],
                    defaults={
                        "source": article["source"]["name"],
                        "category": category,
                        "ai_score": 0
                    }
                )
            print(f"Fetched {category} news")