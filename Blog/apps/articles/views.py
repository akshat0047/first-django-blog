from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import ArticleForm
from django.utils import timezone
# Create your views here.


def home(request):
    articles = Post.objects.filter(author=request.user)
    return render(request, "articles/index.html", {"articles": articles})


def details(request, pk):
    article = get_object_or_404(Post, pk=pk)
    return render(request, "articles/article_detail.html",{"articled":article})


def carticle(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
        return render(request ,"articles/carticle.html", {"form": form})
