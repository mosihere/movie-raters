from .models import Movie, Star, Review, Comment, Genre
from core.models import User
from rest_framework import serializers
from . import views

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'imdb_rate', 'director', 'genres', 'total_likes', 'stars', 'reviews']

    stars = serializers.HyperlinkedRelatedField(many=True, view_name='store:star-detail', queryset=Star.objects.all())
    reviews = serializers.HyperlinkedRelatedField(many=True, view_name='store:review-detail', read_only=True)


class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = ['id', 'first_name', 'last_name', 'movies']
    
    movies = serializers.HyperlinkedRelatedField(many=True, view_name='store:movie-detail', queryset=Movie.objects.all())


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'description', 'created_on', 'owner', 'movie', 'total_likes', 'comments']

    movie = serializers.HyperlinkedRelatedField(view_name='store:movie-detail', queryset=Movie.objects.all())
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'review', 'user', 'text', 'created_on']
    
    review = serializers.PrimaryKeyRelatedField(queryset=Review.objects.select_related('owner').all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name', 'movies']
    
    movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)