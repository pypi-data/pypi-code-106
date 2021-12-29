# Generated by Django 3.0.5 on 2020-07-24 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_rds_iam_auth', '0022_auto_20200724_2020'),
    ]

    operations = [
        migrations.RunSQL("""
            create function ibrag_is_owner_of_user(text) returns boolean
                security definer
                language sql
            as
            $$
            select $1 in (select ibrag_get_owned_users_recursive()) as result
            $$;
        """, reverse_sql="drop function ibrag_is_owner_of_user(text);"),
        migrations.RunSQL("""alter function ibrag_is_owner_of_user(text) owner to postgres;"""),
    ]
