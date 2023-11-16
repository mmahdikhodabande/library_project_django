from django.contrib import admin
from . import models
from django.http import HttpRequest

from .models import Article


# Register your models here.

class AdminArticle(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'auther']
    list_editable = ['is_active']

    def save_model(self, request: HttpRequest, obj: Article, form, change):
        if not change:
            obj.auther = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(models.Article, AdminArticle)
admin.site.register(models.ArticleCategory)
admin.site.register(models.ArticleCommend)
