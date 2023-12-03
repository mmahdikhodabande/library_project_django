# Generated by Django 4.2.1 on 2023-11-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_auther_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='url_title',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='عنوان در url'),
        ),
    ]