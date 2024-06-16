from django.urls import path, include

from . import views
from .views import FilmIndexAPIView, ActorAPIView, FilmGenreAPIView, FilmViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import view_cache
from .views import clear_film_cache

router = DefaultRouter()
router.register(r'films', FilmViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('cache/', view_cache, name='view_cache'),
    path('cache/clear', clear_film_cache, name='clear_film_cache'),
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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
]
