from django.db import models
from django.db.models import QuerySet

class Video(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.title} - {self.author}"
  
  @classmethod
  def get_all_videos(cls) -> QuerySet['Video']:
    return cls.objects.all()
