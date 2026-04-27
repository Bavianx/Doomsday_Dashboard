from django.db import models

class ThreatScore(models.Model):
    category = models.CharField(max_length=50)  # nuclear, economic, etc (short value)
    score = models.FloatField()                  # 0-10 risk score
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category}: {self.score}"
    

class NewsItem(models.Model):
    headline = models.TextField()  #Allows for unlimited field length (long values)
    source = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    ai_score = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.headline[:50]
    
class AISummary(models.Model):
    content = models.TextField()        #Allows for unlimited field length (long values)
    global_score = models.FloatField()
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Summary {self.generated_at}"