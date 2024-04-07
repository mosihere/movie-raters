from django.db import models



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

    def __str__(self) -> str:
        return self.title