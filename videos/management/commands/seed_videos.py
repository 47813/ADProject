from django.core.management.base import BaseCommand
from videos.models import Video

class Command(BaseCommand):
    help = 'Insert sample videos'

    def handle(self, *args, **kwargs):
        Video.objects.create(title='Inception', author='Christopher Nolan')
        Video.objects.create(title='The Matrix', author='Lana Wachowski, Lilly Wachowski')
        Video.objects.create(title='Parasite', author='Bong Joon-ho')
        Video.objects.create(title='Interstellar', author='Christopher Nolan')
        Video.objects.create(title='Spirited Away', author='Hayao Miyazaki')
        Video.objects.create(title='The Godfather', author='Francis Ford Coppola')
        Video.objects.create(title='Pulp Fiction', author='Quentin Tarantino')
        Video.objects.create(title='The Dark Knight', author='Christopher Nolan')
        Video.objects.create(title='Fight Club', author='David Fincher')
        Video.objects.create(title='Forrest Gump', author='Robert Zemeckis')
        self.stdout.write(self.style.SUCCESS('Sample videos inserted!'))
