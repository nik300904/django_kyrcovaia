from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
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
    readonly_fields = ('name', 'release_film' ,'director')


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

