from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
  path('videos/', views.video_list, name='video_list'),
  path('videos/<int:video_id>/history/', views.video_history, name='video_history')
]