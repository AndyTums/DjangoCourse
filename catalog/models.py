from django.utils import timezone

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name="Название категории",
                            help_text="Введите название категории")

    description = models.TextField(verbose_name="Описание",
                                   help_text="Введите описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name", ]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name="Наименование")

    description = models.TextField(verbose_name="Описание")

    image = models.ImageField(upload_to="catalog/photo",
                              blank=True, null=True,
                              verbose_name="Изображение")

    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True,
                                 verbose_name="Категория",
                                 related_name="products")

    price = models.IntegerField(verbose_name="Цена")

    created_at = models.DateField(blank=True, null=True,
                                  verbose_name="Дата создания")

    updated_at = models.DateField(blank=True, null=True,
                                  verbose_name="Дата обновления",
                                  default=timezone.now)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return f"Продукт {self.name}, цена: {self.price}, дата создания: {self.created_at}, категория: {self.category}"
