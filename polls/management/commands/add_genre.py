from django.core.management.base import BaseCommand, CommandError
from polls.models import Genre

class Command(BaseCommand):
    help = 'Добавляет новый жанр в модель Genre'

    def add_arguments(self, parser):
        parser.add_argument('genre_name', type=str, help='Название добавляемого жанра')

    def handle(self, *args, **options):
        genre_name = options['genre_name']
        if Genre.objects.filter(genre=genre_name).exists():
            self.stdout.write(self.style.ERROR('Жанр "%s" уже существует' % genre_name))
        else:
            Genre.objects.create(genre=genre_name)
            self.stdout.write(self.style.SUCCESS('Жанр "%s" успешно добавлен' % genre_name))
