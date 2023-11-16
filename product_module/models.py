from django.db import models
from django.urls import reverse


# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url_title = models.CharField(max_length=100, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی های محصولات'


class Auther(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام نویسنده')
    url_name = models.CharField(max_length=100, verbose_name='نام در url')
    is_active = models.BooleanField(verbose_name='فعال')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'


class Product(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='عنوان')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    price = models.IntegerField(verbose_name='قیمت')
    amount_folio = models.IntegerField(verbose_name='تعداد صفحات')
    image = models.ImageField(upload_to='image/product', null=True, blank=True, verbose_name='تصویر')
    image_2 = models.ImageField(upload_to='image/product', null=True, blank=True, verbose_name='تصویر پشت کتاب')
    auther = models.CharField(max_length=100, null=True, blank=True, verbose_name='نویسنده اش')
    publisher = models.CharField(max_length=100, null=True, blank=True, verbose_name='انتشارات')
    dragoman = models.CharField(max_length=100, null=True, blank=True, verbose_name='مترجم')
    description = models.TextField(db_index=True, verbose_name='توضیحات')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', db_index=True,
                                      verbose_name='دسته بندی')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(default=False, verbose_name='حذف شده / موجود')
    publish_year = models.IntegerField(db_index=True, null=True, blank=True, verbose_name='سال انتشار')
    shebak = models.CharField(max_length=18, null=True, blank=True, verbose_name='شابک')

    # add rating field...

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
