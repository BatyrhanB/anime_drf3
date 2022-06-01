from django.urls import path

from . import views


urlpatterns = [
    path("", views.VideoList.as_view(), name='video-list'),
    path("<int:pk>", views.VideoDetail.as_view(), name='video-detail'),
    path("category/", views.CategoryList.as_view(), name='category-list'),
    path("category/<int:pk>", views.CategoryDetail.as_view(), name='category-detail'),
    path("personage/", views.PersonageList.as_view(), name='personage-list'),
    path("personage/<int:pk>", views.PersonageDetail.as_view(), name='personage-detail'),
]