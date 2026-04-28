from django.urls import path
from . import views

urlpatterns = [
    path('fetch-news/', views.fetch_news_view, name='fetch_news'),
    path('score-news/', views.score_news_view, name='score_news'),
    path('avg_news_score/', views.avg_news_score, name='avg_news_score'),
]