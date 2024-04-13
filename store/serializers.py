from .models import Movie, Star, Review
from rest_framework import serializers
from . import views

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'imdb_rate', 'director', 'total_likes', 'stars', 'reviews']

    stars = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = ['id', 'first_name', 'last_name', 'movies']
    
    movies = serializers.StringRelatedField(many=True)


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ['id', 'description', 'owner', 'movie', 'total_likes']