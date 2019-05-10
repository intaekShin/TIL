from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name = 'movies')
    
    def __str__(self):
        return self.title
    
    
class Score(models.Model):
    content = models.TextField()
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)