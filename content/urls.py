# content/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tutorials/', views.tutorial_list, name='tutorial_list'),
    path('tutorials/<slug:slug>/', views.tutorial_detail, name='tutorial_detail'),
    path('language/<str:language>/', views.language_overview, name='language_overview'),
    path('language/<str:language>/tutorials/', views.tutorial_list, name='language_tutorials'),
    path('category/<slug:category_slug>/', views.tutorial_list, name='category_tutorials'),
    path('about_us/', views.about_us, name='about_us'),
]