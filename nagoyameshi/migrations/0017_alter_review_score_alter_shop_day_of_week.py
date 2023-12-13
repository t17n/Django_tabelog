# Generated by Django 4.2.6 on 2023-11-29 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagoyameshi', '0016_rename_condition_condition_kodawari'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(choices=[('★', '★'), ('★★', '★★'), ('★★★', '★★★'), ('★★★★', '★★★★'), ('★★★★★', '★★★★★')], default=3, verbose_name='レビュースコア'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='day_of_week',
            field=models.IntegerField(choices=[('月曜日', '月曜日'), ('火曜日', '火曜日'), ('水曜日', '水曜日'), ('木曜日', '木曜日'), ('金曜日', '金曜日'), ('土曜日', '土曜日'), ('日曜日', '日曜日'), ('祝日', '祝日'), ('無休', '無休')], verbose_name='店休日'),
        ),
    ]