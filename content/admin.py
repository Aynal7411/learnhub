# content/admin.py
from django.contrib import admin
from .models import Category, Tutorial
from .forms import TutorialForm

class TutorialAdmin(admin.ModelAdmin):
    form = TutorialForm
    list_display = ('title', 'language', 'category', 'is_published')
    list_filter = ('language', 'category', 'is_published')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Tutorial, TutorialAdmin)