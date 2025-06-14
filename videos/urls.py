from django.urls import path
from . import views

urlpatterns = [
    path('videos/', views.get_all_videos_view, name='all_videos'),
    path('videos/author/<str:author_name>/', views.get_videos_by_author_view, name='videos_by_author'),
    path('videos/keyword/<str:keyword>/', views.get_videos_by_title_keyword_view, name='videos_by_keyword'),
    path('videos/sorted/title/', views.get_videos_ordered_by_title_view, name='videos_ordered_title'),
]