from django.shortcuts import render, get_object_or_404, redirect
from apps.articles.models import Post
from random import randint


def IndexView(request):
    blogs = Post.objects.all().order_by('-published_date')
    return render(request, 'home/index.html', {'blogs': blogs})
