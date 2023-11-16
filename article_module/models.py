from django.db import models
from jalali_date import date2jalali

from account_module.models import User


# Create your models here.


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='دسته بندی والد')
    title = models.CharField(max_length=100, verbose_name='عنوان')
    url_title = models.CharField(max_length=100, verbose_name='عنوان در url')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقالات'


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(max_length=100, allow_unicode=True, db_index=True, verbose_name='لینک')
    image = models.ImageField(upload_to='image/article', verbose_name='تصویر ')
    short_description = models.CharField(max_length=250, null=True, blank=True, verbose_name='توضیحات کوتاه')
    is_active = models.BooleanField(default=False, verbose_name='فعال')
    text = models.TextField(verbose_name='متن مقاله')
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name='دسته بندی')
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='نویسنده')
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='تاریخ انتشار')

    def __str__(self):
        return self.title

    def get_jalali_create_date(self):
        return date2jalali(self.create_date)

    def get_jalali_create_time(self):
        return self.create_date.strftime('%H : %M')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class ArticleCommend(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    parent = models.ForeignKey('ArticleCommend', on_delete=models.CASCADE, null=True, blank=True, verbose_name='والد')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    text = models.TextField(verbose_name='متن نظر')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name = 'نظر مقاله'
        verbose_name_plural = 'نظرات مقالات'
