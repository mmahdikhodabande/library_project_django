# Generated by Django 4.2.1 on 2023-11-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_remove_productcategory_url_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='slug',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='url_title',
            field=models.SlugField(default=1, max_length=100, verbose_name='عنوان در url'),
            preserve_default=False,
        ),
    ]
