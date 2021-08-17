from django.urls import path

from . import views

app_name = "auth_app"
urlpatterns = [
    path('', views.index, name='index'),
    path('in/', views.login, name='login'),
    path('out/', views.logout, name='logout'),
    path('reg/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
