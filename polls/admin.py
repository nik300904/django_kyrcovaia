from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ExportMixin
from simple_history.admin import SimpleHistoryAdmin

from .models import *
from .resources import FilmsResource

class GenreInline(admin.TabularInline):
    model = Films.genres.through
    extra = 1

@admin.register(Films)
class FilmsAdmin(ExportMixin, SimpleHistoryAdmin):
    model = Films
    filter_horizontal = ['actors', 'country', 'genres']
    fieldsets = [
        ('Основное', {'fields': ['name', 'genres', 'description']}),
        ('Дата выхода', {'fields': ['release_film']}),
        ('Рейтинг', {'fields': ['rating']}),
        ('Люди', {'fields': ['actors', 'director']}),
        ('Страна', {'fields': ['country']})
    ]
    list_display = ('id', 'name', 'description', 'release_film', 'rating', 'director')
    list_display_links = ('name', 'director')
    list_filter = ['rating']
    search_fields = ['name']
    readonly_fields = ('name', 'release_film', 'director')
    resource_class = FilmsResource
    inlines = [GenreInline]

    def get_export_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(rating__gt=7)

    def dehydrate_description(self, film):
        return f"{film.description} (Экспортировано из системы)"

    def get_director_name(self, film):
        return film.director.full_name if film.director else 'Неизвестный'


class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ("film",)
    list_display = ('film', 'get_photo')

    def get_photo(self, object):
        return mark_safe(f"<img src='/media/{object.image}' width=80>")

    get_photo.short_description = "Баннер"


admin.site.register(Image, ImageAdmin)
admin.site.register(Director)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Actor)

