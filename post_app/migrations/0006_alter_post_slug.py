# Generated by Django 3.2.12 on 2022-03-13 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
