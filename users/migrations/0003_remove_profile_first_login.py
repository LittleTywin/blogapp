# Generated by Django 3.1.6 on 2021-02-02 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_first_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_login',
        ),
    ]
