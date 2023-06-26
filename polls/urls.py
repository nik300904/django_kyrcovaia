from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('films/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('films/random/', views.RandomView.as_view(), name='random'),
    path('films/search/', views.SearchFilm.as_view(), name='search'),
    path('films/filter/', views.FilterView.as_view(), name='filter'),
    path('films/result/', views.FilterView.as_view(), name='result'),
]
