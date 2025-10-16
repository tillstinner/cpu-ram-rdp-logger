from django.contrib import admin
from .models import Metric, Host

# Register your models here.
admin.site.register(Metric)
admin.site.register(Host)