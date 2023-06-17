from django.http import Http404
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import *


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_film_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Films.objects.all()


class DetailView(generic.DetailView):
    model = Films
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Films
    template_name = 'polls/results.html'
