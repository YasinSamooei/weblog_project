# Generated by Django 3.2.12 on 2022-06-28 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0002_remove_massage_create_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='massage',
            options={'verbose_name': 'پیام', 'verbose_name_plural': 'پیام ها'},
        ),
    ]
