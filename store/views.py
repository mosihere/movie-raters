from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MovieSerializer
from .models import Movie


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()