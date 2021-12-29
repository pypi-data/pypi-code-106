# Generated by Django 3.0.5 on 2020-04-25 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_rds_iam_auth', '0010_auto_20200425_1824'),
    ]

    operations = [
        migrations.RunSQL("""
                create function ibrag_privileged_get_user_tenants(text) returns SETOF text
                    security definer
                    language sql
                as
                $$
                select tenant_id as tenant_id FROM api_tenant_users where user_id = $1;
                $$;
            """, reverse_sql="drop function ibrag_privileged_get_user_tenants(text);"),
        migrations.RunSQL("""alter function ibrag_privileged_get_user_tenants(text) owner to postgres;"""),
    ]
