from django.urls import path
from .views import RequestInfoAPIView, FileUploadAPIView

urlpatterns = [
  path('request_info/', RequestInfoAPIView.as_view(), name='request_info'),
  path('upload/', FileUploadAPIView.as_view(), name='upload_file')
]