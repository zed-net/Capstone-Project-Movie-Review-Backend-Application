from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone






    
genres = [
        ('Action', 'Action'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Documentary', 'Documentary'), 
        ('Thriller', 'Thriller'),
        ('Animation', 'Animation'),
        ('Fantasy', 'Fantasy'),
        ('Mystery', 'Mystery'),
        ('Adventure', 'Adventure'),
        ('Crime', 'Crime'),
        ('Musical', 'Musical'),
        ('War', 'War'),
        ('Western', 'Western'),
        ('Biography', 'Biography'),
        ('Family', 'Family'),
        ('Sport', 'Sport'),
        ('History', 'History'),
    ]
family_friendly_choices = [
        (True, 'Yes'),
        (False, 'No'),
    ]    
    
    
class Movie(models.Model):
    title = models.CharField(max_length=200,unique=True)
    genre = models.CharField(max_length=50, choices=genres)
    release_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movies', null=True)
    def average_rating(self):
        reviews = self.review_set.all()
        if reviews:
            return sum(review.rating for review in reviews) / reviews.count()
        return 0

    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    family_friendly = models.BooleanField(choices=family_friendly_choices, default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return  f"{self.user.username} - {self.movie.title}"
