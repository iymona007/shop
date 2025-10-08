from django.contrib import admin
from .models import *

@admin.register(Shop)
class menuAdmin(admin.ModelAdmin):
    list_display = ['name', 'image','price']