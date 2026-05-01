from .models import NewsItem, ThreatScore, AISummary
from django.shortcuts import render
from django.http import HttpResponse
from .news_fetcher import fetch_news
from .AI_Scorer import score_news_items
from .risk_calculator import calculate_global_risk
from .summary_generator import generate_summary
from django.db.models import Avg
import yfinance as yf
import math, requests
from decouple import config

def dashboard(request):
    query = request.GET.get('q', '')    #Checks the URL for a query and a requested search after, else returns default (maximises content efficiency)
    is_search = False
    market_news = []
    news_api_key = config('NEWS_API_KEY') # Live market news from NewsAPI displaying World stock news

    if query:           #Incomplete query requests ( Search function does work and refreshes applications main page but doesnt pull data for specific query within the dashboard)
        threat_response = requests.get(
            f'https://newsapi.org/v2/everything?q="{query}"&language=en&pageSize=10&sortBy=publishedAt&apiKey={news_api_key}'
        )
        raw_articles = threat_response.json().get('articles', [])   
        news_items = [ #Normalises the NewsAPI response to match the NewsItem structure created so the template can display both pieces of data without it causing internal errors
            {
                'headline': article.get('title', 'No title'), #NewsItem Structure: NewsAPI (just converts it)
                'ai_score': '',
                'category': 'search',
                'url': article.get('url', '#') #NewsItem Structure: NewsAPI (just converts it)
            }
            for article in raw_articles
        ]

        market_response = requests.get(
            f"https://newsapi.org/v2/everything?q={query}+market+economy&language=en&pageSize=10&sortBy=publishedAt&apiKey={news_api_key}"
        )
        market_news = market_response.json().get('articles', [])
        is_search = True

    else:
        news_items = NewsItem.objects.order_by('-created_at')[:10]  #Default data displayed incase users dont search
        market_response = requests.get(
            f"https://newsapi.org/v2/everything?q=stock+market+finance+economy&language=en&pageSize=10&sortBy=publishedAt&apiKey={news_api_key}"
        )
        market_news = market_response.json().get('articles', [])
        is_search = False
    
    # Get category scores
    category_scores = {}
    for category in ["nuclear", "geopolitical", "economic", "cyber"]:   
        avg = NewsItem.objects.filter(category=category).aggregate(Avg('ai_score'))['ai_score__avg']  #Django ORM identifying the newsitem objects within the db to the category name within the loop
        category_scores[category] = round(avg or 0, 2)
    
    # Get latest global score
    global_score = ThreatScore.objects.filter(category="global").order_by('-created_at').first() #ORM gathers the last Threatscore of each category to identify the global risk score

    score_value = global_score.score if global_score else 5.0       #Grab the current global risk score or set a default of 5 to minimise broken display
    angle_rad = math.radians((score_value / 10) * 180 + 90)  #radian = the current global risk score / 10 (max global risk score) * 180 degrees + 90 (computer only reads radian)
    tip_x = round(200 + 150 * math.sin(angle_rad), 2)       #200 will be the size of the SVG clock and 150 is the size of the hand 
    tip_y = round(200 - 150 * math.cos(angle_rad), 2)
    
    # Get latest AI summary
    summary = AISummary.objects.order_by('-generated_at').first()
        
    # Fetch ticker data
    tickers = ['SPY', 'QQQ', 'GLD', 'USO']
    ticker_data = []
    
    for symbol in tickers:
        stock = yf.Ticker(symbol)
        history = stock.history(period='1d') #identifies the previous day history 
        if not history.empty:
            price = round(history['Close'].iloc[-1], 2) #identifies the close price from the df and gets the latest value to 2dp
            change = round(history['Close'].iloc[-1] - history['Open'].iloc[-1], 2) #identifies the close price from the df and gets the latest value to 2dp
            ticker_data.append({
                'symbol': symbol,
                'price': price,
                'change': change
            })

    context = {                 #Context dictionary holds commonly requested data for HTML pages
        'news_items': news_items,
        'category_scores': category_scores,
        'global_score': global_score,
        'summary': summary,
        'ticker_data': ticker_data,
        'tip_x': tip_x,        
        'tip_y': tip_y,        
        'score_value': score_value,
        'market_news': market_news,
        'query': query,
        'is_search': is_search,
    }
    return render(request, 'threats/dashboard.html', context)


#Test views to ensure the bridge between models, views and URLs were all working
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

