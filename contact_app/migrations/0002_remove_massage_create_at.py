# Generated by Django 3.2.12 on 2022-04-28 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='massage',
            name='create_at',
        ),
    ]
