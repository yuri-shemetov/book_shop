from django.urls import path
from . import views


app_name = 'users'

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
    # Список всех пользователей
    path('users-all/', views.UsersAllView.as_view(), name='users-all'),
    # Подробная информация о другом покупателе
    path('other-user/', views.UserOtherView.as_view(), name='other-user'),
    # Информация о менеджере
    path('admin-user/', views.UserAdminView.as_view(), name='admin-user'),
    # Подробная информация о пользователе
    path('user-detail/', views.UserListView.as_view(), name='user-detail'),
    # Изменить информацию
    path('user-update/<int:pk>/', views.UserUpdateView.as_view(), name='user-update'),
    # Добавить информацию
    path('user-create/', views.UserCreateView.as_view(), name='user-create'),
    # Подробнее о заказе покупателя
    path('user-order/', views.UserOrderList.as_view(), name='user-order'),
    # Отмена заказа покупателем
    path('status-cancel/', views.StatusCancel.as_view(), name='status-cancel'),
]
