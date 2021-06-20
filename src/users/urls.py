from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Страница входа
    path('login/', views.MyLogin.as_view(), name='login'),
    # Страница выхода
    path('logout/', views.logout_view, name='logout'),
    # Страница регистрации
    path('register/', views.user_register, name='register'),
    # Страница о пользователе
    path('user/', views.User.as_view(), name='user'),
    # Смена пароля
    path('change-password/', views.ChP.as_view(), name='change-password'),
]
