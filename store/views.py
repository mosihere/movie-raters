from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MovieSerializer, StarSerializer, ReviewSerializer
from .models import Movie, Star, Review


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.prefetch_related('stars').prefetch_related('likes').prefetch_related('reviews').all()

    def get_serializer_context(self):
        return {'request': self.request}


class StarViewSet(ModelViewSet):
    serializer_class = StarSerializer
    queryset = Star.objects.prefetch_related('movies').all()

    def get_serializer_context(self):
        return {'request': self.request}
    

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.select_related('owner').select_related('movie').prefetch_related('likes').all()
