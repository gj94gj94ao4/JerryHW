from django.contrib import admin

# Register your models here.
from .models import Choice, Pool

admin.site.register(Choice)
admin.site.register(Pool)