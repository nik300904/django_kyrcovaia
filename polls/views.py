from django.http import Http404, HttpRequest
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import array

from .forms import SearchFilmForm
from .models import *
import random


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_film_list'

    def get_queryset(self):
        return Films.objects.all().order_by('-rating')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Фильмы'
        return context


class DetailView(generic.DetailView):
    model = Films
    template_name = 'polls/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['title'] = 'Фильм'
        context['skip'] = "все"
        return context


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
