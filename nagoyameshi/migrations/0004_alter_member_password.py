# Generated by Django 4.2.6 on 2023-12-25 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagoyameshi', '0003_alter_member_email_alter_member_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=10, verbose_name='パスワード'),
        ),
    ]
