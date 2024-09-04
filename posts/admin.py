from django.contrib import admin
from .models import Article, Image, Tag, Category, Story, Lens, Camera, Film, Scanner, ArticleLinker, ArticleImage

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1
    fields = ('image', 'order')
    ordering = ('order',)

class ArticleAdmin(admin.ModelAdmin): # ermöglicht das zuweisen von Bildern zu einem Artikel
    list_display = ('title',)
    inlines = (ArticleImageInline,)

class StoryAdmin(admin.ModelAdmin): 
    list_display = ('title',)
    filter_horizontal = ('chapters',)
    
class CameraAdmin(admin.ModelAdmin): 
    list_display = ('title',)
    filter_horizontal = ('similar_cameras', 'related_cameras')

    


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Image)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Story, StoryAdmin)
admin.site.register(Lens)
admin.site.register(Camera, CameraAdmin)
admin.site.register(Film)
admin.site.register(Scanner)
admin.site.register(ArticleLinker)




