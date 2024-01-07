from django.http import Http404, HttpRequest
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import array
from rest_framework.decorators import action

from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from .forms import SearchFilmForm
from .models import *
import random
from django_filters import rest_framework as filters

from rest_framework import generics, status, viewsets
from .serializers import ActorSerializer, FilmSerializer, FilmGenreSerializer


class GetGenreAndYear:
    def get_genre(self):
        return Genre.objects.all()

    def get_year(self):
        return Films.objects.values_list("release_film", flat=True).order_by("release_film")


class FilterFilm(GetGenreAndYear, generic.ListView):
    context_object_name = "films"
    paginate_by = 4

    def get_queryset(self):
        year = self.request.GET.getlist("year")
        genre = self.request.GET.getlist("genre")

        combined_q = Q()

        if year:
            year_q = Q(release_film__in=year)
            combined_q &= year_q

        if genre:
            genre_q = Q(genres__in=genre)
            combined_q &= genre_q

        queryset = Films.objects.filter(combined_q)

        return queryset


class FilmUrlFilter(filters.FilterSet):
    genres = filters.CharFilter(field_name='genres__name', lookup_expr='exact')
    genres__icontains = filters.CharFilter(field_name='genres__name', lookup_expr='icontains')

    class Meta:
        model = Films
        fields = []

class FilmIndexAPIView(generics.ListAPIView):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer

class FilmGenreAPIView(generics.ListAPIView):
    serializer_class = FilmGenreSerializer

    def get_queryset(self):
        queryset = Films.objects.all()
        genre_name = self.request.query_params.get("genres")

        if genre_name is not None:
            queryset = queryset.filter(genres__genre=genre_name)
        return queryset

class ActorAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class IndexView(GetGenreAndYear, generic.ListView):
    model = Films
    template_name = 'polls/index.html'
    context_object_name = 'latest_film_list'
    paginate_by = 4

    def get_queryset(self):
        return Films.objects.all().order_by('-rating')


class BestView(generic.ListView):
    model = Films
    template_name = "polls/best.html"
    context_object_name = "best"
    paginate_by = 4

    def get_queryset(self):
        q1 = Q(rating__gte=7.0)

        queryset = Films.objects.filter(q1)

        return queryset


class DetailView(generic.DetailView):
    model = Films
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Фильм'
        context['skip'] = "все"
        return context

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Films.objects.all()
    serializer_class = FilmSerializer

    @action(methods=['get'], detail=False)
    def get_random_film(self, request):
        random_film = Films.objects.order_by('?').first()
        serializer = self.get_serializer(random_film)
        return Response(serializer.data)

    @action(methods=['post'], detail=True)
    def update_rating(self, request, pk=None):
        film = self.get_object()
        new_rating = request.data.get('rating')
        if new_rating:
            try:
                new_rating = float(new_rating)
                if 0 <= new_rating <= 10:
                    old_rating = film.rating
                    film.rating = new_rating
                    film.save()
                    return Response({
                        'status': 'rating updated',
                        'film': film.name,
                        'old_rating': old_rating,
                        'new_rating': new_rating
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Invalid rating'}, status=status.HTTP_400_BAD_REQUEST)
            except ValueError:
                return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No rating provided'}, status=status.HTTP_400_BAD_REQUEST)

class RandomView(generic.ListView):
    template_name = "polls/random.html"
    context_object_name = 'films'

    def get_queryset(self):
        return Films.objects.get(id=random.randint(1, len(Films.objects.all())))

    def get_context_data(self, **kwargs):
        context = super(RandomView, self).get_context_data(**kwargs)
        context['title'] = 'Фильм'
        context['skip'] = "все"
        return context


class SearchFilm(generic.ListView):
    template_name = 'polls/search.html'
    context_object_name = 'result'

    def get_queryset(self):
        return Films.objects.filter(name__icontains=self.request.GET.get('name'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        film = Films.objects.filter(name__icontains=self.request.GET.get('name'))
        for count in film:
            context['count'] = range(len(count.genres.all()) - 3)
        context['skip'] = "все"
        return context


class FilterView(generic.ListView):
    models = Films
    template_name = 'polls/filter.html'
    context_object_name = 'films'
    form_class = SearchFilmForm

    def get_queryset(self):
        # return self.request.GET.get('country')
        return Films.objects.filter(
            country=self.request.GET.get('country'),
            rating__gt=self.request.GET.get('rating', default=0),
            release_film__gt=self.request.GET.get('release_film', False),
            actors=self.request.GET.get('actors'),
            genres=self.request.GET.get('genres')
        )

    def get_context_data(self, **kwargs):
        context = super(FilterView, self).get_context_data(**kwargs)
        context['form'] = SearchFilmForm()
        return context
