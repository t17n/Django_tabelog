# Generated by Django 4.2.6 on 2023-11-23 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagoyameshi', '0002_shop_parking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真'),
        ),
    ]