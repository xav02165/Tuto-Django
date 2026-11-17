
from .models import Article
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import ArticleForm


# Create your views here.
#def liste_articles(request):
 #   articles = Article.objects.all() #recupere tous les articles
  #  context = {
   #     'articles': articles
    #}
    #return render(request=request, template_name='blog/liste_articles.html', context=context)


    

class CreerArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/creer_article.html'
    success_url = reverse_lazy('liste_articles') #redirection apres la creation

class ListeArticlesView(ListView):
    model = Article #specifie le modele a utiliser
    template_name = 'blog/liste_articles.html' #specifie le template
    context_object_name = 'articles' #le nom utilisé dans le template

    def get_queryset(self):
        # Récupérer le paramètre "q" dans l'URL
        query = self.request.GET.get('q')
        if query:
            # Tu pourras affiner plus tard avec un .filter(titre__icontains=query)
            return Article.objects.filter(titre__icontains=query)
        
        # TRÈS IMPORTANT : Renvoyer tous les articles si aucune recherche n'est active
        return Article.objects.all()