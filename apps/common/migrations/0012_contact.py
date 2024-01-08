# Generated by Django 4.0.6 on 2024-01-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_slide_title_ru_slide_title_uz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка на карту')),
                ('phone_number', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('latitude', models.FloatField(blank=True, null=True, verbose_name='Широта')),
                ('longitude', models.FloatField(blank=True, null=True, verbose_name='Долгота')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'ordering': ['order'],
            },
        ),
    ]