from django.db import models

# Create your models here.

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Horror', 'Horror'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    release_date = models.DateField()
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)


