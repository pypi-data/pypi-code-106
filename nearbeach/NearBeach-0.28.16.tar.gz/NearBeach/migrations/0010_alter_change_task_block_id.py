# Generated by Django 3.2 on 2021-05-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0009_auto_20210506_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='change_task_block',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
