from .models import Movie, review, user
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework import viewsets


class AllMoviesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    

    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = review.objects.all()
    serializer_class = ReviewSerializer 
    