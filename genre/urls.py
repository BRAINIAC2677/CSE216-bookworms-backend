from django.urls import path 

from .views import GenreListAPIView, GenreCreateAPIView

urlpatterns = [
    path('', GenreListAPIView.as_view(), name='genre-list'),
    path('create/', GenreCreateAPIView.as_view(), name='genre-create'),
]