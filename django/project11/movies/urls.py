from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('', views.index),
    path('docs/', get_swagger_view(title='API Docs')),
    path('genres/', views.genre_list),
    path('genres/<int:genre_pk>/', views.genre_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/scores/', views.score_create),
    path('scores/<int:score_pk>/', views.score_update_and_delete),
    ]
