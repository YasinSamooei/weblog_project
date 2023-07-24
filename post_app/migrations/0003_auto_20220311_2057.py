# Generated by Django 3.2.12 on 2022-03-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_app', '0002_post_auther'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(to='post_app.Category'),
        ),
    ]
