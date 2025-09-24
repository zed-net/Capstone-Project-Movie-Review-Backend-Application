from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
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
    
    
    
class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=genres)
    release_date = models.DateField()
    is_family_friendly = models.BooleanField(default=True)
    
    def average_rating(self):
        reviews = self.review_set.all()
        if reviews:
            return sum(review.rating for review in reviews) / reviews.count()
        return 0

    def __str__(self):
        return self.title
    
    
class review(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"{self.user.name} - {self.movie.title}"
