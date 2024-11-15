# Generated by Django 5.1.3 on 2024-11-15 20:11

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_categories', models.CharField(max_length=150, unique=True, verbose_name='Категории')),
                ('category_code', models.CharField(max_length=150, unique=True, verbose_name='Код категории')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_materials', models.CharField(max_length=150, unique=True, verbose_name='Наименование материала')),
                ('materials_code', models.CharField(max_length=150, unique=True, verbose_name='Код материала')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01000000000000000020816681711721685132943093776702880859375'))], verbose_name='Цена')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('categories_materials', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'материалы',
                'ordering': ('-pub_date',),
            },
        ),
    ]