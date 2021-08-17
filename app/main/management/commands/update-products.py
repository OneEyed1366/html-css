from django.core.management.base import BaseCommand, CommandError
from main.models import Product
from os import path
from json import load

class Command(BaseCommand):
    help = "Обновление линейки представленных на сайте товаров"

    def handle(self, *args, **kwargs):
        with open(path.join(
            'media',
            'bd',
            'products.json'
        ), "r+", encoding="utf-8") as f:
            products = load(f)

        for product_id in products:
            number_id = product_id
            data = {
                "title": products[product_id]["title"],
                "desc": products[product_id]["desc"],
            }

            Product.objects.update_or_create(
                id=number_id,
                defaults=data
            )
