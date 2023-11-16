from django.contrib import admin
from . import models
# Register your models here.


class AdminFooterLink(admin.ModelAdmin):
    list_display = ['title' ,'url_title']

admin.site.register(models.SiteSetting)
admin.site.register(models.SiteBanner)
admin.site.register(models.FooterLinkBox)
admin.site.register(models.FooterLink, AdminFooterLink)
admin.site.register(models.Slider)
