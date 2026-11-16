from django.shortcuts import render
from .models import Article
from django.views.generic import ListView

# Create your views here.
#def liste_articles(request):
 #   articles = Article.objects.all() #recupere tous les articles
  #  context = {
   #     'articles': articles
    #}
    #return render(request=request, template_name='blog/liste_articles.html', context=context)

class ListeArticlesView(ListView):
    model = Article #specifie le modele a utiliser
    template_name = 'blog/liste_articles.html' #specifie le template
    context_object_name = 'articles' #le nom utilisé dans le template