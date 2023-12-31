from django.urls import path, include

from . import views
from .views import FilmIndexAPIView, ActorAPIView, FilmGenreAPIView, FilmViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'films', FilmViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('films/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('films/random/', views.RandomView.as_view(), name='random'),
    path('films/search/', views.SearchFilm.as_view(), name='search'),
    path('films/filter/', views.FilterView.as_view(), name='filter'),
    path('films/result/', views.FilterView.as_view(), name='result'),
    path('films/best/', views.BestView.as_view(), name='best'),
    path('films/years/', views.FilterFilm.as_view(), name='year'),
    path('api/filmlist', FilmIndexAPIView.as_view()),
    path('api/actorlist', ActorAPIView.as_view()),
    path('api/genre', FilmGenreAPIView.as_view()),
    path('api/random/', FilmViewSet.as_view({'get': 'get_random_film'}), name='random-film'),
    path('', include(router.urls)),
]
