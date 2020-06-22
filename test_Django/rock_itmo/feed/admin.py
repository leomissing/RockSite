from django.contrib import admin
from news.models import Articles
from schedule.models import reservasions, zapis

admin.site.register(Articles)
admin.site.register(reservasions)
admin.site.register(zapis)
# Register your models here.
