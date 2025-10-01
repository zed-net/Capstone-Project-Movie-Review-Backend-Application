from .models import Movie, review, user
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework import viewsets
from rest_framework import filters
from django.db.models import Avg



class AllMoviesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'genre']
    ordering_fields = ['release_date' ]
    
  

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = review.objects.all()
    serializer_class = ReviewSerializer 
    