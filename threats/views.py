from django.shortcuts import render
from django.http import HttpResponse
from .news_fetcher import fetch_news

def fetch_news_view(request):
    fetch_news()
    return HttpResponse("News fetched successfully!")
