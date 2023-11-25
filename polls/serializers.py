from rest_framework import serializers

from .models import Films, Actor

class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = ('id', 'name', 'rating')

class FilmGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Films
        fields = ('id', 'name', 'rating')

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'