from django.db import models
import datetime


class Actor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Director(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    second_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Country(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.country}'


class Genre(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.genre}'


class Films(models.Model):
    name = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    description = models.CharField(max_length=500, null=True)
    release_film = models.CharField(max_length=50, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    id = models.AutoField(primary_key=True, blank=True)
    actors = models.ManyToManyField(Actor, blank=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True)
    country = models.ManyToManyField(Country)

    def __str__(self):
        return self.name


class Image(models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE, null=True)
    image = models.ImageField()

    def __str__(self):
        return f'Баннер фильма "{self.film.name}"'


