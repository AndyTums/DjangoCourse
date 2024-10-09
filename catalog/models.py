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
                            verbose_name="Наименование",
                            help_text="Введите наименование продукта")

    description = models.TextField(verbose_name="Описание",
                                   help_text="Введите описание продукта")

    image = models.ImageField(upload_to="catalog/photo",
                              blank=True, null=True,
                              verbose_name="Изображение",
                              help_text="Загрузите изображение")

    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True,
                                 verbose_name="Категория",
                                 help_text="Введите категорию продукта",
                                 related_name="products")

    price = models.IntegerField(verbose_name="Цена",
                                help_text="Введите цену продукта")

    created_at = models.DateField(blank=True, null=True,
                                  verbose_name="Дата создания",
                                  help_text="Введите дату добавления продукта")

    updated_at = models.DateField(blank=True, null=True,
                                  verbose_name="Дата обновления",
                                  help_text="Введите дату изменения продукта")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price"]

    def __str__(self):
        return f"Продукт {self.name}, цена: {self.price}, дата создания: {self.created_at}, категория: {self.category}"
