# Generated by Django 4.0.6 on 2024-01-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_slide'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='slide',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Заголовок'),
        ),
    ]
