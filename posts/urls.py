from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:cpk>/article/<str:pk>', views.article, name='article'),
    path('story/<str:spk>/article/<str:pk>', views.story_article, name='story_article'),
    path('category/stories', views.stories_overview, name='stories'),
    path('category/<str:title>', views.article_overview, name="article_overview"),
    path('objektive/<str:pk>', views.article, name='lenses'),
    path('uebermich/<str:pk>', views.aboutme, name='aboutme'),
]