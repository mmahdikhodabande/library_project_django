# Generated by Django 4.2.1 on 2023-11-21 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0005_remove_productcategory_url_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='elected_books',
            field=models.ManyToManyField(to='product_module.product', verbose_name='انتخاب کتاب ها '),
        ),
    ]