# content/views.py
from django.shortcuts import render, get_object_or_404
from .models import Tutorial, Category
from django.core.paginator import Paginator

def home(request):
    categories = Category.objects.all()
    featured_tutorials = Tutorial.objects.filter(is_published=True).order_by('-created_at')[:5]
    return render(request, 'home.html', {
        'categories': categories,
        'featured_tutorials': featured_tutorials,
    })

def tutorial_list(request, language=None, category_slug=None):
    tutorials = Tutorial.objects.filter(is_published=True)
    
    if language:
        tutorials = tutorials.filter(language=language)
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        tutorials = tutorials.filter(category=category)
    else:
        category = None
    
    # Pagination
    paginator = Paginator(tutorials.order_by('-created_at'), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'tutorial_list.html', {
        'page_obj': page_obj,
        'language': language,
        'category': category,
    })

def tutorial_detail(request, slug):
    tutorial = get_object_or_404(Tutorial, slug=slug, is_published=True)
    return render(request, 'tutorial_detail.html', {
        'tutorial': tutorial,
    })

def language_overview(request, language):
    tutorials = Tutorial.objects.filter(language=language, is_published=True)
    categories = Category.objects.filter(tutorial__language=language).distinct()
    
    return render(request, 'language_overview.html', {
        'language': dict(Tutorial.LANGUAGES).get(language),
        'language_code': language,
        'categories': categories,
        'tutorial_count': tutorials.count(),
    })
def about_us(request):
    return render(request, 'about_us.html')