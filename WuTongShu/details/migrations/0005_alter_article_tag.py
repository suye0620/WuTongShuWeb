# Generated by Django 3.2.5 on 2023-05-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_alter_article_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='details.Tag', verbose_name='文章标签'),
        ),
    ]