from django.urls import path

from .views import MoviesDetailApi, MoviesListApi

urlpatterns = [
    path("movies/", MoviesListApi.as_view()),
    path("movies/<uuid:id>", MoviesDetailApi.as_view()),
]
