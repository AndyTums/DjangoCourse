from django.db import models
from django.utils import timezone


class Blogs(models.Model):
    title = models.CharField(max_length=25, verbose_name='Заголовок блога', help_text='Введите заголовок вашего блога')
    text = models.TextField(verbose_name='Текст блога', help_text='Добавьте ваш текст')
    image = models.ImageField(blank=True, null=True, upload_to='blog/photo', verbose_name='Изображение', help_text='Добавьте изображение')
    created_at = models.DateField(default=timezone.now, verbose_name="Дата создания",
                                  help_text="Введите дату добавления продукта")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовать")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["created_at"]
