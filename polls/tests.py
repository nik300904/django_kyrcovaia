from django.test import TestCase

from .models import *


def create_film(name, description, release_film, rating):
    return Films.objects.create(name=name, description=description,
                                release_film=release_film, rating=rating)


class FilmIndexViewTests(TestCase):
    def test_index(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_index_empty(self):
        response = self.client.get('').content.decode()
        self.assertIn('No polls are available.', response)

    def test_create_films_and_check_data(self):
        create_film('Бегущий по лезвию', 'Кино', 2009, 8.8)
        table = Films.objects.get(id=1)
        self.assertEquals(table.name, 'Бегущий по лезвию')
        self.assertEquals(table.description, 'Кино')

    def test_create_films_and_view(self):
        create_film('Бегущий по лезвию', 'Кино', 2009, 8.8)
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
        self.assertIn('Бегущий по лезвию', response.content.decode())

class ModelsTests(TestCase):
    def test_create_genre(self):
        test = Genre.objects.create(genre='боевик')
        self.assertEquals(test.genre, 'боевик')

    def test_create_country(self):
        test = Country.objects.create(country='Франция')
        self.assertEquals(test.country, 'Франция')

    def test_create_actor(self):
        test = Actor.objects.create(name='Уильям Дефо')
        self.assertEquals(test.name, 'Уильям Дефо')

    def test_create_director(self):
        test = Director.objects.create(first_name='Квентин', second_name='Тарантино')
        self.assertEquals(test.first_name, 'Квентин')
        self.assertEquals(test.second_name, 'Тарантино')

