from .models import Movie, Star
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'imdb_rate', 'director', 'stars']

    stars = serializers.StringRelatedField(many=True)

class StarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Star
        fields = ['id', 'first_name', 'last_name', 'movies']
    
    movies = serializers.StringRelatedField(many=True)