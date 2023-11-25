from django.db import models
import datetime

from simple_history.models import HistoricalRecords


class Actor(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя и Фамилия')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Актёры'
        verbose_name_plural = 'Актёры'


class Director(models.Model):
    first_name = models.CharField(max_length=255, null=True, verbose_name='Имя')
    second_name = models.CharField(max_length=255, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.first_name} {self.second_name}'

    class Meta:
        verbose_name = 'Режиссеры'
        verbose_name_plural = 'Режиссеры'


class Country(models.Model):
    country = models.CharField(max_length=50, verbose_name='Страна')

    def __str__(self):
        return f'{self.country}'

    class Meta:
        verbose_name = 'Страны'
        verbose_name_plural = 'Страны'


class Genre(models.Model):
    genre = models.CharField(max_length=50, verbose_name='Жанр')

    def __str__(self):
        return f'{self.genre}'

    class Meta:
        verbose_name = 'Жанры'
        verbose_name_plural = 'Жанры'


class Films(models.Model):
    history = HistoricalRecords()
    name = models.CharField(max_length=255, verbose_name='Название')
    genres = models.ManyToManyField(Genre, verbose_name='Жанр')
    description = models.CharField(max_length=500, null=True, verbose_name='Описание')
    release_film = models.CharField(max_length=50, null=True, blank=True, verbose_name='Дата выхода')
    rating = models.FloatField(null=True, blank=True, verbose_name='Рейтинг')
    id = models.AutoField(primary_key=True, blank=True)
    actors = models.ManyToManyField(Actor, blank=True, verbose_name='Актеры')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Режиссер')
    country = models.ManyToManyField(Country, verbose_name='Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фильмы'
        verbose_name_plural = 'Фильмы'
        ordering = ['id']


class Image(models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE, null=True, verbose_name='Фильм')
    image = models.ImageField(verbose_name='Баннер')

    def __str__(self):
        return f'Баннер фильма "{self.film.name}"'

    class Meta:
        verbose_name = 'Баннеры'
        verbose_name_plural = 'Баннеры'
