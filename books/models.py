from django.db import models
from django.db.models import QuerySet

class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.title} - {self.author}"
  
  @classmethod
  def get_all_books(cls) -> QuerySet['Book']:
    return cls.objects.all()
