from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    email = models.EmailField(
        unique=True,
        max_length=150,
        verbose_name='e-mail',
        help_text='Укажите свой e-mail'
    )
    username = models.CharField(
        max_length=150,
        verbose_name='Имя пользователя',
        help_text='Укажите имя пользователя'
    )
    department = models.CharField(
        max_length=150,
        verbose_name='Отдел',
        unique=True
    )
    job_title = models.CharField(
        max_length=150,
        verbose_name='Должность'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'пользователи'
    
    def __str__(self):
        return self.username
