from django.db import models
from os import path

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    is_active = models.BooleanField(verbose_name='Активно?', default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    hero = models.ImageField(blank=True, verbose_name="Лицо товара", upload_to=path.join(
        'img',
        'products',
    ))
    title = models.CharField(max_length=100, verbose_name="Название")
    desc = models.CharField(max_length=100, verbose_name="Описание")
    price = models.FloatField(max_length=20, verbose_name="Цена")
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f"Карточка товара -> {self.title}"

class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name="imgs", on_delete=models.CASCADE)
    img = models.ImageField(
        "Фотографии товара", upload_to=path.join('img', 'products',))

    class Meta:
        ordering = ('product',)
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return f"Фотография товара {self.product.title}"
