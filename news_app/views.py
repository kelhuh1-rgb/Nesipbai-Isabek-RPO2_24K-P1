from xml.etree.ElementInclude import include

from django.shortcuts import render, get_object_or_404
from.models import Post, Category, Adv
from django.db.models import Q

def home_page(request):
    hot_posts = Post.objects.all().order_by('created_at')[:4]
    posts = Post.objects.all().order_by('-created_at')[:4]
    advs = Adv.objects.all()[:4]
    categories = Category.objects.all()
    context = {'posts': posts,
               'hot_posts': hot_posts,
               'advs':advs
               }
    return render(request, 'index.html', context)

def all_news_page(request):
    posts = Post.objects.all().order_by('-created_at')
    advs = Adv.objects.all()[:4]
    context = {
        'posts': posts,
        'advs': advs
    }
    return render(request, 'all-news.html', context)

def news_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    advs = Adv.objects.all()[:4]
    context = {
        'category': category,
        'posts': posts,
        'advs': advs
    }
    return render(request, 'news-by-category.html', context)


def search_page(request):
    advs = Adv.objects.all()[:4]
    context = {
        'advs': advs
    }
    return render(request, 'search.html', context)

def search_results(request):
    query = request.GET.get('q')
    advs = Adv.objects.all()[:4]
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains = query) | Q(description__icontains = query)
        )
    context = {
        'query':query,
        'results':results,
        'advs': advs
    }
    return render(request, 'search-results.html', context)

def read_news_page(request, pk):
    post = get_object_or_404(Post, pk=pk)
    advs = Adv.objects.all()[:4]
    context = {
        'post': post,
        'advs': advs
    }
    return render(request, 'read-news.html', context)


