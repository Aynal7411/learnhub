# content/models.py
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Tutorial(models.Model):
    LANGUAGES = [
        ('js', 'JavaScript'),
        ('py', 'Python'),
        ('html', 'HTML'),
        ('css', 'CSS'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    language = models.CharField(max_length=10, choices=LANGUAGES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    external_links = models.TextField(blank=True, help_text="One link per line")
    is_published = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_external_links(self):
        if self.external_links:
            return [link.strip() for link in self.external_links.split('\n') if link.strip()]
        return []
    
    def __str__(self):
        return self.title