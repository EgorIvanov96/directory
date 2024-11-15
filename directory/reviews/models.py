from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator


class Categories(models.Model):
    """Модель категорий."""

    name_categories = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Категории'
    )
    category_code = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Код категории'
    )

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name_categories


class Materials(models.Model):
    """Модель материалов."""

    name_materials = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Наименование материала'
    )
    categories_materials = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )
    materials_code = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Код материала'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal(0.01))],
        verbose_name='Цена'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата публикации',
        auto_now_add=True)

    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'материалы'
        ordering = ('-pub_date',)

    def __str__(self):
        return self.name_materials
