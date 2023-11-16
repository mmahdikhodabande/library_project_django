from django.db import models


# Create your models here.


class ContactUsModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='موضوع')
    full_name = models.CharField(max_length=100, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=100, verbose_name='ایمیل')
    text = models.TextField(verbose_name='متن پیام')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    response = models.TextField(verbose_name='پاسخ ادمین')
    is_read_by_admin = models.BooleanField(default=True, verbose_name='خوانده شده توسط ادمین')

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.full_name
