# Generated by Django 5.1.1 on 2024-10-24 13:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogs_image_alter_blogs_is_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='views_count',
            field=models.PositiveIntegerField(default=0, verbose_name='Счетчик просмотров'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/photo', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='text',
            field=models.TextField(verbose_name='Текст блога'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=25, verbose_name='Заголовок блога'),
        ),
    ]
