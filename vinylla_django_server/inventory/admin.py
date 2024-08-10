from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Release, Track

# Register your models here.
admin.site.register(Release)


class ReleaseAdmin(ModelAdmin):
    ordering = ["-artist_name"]


admin.site.register(Track)
