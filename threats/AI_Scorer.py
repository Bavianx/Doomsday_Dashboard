import anthropic
from decouple import config
from .models import NewsItem, ThreatScore

client = anthropic.Anthropic(api_key=config('ANTHROPIC_API_KEY'))

import random
from .models import NewsItem

def score_news_items():                                     #Randomised fake testing approach before buying Anthropic API credits for real testing
    unscored = NewsItem.objects.filter(ai_score=0)
    
    for item in unscored:   
        item.ai_score = round(random.uniform(3, 9), 1)
        item.save()
        print(f"Scored: {item.headline[:50]} → {item.ai_score}")
    
    print(f"Scored {unscored.count()} items")