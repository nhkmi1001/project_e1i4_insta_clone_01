# Generated by Django 3.2.15 on 2022-10-03 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
    ]
