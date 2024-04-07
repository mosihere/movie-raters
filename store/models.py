from django.db import models



class Movie(models.Model):
    title = models.CharField(max_length=255)
    imdb_rate = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    director = models.CharField(max_length=255, null=True, blank=True)
    # actors = models.ForeignKey(Star, on_delete=models.PROTECT)