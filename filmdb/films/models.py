from django.db import models
from django.db.models import Avg


class Movie(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(default='')
    image_url = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    avg_rating = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True)
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.SET_NULL)
    genres = models.ManyToManyField('Genre', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.year})"

    def genres_display(self):
        return ", ".join([i.name for i in self.genres.all()])

    def update_avg_rating(self):
        avg_rating = self.comment_set.aggregate(Avg('rating'))['rating__avg']
        self.avg_rating = avg_rating
        self.save()


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    author = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    rating = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.movie.update_avg_rating()

class Director(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='')
    birth_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.birth_year})"


class Actor(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(default='')
    photo_url = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    movies = models.ManyToManyField('Movie', related_name='actors')

    def __str__(self):
        return f"{self.name} ({self.birth_year})"

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
