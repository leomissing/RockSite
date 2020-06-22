from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', views.RegisterFormView.as_view()),
    path('login/', views.LoginFormView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('', views.index, name='index'),
    path('media/', views.media, name='media')
]
