from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Movie_app import views
from django.db import models

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet,)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'all-movies', views.AllMoviesViewSet, basename='AllMovies')


urlpatterns = [
    path('', include(router.urls)),

]
