# Generated by Django 3.0.5 on 2021-09-02 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_rds_iam_auth', '0041_tenant_bucket_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
