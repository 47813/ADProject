from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.urls import path
from . import views

@ensure_csrf_cookie
def set_csrf_token(request):
    return JsonResponse({"message": "CSRF cookie set"})

urlpatterns = [
  path('login/', views.LoginAPIView.as_view(), name='login'),
  path('logout/', views.LogoutAPIView.as_view(), name='logout'),
  path('home/', views.HomeAPIView.as_view(), name='home'),
  path('csrf/', set_csrf_token, name='set_cstf_token'),
]