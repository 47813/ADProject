from django.core.management.base import BaseCommand
from books.models import Book

class Command(BaseCommand):
    help = 'Insert sample books'

    def handle(self, *args, **kwargs):
        Book.objects.create(title='1984', author='George Orwell')
        Book.objects.create(title='Brave New World', author='Aldous Huxley')
        Book.objects.create(title='Fahrenheit 451', author='Ray Bradbury')
        Book.objects.create(title='To Kill a Mockingbird', author='Harper Lee')
        Book.objects.create(title='The Catcher in the Rye', author='J.D. Salinger')
        Book.objects.create(title='The Great Gatsby', author='F. Scott Fitzgerald')
        Book.objects.create(title='Moby-Dick', author='Herman Melville')
        Book.objects.create(title='Pride and Prejudice', author='Jane Austen')
        Book.objects.create(title='The Hobbit', author='J.R.R. Tolkien')
        Book.objects.create(title='The Lord of the Rings', author='J.R.R. Tolkien')
        self.stdout.write(self.style.SUCCESS('Sample books inserted!'))
