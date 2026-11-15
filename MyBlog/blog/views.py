from django.shortcuts import render
from .models import Article
# C
# reate your views here.
def liste_articles(request):
    articles = Article.objects.all() #recupere tous les articles
    context = {
        'articles': articles
    }
    return render(request=request, template_name='blog/liste_articles.html', context=context)
