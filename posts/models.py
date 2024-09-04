from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
    
class Lens(models.Model):
    title = models.CharField(max_length=5000, null=True, blank=True)
    manufacturer = models.CharField(max_length=5000, null=True, blank=True)
    modell = models.CharField(max_length=5000, null=True, blank=True)
    focallength = models.CharField(max_length=5000, null=True, blank=True)
    aperature = models.CharField(max_length=5000, null=True, blank=True)
    first_production = models.DateTimeField(default=datetime.now, blank=True)
    focus_type = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('automatisch', 'automatisch'), 
        ('Messsucher', 'Messsucher'),
        ('automatischundmanuell', 'automatisch und manuell'),
        ('manuell', 'manuell'),
    ])
    min_focusdistance = models.CharField(max_length=5000, null=True, blank=True)
    def __str__(self):
        return f"{self.title} - (id: {self.id})" 
    
class Camera(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    manufacturer = models.CharField(max_length=100, null=True, blank=True)
    series = models.CharField(max_length=100, null=True, blank=True)
    variant = models.CharField(max_length=100, null=True, blank=True)

    first_production = models.CharField(max_length=4, null=True, blank=True)
    last_production = models.CharField(max_length=4, null=True, blank=True)

    view_finder_type = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('SLR', 'SLR'),
        ('Messsucher', 'Messsucher'),
        ('elektrisch','elektrisch')
    ])

    lens_type = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('festverbaut', 'festverbaut'),
        ('austauschbar', 'austauschbar')
    ])
    lens = models.ForeignKey(Lens, on_delete=models.CASCADE, null=True, blank=True)
    lens_socket = models.CharField(max_length=100, null=True, blank=True)

    modes = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('Vollautomatisch', 'Vollautomatisch'),
        ('Programm','Programm'),
        ('Blendenautomatik', 'Blendenautomatik'),
        ('Belichtungsautomatik', 'Belichtungsautomatik'),
        ('Manuell', 'Manuell'),
        ('Belichtungsautomatik und vollautomatisch', 'Belichtungsautomatik und vollautomatisch'),
        ('Blendenautomatik und Vollautomatisch', 'Blendenautomatik und vollautomatisch'),

    ])
    lightmeter_type = models.CharField(max_length=50, null=True, blank=True)

    min_shutter_speed = models.CharField(max_length=50, null=True, blank=True)
    max_shutter_speed = models.CharField(max_length=50, null=True, blank=True)
    bulb = models.BooleanField(default=True) 
    
    film_size = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('Kleinbild', 'Kleinbild'),
        ('Mittelbild', 'Mittelbild'),
        ('Großbild', 'Großbild'),
    ])
    iso_setting = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('manuell', 'manuell'),
        ('automatisch', 'automatisch'),
        ('manuellundautomatisch', 'manuell und automatisch'),
    ])
    film_transport = models.CharField(max_length=100, null=True, blank=True, choices=[
        ('manuell', 'manuell'),
        ('elektrisch', 'elektrisch')
    ])
    min_iso = models.IntegerField( null=True, blank=True)
    max_iso = models.IntegerField( null=True, blank=True)
    
    accessories = models.CharField(max_length=5000, null=True, blank=True)

    height = models.IntegerField( null=True, blank=True)
    width = models.IntegerField( null=True, blank=True)
    depth = models.IntegerField( null=True, blank=True)
    weight = models.IntegerField( null=True, blank=True)
    build_material = models.CharField(max_length=5000, null=True, blank=True)
    color_variants = models.CharField(max_length=5000, null=True, blank=True)

    battery = models.CharField(max_length=5000, null=True, blank=True)

    successor = models.ForeignKey('self', related_name='successors', null=True, blank=True, on_delete=models.CASCADE)
    predecessor = models.ForeignKey('self', related_name='predecessors', null=True, blank=True, on_delete=models.CASCADE)
    similar_cameras = models.ManyToManyField('self', null=True, blank=True, related_name='similar_cameras')
    related_cameras = models.ManyToManyField('self', null=True, blank=True, related_name='related_cameras')
    
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
    image_file = models.ImageField(upload_to='media/', null=True)
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
            return f"{self.title} - {self.date_shot.strftime('%d.%m.%Y')} - (id: {self.id})"
    

class Article(models.Model):
    html_template = models.CharField(max_length=5000,  blank=True, choices=[
        ('article_template01.html', 'Story, links Text, rechts Bilder'),
        ('article_template02.html', 'Artikel, links Text, rechts Bilder'),
        ('article_template03.html', 'Artikel, Text, Bild, Tabelle'),
    ])
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=5000)
    intro_text = RichTextField(null=True, blank=True)
    seperated_texts = models.TextField(max_length=1000000, null=True, blank=True)
    images = models.ManyToManyField(Image, through='ArticleImage', related_name='articles')
    author = models.CharField(max_length=5000, default='Oskar Antretter', null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True) 
    updated_at = models.DateTimeField(default=datetime.now, blank=True)
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
    article = models.ForeignKey(Article, related_name='linked_article', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} - (id: {self.id})" 
    

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.article.title} - {self.image.title} (Order: {self.order})"