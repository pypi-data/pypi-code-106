# Generated by Django 3.0.5 on 2020-04-25 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_rds_iam_auth', '0009_auto_20200425_1824'),
    ]

    operations = [
        migrations.RunSQL("""
                create function ibrag_privieged_user_has_role(text, text) returns boolean security definer 
                    language sql
                as
                $$
                select $1 in (select ibrag_get_user_roles($2)) as result
                $$;
            """, reverse_sql="drop function ibrag_privieged_user_has_role(text, text);"),
        migrations.RunSQL("""alter function ibrag_privieged_user_has_role(text, text) owner to postgres;"""),
    ]
