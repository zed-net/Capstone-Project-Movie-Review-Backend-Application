from rest_framework import serializers
from .models import Movie, review, user
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'release_date',  'average_rating']
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = ['id', 'movie', 'rating', 'review_text', 'family_friendly', 'created_at'] # 'user'
        
        
        