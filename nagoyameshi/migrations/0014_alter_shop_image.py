# Generated by Django 4.2.6 on 2023-11-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagoyameshi', '0013_alter_shop_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='image',
            field=models.ImageField(blank=True, default='noImage.png', upload_to='media_local', verbose_name='写真'),
        ),
    ]
