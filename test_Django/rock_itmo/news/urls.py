from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from .models import Articles

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20], template_name="news/posts.html")),
    path('<int:id>/', views.post, name='post'),
    path('post/new/', views.post_new, name='post_new')
]
