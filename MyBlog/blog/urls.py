from django.urls import path, include
from .import views
from .views import ListeArticlesView, CreerArticleView

urlpatterns = [
    path('', ListeArticlesView.as_view(), name='liste_articles'),
    path('nouveau/', CreerArticleView.as_view(), name='creer_article'),
]