from django.shortcuts import render
from .models import Blog
# Create your views here.

def home(request):
    latest_posts = Blog.objects.all().order_by('-date')[:2]
    return render(request, 'blog/index.html', {'latest_posts' : latest_posts})

def posts(request):
    all_posts = Blog.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {'all_posts' : all_posts})

def blog(request, slug):
    blog = Blog.objects.get(slug = slug)
    return render(request, 'blog/post-details.html', {'post' : blog})