# Generated by Django 4.0.6 on 2024-01-06 12:07

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_tarif_price_alter_tarifpricing_tarif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=85, scale=None, size=[1920, 1080], upload_to='news', verbose_name='Изображение'),
        ),
    ]