from django.contrib import admin
from .models import Article, Image, Tag, Category, Story, Lens, Camera, Film, Scanner, ArticleLinker


class ArticleAdmin(admin.ModelAdmin): # ermöglicht das zuweisen von Bildern zu einem Artikel
    list_display = ('title',)
    filter_horizontal = ('images',)

class StoryAdmin(admin.ModelAdmin): 
    list_display = ('title',)
    filter_horizontal = ('chapters',)

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Story, StoryAdmin)
admin.site.register(Lens)
admin.site.register(Camera)
admin.site.register(Film)
admin.site.register(Scanner)
admin.site.register(ArticleLinker)



