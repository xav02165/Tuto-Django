from django.urls import path, include
from .import views
from .views import ListeArticlesView

urlpatterns = [
    path('', ListeArticlesView.as_view(), name='liste_articles'),
]