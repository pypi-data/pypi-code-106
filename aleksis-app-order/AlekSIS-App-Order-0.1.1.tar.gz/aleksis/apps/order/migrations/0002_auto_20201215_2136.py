# Generated by Django 3.1.3 on 2020-12-15 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='housenumber',
            field=models.CharField(blank=True, max_length=255, verbose_name='Housenumber'),
        ),
        migrations.AlterField(
            model_name='order',
            name='street',
            field=models.CharField(blank=True, max_length=255, verbose_name='Straße'),
        ),
    ]
