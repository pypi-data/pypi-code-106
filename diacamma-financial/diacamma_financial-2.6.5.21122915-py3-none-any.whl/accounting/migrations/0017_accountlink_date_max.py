# Generated by Django 3.2.9 on 2021-11-13 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0016_fiscalyear_deletecascade'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountlink',
            name='date_max',
            field=models.DateField(default=None, null=True, verbose_name='date max'),
        ),
    ]
