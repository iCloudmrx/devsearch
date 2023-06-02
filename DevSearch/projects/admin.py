from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name','created','updated']

admin.site.register(Project)
admin.site.register(Review)