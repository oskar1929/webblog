from django.shortcuts import render
from .models import Article, Story, Category, ArticleLinker, Image
from django.shortcuts import render, get_object_or_404

# Create your views here.
# those functions get called in urls.py
# hand over data to html here 
# data from Databank (Admin) is handed over by referencing 
#  classes from modules.py that are migrated (python manage.py makemigrations, migrate)


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all().order_by('-updated_at')
    stories = Story.objects.all()

    return render(request, 'index.html', {
        'articles': articles, 
        'stories': stories, 
        'categories': categories,
    })

def stories_overview(request,):
    stories = Story.objects.all()
    categories = Category.objects.all()
    return render(request, 'stories_overview.html', {
        'stories': stories, 
        'categories': categories
    })

def article(request, pk, cpk):
    article = Article.objects.get(id=pk) # holt den Artikel mit der entsprechenden ID die im Link stand
    images = article.images.all() #ArticleImage.objects.filter(article=article).order_by('order')
    articles = Article.objects.all()
    category = Category.objects.get(title=cpk)
    categories = Category.objects.all()
    articleLinkers = ArticleLinker.objects.all()
    allimages = Image.objects.all()
    alllinkers = ArticleLinker.objects.all()
    linker = ArticleLinker.objects.filter(article=article)   
    return render(request, article.html_template, {
        'article': article,
        'category': category,
        'linkers': articleLinkers,
        'categories': categories, 
        'articles': articles,
        'linker': linker,
        'allimages': allimages,
        'images': images,
        'alllinkers': alllinkers,
    })

def aboutme(request, pk):
    categories = Category.objects.all()
    article = Article.objects.get(id=pk)

    return render(request, article.html_template, {
        'article': article,
        'categories': categories, 
    })

def story_article(request, pk, spk):
    story = Story.objects.get(id=spk)
    categories = Category.objects.all()
    article = Article.objects.get(id=pk) # holt den Artikel mit der entsprechenden ID die im Link stand
    articleLinkers = ArticleLinker.objects.all()
    return render(request, article.html_template, {
        'article': article,
        'story': story,
        'linkers': articleLinkers,
        'categories': categories, 
    })

def article_overview(request, title):
    category = get_object_or_404(Category, title=title)
    categories = Category.objects.all()
    articles = Article.objects.filter(category=category)
    return render(request, 'article_overview.html', {
        'category': category, 
        'categories': categories, 
        'articles': articles
    })


