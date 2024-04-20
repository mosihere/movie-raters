from .models import Movie, Star, Review
from rest_framework import serializers
from . import views

class MovieSerializer(serializers.ModelSerializer):


    class Meta:
        model = Movie
        fields = ['id', 'title', 'imdb_rate', 'director', 'total_likes', 'stars', 'reviews']

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
        fields = ['id', 'description', 'owner', 'movie', 'total_likes']

    movie = serializers.HyperlinkedRelatedField(view_name='store:movie-detail', queryset=Movie.objects.all())
