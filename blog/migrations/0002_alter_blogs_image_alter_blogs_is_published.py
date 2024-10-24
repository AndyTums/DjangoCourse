# Generated by Django 5.1.1 on 2024-10-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавьте изображение', null=True, upload_to='blog/photo', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовать'),
        ),
    ]
