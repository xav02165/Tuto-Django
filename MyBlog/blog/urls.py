from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.liste_articles, name='liste_articles'),
]