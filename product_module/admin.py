from django.contrib import admin
from jalali_date import datetime2jalali
from jalali_date.admin import ModelAdminJalaliMixin

from . import models


# Register your models here.

class date_persian(ModelAdminJalaliMixin, admin.ModelAdmin):
    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')


admin.site.register(models.Product)
admin.site.register(models.ProductCategory)
admin.site.register(models.Auther)
admin.site.register(models.Product_time_free, date_persian)
