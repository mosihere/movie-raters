from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MovieSerializer, StarSerializer
from .models import Movie, Star


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.prefetch_related('stars').all()


class StarViewSet(ModelViewSet):
    serializer_class = StarSerializer
    queryset = Star.objects.prefetch_related('movies').all()