from django.db import models
from django.conf import settings
from main.models import Product

class ShoppingCartTax(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(max_length=10, verbose_name="Стоимость доставки")

    class Meta:
        ordering = ('price',)
        verbose_name = 'Доставка'
        verbose_name_plural = 'Стоимость доставки'

    def __str__(self):
        return self.title

class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Кол-во', default=0)
    add_datetime = models.DateTimeField(verbose_name='Время', auto_now_add=True)

    @property
    def cost(self):
        return self.quantity * self.product.price
