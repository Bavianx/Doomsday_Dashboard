from .models import NewsItem, ThreatScore, AISummary
from django.shortcuts import render
from django.http import HttpResponse
from .news_fetcher import fetch_news
from .AI_Scorer import score_news_items
from .risk_calculator import calculate_global_risk
from .summary_generator import generate_summary
import yfinance as yf

def fetch_news_view(request):
    fetch_news()
    return HttpResponse("News fetched successfully!")

def score_news_view(request):
    score_news_items()
    return HttpResponse("News scored successfully!")

def avg_news_score(request):
    calculate_global_risk()
    return HttpResponse("Global risk score calculated!")

def generate_summary_view(request):
    generate_summary()
    return HttpResponse("Summary created successfully!")

def dashboard(request):
    # Get latest news items
    news_items = NewsItem.objects.order_by('-created_at')[:10]
    
    # Get category scores
    category_scores = {}
    for category in ["nuclear", "geopolitical", "economic", "cyber"]:
        from django.db.models import Avg
        avg = NewsItem.objects.filter(
            category=category
        ).aggregate(Avg('ai_score'))['ai_score__avg']
        category_scores[category] = round(avg or 0, 2)
    
    # Get latest global score
    global_score = ThreatScore.objects.filter(
        category="global"
    ).order_by('-created_at').first()
    
    # Get latest AI summary
    summary = AISummary.objects.order_by('-generated_at').first()
        
    # Fetch ticker data
    tickers = ['SPY', 'QQQ', 'GLD', 'USO']
    ticker_data = []
    
    for symbol in tickers:
        stock = yf.Ticker(symbol)
        history = stock.history(period='1d') #identifies the previous day
        if not history.empty:
            price = round(history['Close'].iloc[-1], 2)
            change = round(history['Close'].iloc[-1] - history['Open'].iloc[-1], 2)
            ticker_data.append({
                'symbol': symbol,
                'price': price,
                'change': change
            })
    context = {
        'news_items': news_items,
        'category_scores': category_scores,
        'global_score': global_score,
        'summary': summary,
        'ticker_data': ticker_data,
    }
    
    return render(request, 'threats/dashboard.html', context)

