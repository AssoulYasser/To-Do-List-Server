# Generated by Django 4.1.7 on 2023-03-23 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApi', '0003_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created',
        ),
    ]