from django.shortcuts import render, get_object_or_404
from .models import Genre, Movie, Score
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import GenreSerializer, GenreDetailSerializer, MovieSerializer, ScoreSerializer

# Create your views here.

def index(request):
    return render(request, 'index.html')

@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializers = GenreSerializer(genres, many = True)  # 여러개가 들어가도 괜찮아~!
    return Response(serializers.data)
    
@api_view(['GET'])    
def genre_detail(request, genre_pk):
    genre = get_object_or_404(Genre, id = genre_pk)
    serializers = GenreDetailSerializer(genre)
    return Response(serializers.data)
    
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializers = MovieSerializer(movies, many = True)
    return Response(serializers.data)
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, id = movie_pk)
    serializers = MovieSerializer(movie)
    return Response(serializers.data)
    
@api_view(['POST'])
def score_create(request, movie_pk):
    serializers = ScoreSerializer(data = request.data)
    if serializers.is_valid(raise_exception=True):
        serializers.save(movie_id = movie_pk)   # save 메소드는 실제 데이터 베이스에 저장 되기 때문에 앞 변수가 model에 존재하는 column이어야 한다.
    return Response({"message":"작성되었습니다."})
	
	
@api_view(['PUT', 'DELETE'])
def score_update_and_delete(request, score_pk):
	score = get_object_or_404(Score, id = score_pk)
	if request.method == 'PUT':
		serializers = ScoreSerializer(data = request.data, instance = score)
	if serializers.is_valid(raise_exception=True):
	    serializers.save()
	    return Response({"message":"수정되었습니다."})
	else:
		score.delete()
		return Response({"message":"삭제되었습니다."})
		