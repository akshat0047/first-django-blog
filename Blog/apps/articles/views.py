from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import ArticleForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import markdown2

@login_required
def article_list(request):
    articles = request.user.posts.all()
    return render(request, "articles/article_list.html", {"articles": articles})

def article_detail(request, pk):
    article = get_object_or_404(Post, pk=pk)
    return render(request, "articles/article_detail.html",{"article":article})

@login_required
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('user_articles')
    else:
        form = ArticleForm()
        return render(request ,"articles/article_create.html", {"form": form})
    
@login_required
def preview_markdown(request):
    if request.method == "POST":
        content = request.POST.get("content", "")
        html = markdown2.markdown(content)
        return JsonResponse({"html": html})
