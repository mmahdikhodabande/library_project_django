# Generated by Django 4.2.1 on 2023-11-20 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auther',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/auther', verbose_name='تصویر'),
        ),
    ]
