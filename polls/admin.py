from django.contrib import admin

from .models import *

admin.site.register(Image)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Country)
admin.site.register(Genre)


# Register your models here.

@admin.register(Films)
class FilmsAdmin(admin.ModelAdmin):
    filter_horizontal = ['actors', 'country', 'genres']
