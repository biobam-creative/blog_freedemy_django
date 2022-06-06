from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from . serializers import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from taggit.models import Tag

# BLOG_POST_PER_PAGE = 10

# # Create your views here.


# def base(request,):
#     categories = Category.objects.all()

#     context = {
#         'categories': categories,
#     }

#     return render(request, 'blog/base.html', context)


# def home(request):
#     blogs = Opportunity.objects.all()
#     categories = Category.objects.all()
#     recent_posts = Blog.objects.order_by('-date')[:3]
#     common_tags = Blog.tags.most_common()[:7]
#     search_term = ''

#     if 'search' in request.GET:
#         search_term = request.GET.get('search')
#         recent_posts = recent_posts.filter(body__icontains=search_term)

#     context = {
#         'blogs': blogs,
#         'categories': categories,
#         'recent_posts': recent_posts,
#         'common_tags': common_tags,
#     }
    
#     return render(request, 'blog/home.html', context)


# def all_blogs(request,):
#     categories = Category.objects.all()
#     recent_posts = Blog.objects.order_by('-date')
#     common_tags = Blog.tags.most_common()[:7]
#     search_term = ''

#     if 'search' in request.GET:
#         search_term = request.GET.get('search')
#         recent_posts = recent_posts.filter(body__icontains=search_term)

#     # pagination
#     page = request.GET.get('page', 1)
#     paginator = Paginator(recent_posts, BLOG_POST_PER_PAGE)

#     try:
#         recent_posts = paginator.page(page)
#     except PageNotAnInteger:
#         recent_posts = page(BLOG_POST_PER_PAGE)
#     except EmptyPage:
#         recent_posts = page(recent_posts.num_pages)

#     context = {
#         'categories': categories,
#         'recent_posts': recent_posts,
#         'common_tags': common_tags,
#     }
#     return render(request, 'blog/all_blogs.html', context)


# def blog_detail(request, slug):
#     blog = get_object_or_404(Opportunity, slug=slug)
#     categories = Category.objects.all()
#     recent_posts = Blog.objects.order_by('-date')
#     common_tags = Blog.tags.most_common()[:7]
#     search_term = ''

#     if 'search' in request.GET:
#         search_term = request.GET.get('search')
#         recent_posts = recent_posts.filter(body__icontains=search_term)

#     context = {'blog': blog,
#                'categories': categories,
#                'recent_posts': recent_posts,
#                'common_tags': common_tags,
#                }

#     return render(request, 'blog/blog_detail.html', context)


# def tagged(request, slug):
#     tag = get_object_or_404(Tag, slug=slug)
#     categories = Category.objects.all()
#     recent_posts = Blog.objects.filter(tags=tag)
#     common_tags = Blog.tags.most_common()[:7]
#     search_term = ''

#     if 'search' in request.GET:
#         search_term = request.GET.get('search')
#         recent_posts = recent_posts.filter(body__icontains=search_term)

#     # pagination
#     page = request.GET.get('page', 1)
#     paginator = Paginator(recent_posts, BLOG_POST_PER_PAGE)

#     try:
#         recent_posts = paginator.page(page)
#     except PageNotAnInteger:
#         recent_posts = page(BLOG_POST_PER_PAGE)
#     except EmptyPage:
#         recent_posts = page(recent_posts.num_pages)

#     context = {
#         'tag': tag,
#         'categories': categories,
#         'recent_posts': recent_posts,
#         'common_tags': common_tags,
#     }
#     return render(request, 'blog/all_blogs.html', context)


# def about(request):

#     return render(request, 'blog/about.html')


# def category(request, cats):

#     categories = Category.objects.all()
#     recent_posts = Blog.objects.filter(category=cats)
#     common_tags = Blog.tags.most_common()[:7]
#     search_term = ''

#     if 'search' in request.GET:
#         search_term = request.GET.get('search')
#         recent_posts = recent_posts.filter(body__icontains=search_term)

#     # pagination
#     page = request.GET.get('page', 1)
#     paginator = Paginator(recent_posts, BLOG_POST_PER_PAGE)

#     try:
#         recent_posts = paginator.page(page)
#     except PageNotAnInteger:
#         recent_posts = page(BLOG_POST_PER_PAGE)
#     except EmptyPage:
#         recent_posts = page(recent_posts.num_pages)

#     context = {

#         'categories': categories,
#         'recent_posts': recent_posts,
#         'common_tags': common_tags,
#         'cats': cats,
#     }

#     return render(request, 'blog/all_blogs.html', context)


# def contact(request):
#     form = ContactForm()
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             message = form.cleaned_data["message"]
#             name = form.cleaned_data["name"]
#             email = f'Message from {form.cleaned_data["email"]}'
#             subject = form.cleaned_data["subject"]
#             recipients = ['eminentia.ea@gmail.com', ]

#             sucess_message = f'Thank you {name}, Your email has been sent.'
#             failed_message = 'Your message was not delivered please try again!!!'

#             try:
#                 send_mail(subject, message, email,
#                           recipients,  fail_silently=True, )
#             except BadHeaderError:
#                 return render(request, 'blog/contact.html', {'failed_message': failed_message, 'form': form})
#             return render(request, 'blog/contact.html', {'sucess_message': sucess_message, 'form': form})

#     return render(request, 'blog/contact.html', {'form': form})

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_number'
    max_page_size = 4

class BlogView(ListAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    pagination_class = StandardResultsSetPagination
    


class OpportunityView(ListAPIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer