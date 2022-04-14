from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/challengeInfo', views.challenge, name='challengeInfo'),
    path('create/', views.create, name='create'),
    path('comment/', views.comment, name='comment'),
]