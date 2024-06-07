from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MovieSerializer, StarSerializer, ReviewSerializer, CommentSerializer
from .models import Movie, Star, Review, Comment
from .pagination import DefaultPagination


class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.prefetch_related('stars', 'likes', 'reviews').all()
    pagination_class = DefaultPagination

    def get_serializer_context(self):
        return {'request': self.request}


class StarViewSet(ModelViewSet):
    serializer_class = StarSerializer
    queryset = Star.objects.prefetch_related('movies').all()
    pagination_class = DefaultPagination

    def get_serializer_context(self):
        return {'request': self.request}
    

class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.select_related('owner').select_related('movie').prefetch_related('likes').all()
    pagination_class = DefaultPagination



class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.select_related('review', 'user').all()
    pagination_class = DefaultPagination
