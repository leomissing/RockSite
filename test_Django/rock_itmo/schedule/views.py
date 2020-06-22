from django.shortcuts import render
from django.http import HttpResponse
from .models import zapis
from .forms import zapisForm
# from django.utils import timezone
from django.shortcuts import redirect

def index(request):
    return render(request, 'schedule/week.html',)

def zapis(request, id):
    post = Articles.objects.get(pk=id)
    return render(request, 'schedule/zapis.html', {'post': post})

def zapisi(request, day, time):
    bron = zapis.objects.get(week_day=day, start_time=time)
    return render(request, 'schedule/bron.html', {'bron':bron})

def zapis_new(request):
    if request.method == "POST":
        form = zapisForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form=zapisForm()
    return render(request, 'schedule/zapis_edit.html', {'form': form})
