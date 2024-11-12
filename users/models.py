from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='phone')
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name='country')
    photo = models.ImageField(upload_to='users/avatars/', blank=True, null=True, verbose_name='photo')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

