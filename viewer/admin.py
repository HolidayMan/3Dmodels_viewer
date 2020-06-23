from django.contrib import admin
from .models import *


@admin.register(Model3D)
class Model3DAdmin(admin.ModelAdmin):
    list_display = ['file', 'file_id']
