from django.urls import path
from usermodel import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UsersView, 'users')

urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view()),
    path('profile/', views.ProfileAPIView.as_view()),
]
