from django.db import models
from django.urls import reverse


# Create your models here.
from django.utils import timezone


class Auther(models.Model):
    name = models.CharField(max_length=100, verbose_name='نام نویسنده')
    url_name = models.CharField(max_length=100, verbose_name='نام در url')
    is_active = models.BooleanField(verbose_name='فعال')
    image = models.ImageField(upload_to='image/auther', null=True, blank=True, verbose_name='تصویر')

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
    category = models.ManyToManyField('ProductCategory', related_name='product_categories', db_index=True,
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


class ProductCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url')
    image = models.ImageField(upload_to='image/product_category', null=True, blank=True, verbose_name='تصویر')
    is_active = models.BooleanField(verbose_name='فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده')

    def get_absolute_url(self):
        return reverse('Product_list_category', args=[self.slug])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی های محصولات'


Percent = (
    ('10', '10'),
    ('20', '20 '),
    ('30', '30'),
    ('40', '40'),
    ('50', '50'),
    ('60', '60'),
    ('70', '70'),
    ('80', '80'),
    ('90', '90'),
    ('100', '100'),
)


class Product_time_free(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='اسم محصول')
    percent = models.CharField(max_length=3, choices=Percent, verbose_name='درصد تخفیف', null=False)
    uploaded = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ آپلود')
    dead_line = models.DateTimeField(null=True, verbose_name='تاریخ اتمام تخفیف')

    def __str__(self):
        return self.product.title

    def is_discount_expired(self):
        return self.dead_line < timezone.now()

    class Meta:
        verbose_name = 'محصول تخفیفی'
        verbose_name_plural = 'محصولات تخفیف دار'
