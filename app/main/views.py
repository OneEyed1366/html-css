from django.shortcuts import render
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category
from shoppingCart_app.models import ShoppingCart
from random import randrange

# slugs = [item.slug for item in Category.objects.all()]
data = {
    "cat_list": Category.objects.all(),
}


def index(request):
    data["products"] = Product.objects.all()
    data["cart"] = Product.objects.all().aggregate(Sum("quantity"))["quantity__sum"]

    return render(request, "index.html", context=data)


def products(request, slug=None):
    page = request.GET["page"] if "page" in request.GET else 1
    data["cart"] = ShoppingCart.objects.all().aggregate(Sum("quantity"))[
        "quantity__sum"]
    products = Product.objects.filter(
        category__is_active = True, category__slug=slug) if slug else Product.objects.filter(
            category__is_active = True)
    paginator = Paginator(products, 2)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    data["product"] = products[randrange(0, len(products))]
    data["products"] = products_paginator

    return render(request, "products/_index.html", context=data)

def products_sel(request, pk):
    data["data"] = Product.objects.get(pk=pk)
    data["cart"] = ShoppingCart.objects.all().aggregate(Sum("quantity"))[
        "quantity__sum"]
    # data["similars"] = Product.objects.filter(category__slug=)
    
    return render(request, "products/id.html", context=data)

def contact(request):
    return render(request, 'contact.html', context=data)
