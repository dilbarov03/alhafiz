# Generated by Django 4.0.6 on 2023-12-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_tarif_tarifservice_tarifpricing_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='star',
            field=models.PositiveIntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five')], verbose_name='Количество звезд'),
        ),
    ]
