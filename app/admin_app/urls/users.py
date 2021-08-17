import admin_app.views as admin_app
from django.urls import path

app_name = "admin_app-users"
urlpatterns = [
    path('create/', admin_app.UsersCreateView.as_view(), name='create'),
    path('read/', admin_app.UsersListView.as_view(), name='read'),
    path('update/<int:pk>/', admin_app.UsersUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', admin_app.UsersDeleteView.as_view(), name='delete'),
]
