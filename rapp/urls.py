from django.urls import path
from .import views

urlpatterns = [
    path('', views.MovieCreateList.as_view(), name='movielist'),
    path('<int:pk>/', views.MovieDetail.as_view(), name='movieDetail'),
]