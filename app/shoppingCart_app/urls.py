from django.urls import path

from . import views

app_name = "shoppingCart_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:pk>/', views.add, name="add"),
    path('rem/<int:pk>/', views.remove, name="remove"),
]
