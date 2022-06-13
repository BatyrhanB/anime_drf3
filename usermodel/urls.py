from django.urls import path
from usermodel import views
from rest_framework.routers import DefaultRouter
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view()),
    path('profile/', views.ProfileAPIView.as_view()),
    path('verify-email/', views.VerifyEmail.as_view()),
    path('login/', views.LoginAPIView.as_view()),
]
