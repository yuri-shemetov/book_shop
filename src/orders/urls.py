from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # Заказ
    path('create-order/', views.CreateOrder.as_view(), name='create-order'),
    # Заказ оформлен
    path('thanks/', views.Thanks.as_view(), name='thanks'),
    ]
