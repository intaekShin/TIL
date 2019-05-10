from rest_framework import serializers
from .models import Genre, Movie, Score


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience', 'poster_url', 'description', 'genre']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
        
class GenreDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many = True)
    class Meta:
        model = Genre
        fields = ['id', 'movies', 'name']
        
# Movie : Score = 1 : N
# score_set 이 기본값. related_name 을 통해서 scores로 변경.        
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'content', 'score']