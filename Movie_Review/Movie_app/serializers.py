from rest_framework import serializers, generics
from .models import Movie, Review
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.serializers import ModelSerializer
from django.shortcuts import redirect

#serilaztion for movie model
class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'release_date',  'average_rating']
        read_only_fields = ['owner']
        
    def create(self, validated_data):
        # Assign the current user as the owner automatically
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['owner'] = request.user
        return Movie.objects.create(**validated_data)    
        
#serilaztion for review model        
class ReviewSerializer(serializers.ModelSerializer):
    #movie = serializers.StringRelatedField(read_only=True)
    movie_title = serializers.StringRelatedField(source='movie', read_only=True)
    owner = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Review
        fields = ['id','movie_title', 'owner','movie' ,'review_text', 'rating', 'family_friendly', 'created_at']
        read_only_fields = ['owner', 'created_at']

    family_friendly = serializers.SerializerMethodField()  # changinging the true/false to yes/no
    def get_family_friendly(self, obj):
        return "Yes" if obj.family_friendly else "No"

#serilaztion for users with inbuilt user model      
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

#serilaztion for registration
class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user