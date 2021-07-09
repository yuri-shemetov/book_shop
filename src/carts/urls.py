from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    # Корзина
    path('', views.CartView.as_view(), name='cart-edit'),
    # Удалить товар
    path('delete-book-in-cart/<int:pk>/', views.DeleteBook.as_view(), name='delete-book-in-cart'),
     # Обновить корзину
    path('update-cart/', views.CartUpdate.as_view(), name='update-cart'),
    ]
