from django.db import models

# Create your models here.
class News(models.Model):

    title = models.CharField(max_length=200)
    source = models.CharField(max_length=100)
    link = models.URLField()
    image = models.CharField(max_length=300)
    
    #Lineas a considerar para el valor de sentimiento
    #sentiment = models.CharField(max_length=100)   
    #sentiment_int = models.IntegerField()

    def __str__(self):
        return f'{self.source} - {self.title}'