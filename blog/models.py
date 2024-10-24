from django.db import models
from django.utils import timezone


class Blogs(models.Model):
    title = models.CharField(max_length=25, verbose_name='Заголовок блога')
    text = models.TextField(verbose_name='Текст блога')
    image = models.ImageField(blank=True, null=True, upload_to='blog/photo', verbose_name='Изображение')
    created_at = models.DateField(default=timezone.now, verbose_name="Дата создания")
    is_published = models.BooleanField(default=False, verbose_name="Опубликовать")
    views_count = models.PositiveIntegerField(verbose_name="Счетчик просмотров", default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["created_at"]
