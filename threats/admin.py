from django.contrib import admin
from .models import ThreatScore, NewsItem, AISummary

admin.site.register(ThreatScore)
admin.site.register(NewsItem)
admin.site.register(AISummary)
