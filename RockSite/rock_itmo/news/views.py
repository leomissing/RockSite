from django.shortcuts import render
from .models import Articles
from .forms import ArticleForm
from django.utils import timezone
from django.shortcuts import redirect

def index(request):
    return render(request, 'mainPage/homePage.html',)


def post(request, id):
    post = Articles.objects.get(pk=id)
    return render(request, 'news/post.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.date = timezone.now()
            post.save()
            return render(request, 'mainPage/homePage.html',)
    else:
        form = ArticleForm()
    return render(request, 'news/post_edit.html', {'form': form})
