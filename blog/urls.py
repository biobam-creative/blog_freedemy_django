from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [

    path('', views.home, name='home'),
    path('all_blogs', views.all_blogs, name='all_blogs'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('tag/<slug:slug>/', views.tagged, name='tagged'),
    path('category/<int:cats>/', views.category, name='category'),
]
