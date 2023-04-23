# Generated by Django 3.2.5 on 2023-04-18 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='cover_square',
            field=models.URLField(blank=True, default='http://42.193.14.111/static/upload/tsxywts/6.png', verbose_name='在首页子版块中展示的方形封面'),
        ),
        migrations.AlterField(
            model_name='article',
            name='index',
            field=models.IntegerField(blank=True, default=1, verbose_name='在首页子版块中展示的顺序'),
        ),
    ]