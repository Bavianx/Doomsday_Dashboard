from .models import NewsItem, ThreatScore
from django.db.models import Avg

WEIGHTS = {         #Defined weights per categorical event which can occur.
    "nuclear": 0.35,
    "geopolitical": 0.25,
    "economic": 0.25,
    "cyber": 0.15
}

def calculate_global_risk():
    category_scores = {}
    
    for category in WEIGHTS.keys():     #loops through each category
        avg = NewsItem.objects.filter(      #Filters for the category news
            category=category           
        ).aggregate(Avg('ai_score'))['ai_score__avg']       #Calculates the average AI score across all items within the sub-category
        category_scores[category] = round(avg or 0, 2)     #stores the average score for the category. Content is either the average or 0 for no news within the category
    
    global_score = sum(
        category_scores[cat] * weight           #Multiplies the category score by the weight of the category and the sum of all of these items
        for cat, weight in WEIGHTS.items()
    )
    
    print(f"Category scores: {category_scores}")

    ThreatScore.objects.create(     #Saves the calculated global score to the db and creates a new threatscore record each time its ran 
        category="global",
        score=round(global_score, 2) # Provides historical tracking of the change over time
    )
    
    print(f"Global score: {global_score}")
    print(f"Global risk score: {round(global_score, 2)}")
    return round(global_score, 2)

    