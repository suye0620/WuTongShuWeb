# Generated by Django 3.2.5 on 2023-05-12 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0006_auto_20230512_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='add_to_index',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='details.tag', verbose_name='文章标签'),
        ),
        migrations.AlterField(
            model_name='category',
            name='primary_color',
            field=models.CharField(default='#FFD700', max_length=7, verbose_name='颜色1(primary_color)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='secondary_color',
            field=models.CharField(default='#fd614a', max_length=7, verbose_name='颜色2(secondary_color)'),
        ),
    ]