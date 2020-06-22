from django.urls import path, include
from . import views
from django.views.generic import ListView, DetailView
from schedule.models import reservasions,zapis


urlpatterns = [
    path('', ListView.as_view(queryset=zapis.objects.all(), template_name="schedule/zapisi.html")),
    path('<int:id>/', views.zapis, name='zapis'),
    path('new/', views.zapis_new, name='zapis_new')
]
