# Generated by Django 3.1.4 on 2021-02-16 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_post_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='phone',
        ),
    ]
