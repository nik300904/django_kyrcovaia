from import_export import resources, fields
from .models import Films

class FilmsResource(resources.ModelResource):
    director_name = fields.Field(
        attribute='director',
        column_name='director_name'
    )

    class Meta:
        model = Films
        fields = ('id', 'name', 'description', 'release_film', 'rating', 'director_name', 'actors', 'genres', 'country')  # Указание конкретных полей
        export_order = ('id', 'name', 'description', 'release_film', 'rating', 'director_name', 'actors', 'genres', 'country')  # Указание порядка экспорта полей

    def dehydrate_director_name(self, film):
        return film.director.first_name if film.director else 'Неизвестный'

    def get_export_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(rating__gt=7)

    def dehydrate_description(self, film):
        return f"{film.description} (Экспортировано из системы)"