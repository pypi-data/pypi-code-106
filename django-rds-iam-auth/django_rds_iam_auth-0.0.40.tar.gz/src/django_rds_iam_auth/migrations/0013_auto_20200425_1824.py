# Generated by Django 3.0.5 on 2020-04-25 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_rds_iam_auth', '0012_auto_20200425_1824'),
    ]

    operations = [
        migrations.RunSQL("""
                create function ibrag_user_has_role(text) returns boolean security invoker
                    language sql
                as
                $$
                select $1 in (select ibrag_get_user_roles(current_user)) as result
                $$;
            """, reverse_sql="drop function ibrag_user_has_role(text);"),
        migrations.RunSQL("""alter function ibrag_user_has_role(text) owner to postgres;"""),
    ]
