from rest_framework import serializers
from .models import Movie, review, user
from django.contrib.auth.models import User


class MovieSerializer(serializers.ModelSerializer):
    #average_rating = serializers.FloatField(source='average_rating', read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'release_date', 'is_family_friendly', 'average_rating']
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = ['id', 'user', 'movie', 'rating', 'review_text', 'created_at']
        