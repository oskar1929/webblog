from django.db import models
from datetime import datetime


# Create your models here.
    
class Lens(models.Model):
    title = models.CharField(max_length=5000, null=True, blank=True)
    manufacturer = models.CharField(max_length=5000, null=True, blank=True)
    modell = models.CharField(max_length=5000, null=True, blank=True)
    focallength = models.CharField(max_length=5000, null=True, blank=True)
    aperature = models.CharField(max_length=5000, null=True, blank=True)
    first_production = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.title} - (id: {self.id})" 
    
class Camera(models.Model):
    title = models.CharField(max_length=5000, null=True, blank=True)
    manufacturer = models.CharField(max_length=5000, null=True, blank=True)
    modell = models.CharField(max_length=5000, null=True, blank=True)
    first_production = models.DateTimeField(default=datetime.now, blank=True)
    lens = models.ForeignKey(Lens, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.title} - (id: {self.id})"  
    

class Film(models.Model):
    title = models.CharField(max_length=5000, null=True, blank=True)
    iso = models.IntegerField(null=True, blank=True)
    manufacturer = models.CharField(max_length=5000, null=True, blank=True)
    first_production = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.title} - (id: {self.id})"  
    
class Scanner(models.Model):
    title = models.CharField(max_length=5000, null=True, blank=True)
    def __str__(self):
        return f"{self.title} - (id: {self.id})"  
    
    
class Category(models.Model):
    title = models.CharField(max_length=5000)
    def __str__(self):
        return f"{self.title} - (id: {self.id})"  
    
    
class Tag(models.Model):
    title = models.CharField(max_length=5000)
    def __str__(self):
        return f"{self.title} - (id: {self.id})" 
    

class Image(models.Model):
    image = models.ImageField(upload_to='media/', null=True)
    title = models.CharField(max_length=5000)
    author = models.CharField(max_length=5000, default='Oskar Antretter', null=True)
    date_shot = models.DateTimeField(default=datetime.now, blank=True)
    place = models.CharField(max_length=5000, null=True, blank=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True, blank=True)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, null=True, blank=True)
    lens = models.ForeignKey(Lens, on_delete=models.CASCADE, null=True, blank=True)
    scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE, null=True, blank=True)
    notes = models.TextField(max_length=1000000, null=True, blank=True)
    def __str__(self):
            return f"{self.title} - (id: {self.id})"

    
class Article(models.Model):
    html_template = models.CharField(max_length=5000,  blank=True, choices=[
        ('article_template01.html', 'Story, links Text, rechts Bilder'),
        ('article_template02.html', 'Artikel, links Text, rechts Bilder'),
    ])
    title = models.CharField(max_length=5000)
    intro_text = models.TextField(max_length=1000000, null=True, blank=True)
    seperated_texts = models.TextField(max_length=1000000, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=5000, default='Oskar Antretter', null=True)
    images = models.ManyToManyField(Image, related_name='articles', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='articles', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.title} - (id: {self.id})"
     
class Story(models.Model):
    title = models.CharField(max_length=5000, null=True, blank=True)
    first_chapter = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, blank=True)
    chapters = models.ManyToManyField(Article, related_name='articles', null=True, blank=True)
    def __str__(self):
        return f"{self.title} - (id: {self.id})"  

class ArticleLinker(models.Model):
    title = models.CharField(max_length=5000, null=True, blank=True)
    lens = models.ForeignKey(Lens, on_delete=models.CASCADE, null=True, blank=True)
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE, null=True, blank=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, null=True, blank=True)
    scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} - (id: {self.id})" 
    

    