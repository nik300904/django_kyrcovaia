from import_export import resources
from .models import Films

class FilmsResource(resources.ModelResource):
    class Meta:
        model = Films