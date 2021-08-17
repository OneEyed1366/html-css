from django.urls import include, path
from . import users, categories, products
from admin_app import views

app_name = "admin_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("users/", include(users, namespace="users")),
    path("categories/", include(categories, namespace="categories")),
    path("products/", include(products, namespace="products"))
]
