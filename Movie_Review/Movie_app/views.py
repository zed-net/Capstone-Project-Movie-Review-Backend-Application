from .models import Movie, Review
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework import viewsets
from rest_framework import filters
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from rest_framework import generics,permissions
from .permissions import IsOwnerOrAdminOrReadOnly, IsOwnerOrAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Viewset for all movies with search and ordering functionality
class AllMoviesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'genre']
    ordering_fields = ['release_date' ]
#No permission restrictions for viewing all movies
    permission_classes = [permissions.AllowAny]
  
# Viewset for Movie model
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
# Only authenticated users can create, update, or delete movies    
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdminOrReadOnly]

# ties the movie creation to the logged in user
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Viewset for Review model
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 
# Only authenticated users can create, update, or delete reviews and only owners or admins can edit/delete  
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly]
# ties the review creation to the logged in user  
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    
    
#viewset for user registration and authentication
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"],
        )
        return user

#viewset for user registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]