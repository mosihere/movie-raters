from django.contrib import admin
from .models import Movie, Star, Review


admin.site.register(Movie)
admin.site.register(Star)
admin.site.register(Review)