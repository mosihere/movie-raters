from django.db import models
from django.contrib.auth.models import User


class Star(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Movie(models.Model):
    title = models.CharField(max_length=255)
    imdb_rate = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    stars = models.ManyToManyField(Star, blank=True, related_name='movies')
    likes = models.ManyToManyField(User, related_name='liked_movies', blank=True)

    def __str__(self) -> str:
        return self.title
    
    def total_likes(self):
        return self.likes.count()

class Review(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_list')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self) -> str:
        return f'Review {self.description} by {self.owner}'

    def total_likes(self):
        return self.likes.count()