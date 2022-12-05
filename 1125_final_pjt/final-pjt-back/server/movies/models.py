from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Movie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=200, null=True)
    genre_ids = models.ManyToManyField(Genre)
    original_language = models.CharField(max_length=20)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=200)
    release_date = models.DateField()
    title = models.CharField(max_length=100)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)