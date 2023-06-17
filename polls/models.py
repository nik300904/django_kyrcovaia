from django.db import models


class Films(models.Model):
    name = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    release_film = models.CharField(max_length=255)
    description = models.CharField(max_length=500, null=True)
    rating = models.FloatField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    film = models.ForeignKey(Films, on_delete=models.CASCADE, null=True)
    image = models.ImageField()
