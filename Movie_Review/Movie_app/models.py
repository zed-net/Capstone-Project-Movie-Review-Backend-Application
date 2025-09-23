from django.db import models



class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class movie(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.title
    
    
class review(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user.name} - {self.movie.title}"
