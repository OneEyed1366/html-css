import admin_app.views as admin_app
from django.urls import path, re_path

app_name = "admin_app-products"
urlpatterns = [
    path('read/category/<int:pk>/', admin_app.products, name='index'),
    path('create/category/<int:pk>/', admin_app.ProductsCreateView.as_view(), name='create'),
    path('read/<int:pk>/', admin_app.ProductDetailView.as_view(), name='read'),
    path('update/<int:pk>/', admin_app.ProductsUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', admin_app.ProductsDeleteView.as_view(), name='delete'),
]
