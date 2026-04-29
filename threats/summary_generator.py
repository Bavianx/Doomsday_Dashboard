from .models import NewsItem, ThreatScore, AISummary
from django.db.models import Avg

def generate_summary():
    # Get latest scores from the category items similar to the risk_calc but we arent leveraging weight.keys() just previous values stored
    scores = {}
    for category in ["nuclear", "geopolitical", "economic", "cyber"]:   
        avg = NewsItem.objects.filter(
            category=category
        ).aggregate(Avg('ai_score'))['ai_score__avg']
        scores[category] = round(avg or 0, 2)
    
    global_score = ThreatScore.objects.filter(
        category="global"
    ).order_by('-created_at').first()       #Gathers the latest threatscore within the global category (last stored value)
    
    # Generate summary text
    summary_text = f"""
    GLOBAL THREAT ASSESSMENT
    Global Risk Score: {global_score.score if global_score else 'N/A'}/10
    
    Nuclear Threat: {scores['nuclear']}/10
    Geopolitical Tension: {scores['geopolitical']}/10
    Economic Instability: {scores['economic']}/10
    Cyber Threat Level: {scores['cyber']}/10
    
    Latest Headlines:
    """
    
    recent_news = NewsItem.objects.order_by('-created_at')[:5]
    for item in recent_news:
        summary_text += f"\n- [{item.category.upper()}] {item.headline} (Score: {item.ai_score})"
    
    AISummary.objects.create(
        content=summary_text,
        global_score=global_score.score if global_score else 0
    )
    
    print("Summary generated!")
    return summary_text