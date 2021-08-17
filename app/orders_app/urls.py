from . import views as orders_app
from django.urls import path, re_path

from . import views

app_name = "orders_app"
urlpatterns = [
    # path('', views.index, name='index'),
    re_path(r'^$', orders_app.OrderList.as_view(), name='orders_list'),
    re_path(r'^forming/complete/(?P<pk>\d+)/$',
            orders_app.order_forming_complete, name='order_forming_complete'),
    re_path(r'^create/$', orders_app.OrderItemsCreate.as_view(), name='order_create'),
    re_path(r'^read/(?P<pk>\d+)/$', orders_app.OrderRead.as_view(),
            name='order_read'),
    re_path(r'^update/(?P<pk>\d+)/$', orders_app.OrderItemsUpdate.as_view(),
            name='order_update'),
    re_path(r'^delete/(?P<pk>\d+)/$', orders_app.OrderDelete.as_view(),
            name='order_delete'),
]
