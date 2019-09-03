from django.urls import path

from . import views


urlpatterns = [
    path('customer_list', views.customer_list, name='customer_list'),
]
