from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),
    # Книги
    path('books/', views.Books.as_view(), name='books'),
    # Карточка книги
    path('book/<int:pk>/', views.Book.as_view(), name='book'),
    # Рейтинг
    path('raiting/', views.BookUpdateRaiting.as_view(), name='raiting'),
    # Административный портал
    path('administration/', views.Administration.as_view(), name='administration'),
    # Редактировать книги
    path('books-managers/', views.BooksManagers.as_view(), name='books-managers'),
    # Добавить книгу
    path('book-create/', views.Book_create.as_view(), name='book-create'),
    # Редактировать книгу
    path('book-update/<int:pk>/', views.Book_update.as_view(), name='book-update'),
    # Удалить книгу
    path('book-delete/<int:pk>/', views.Book_delete.as_view(), name='book-delete'),
    # Промо-акции
    path('promo/', views.Promo_List.as_view(), name='promo'),
    # Подробнее об акции
    path('promo/<int:pk>/', views.Promo.as_view(), name='promo-detail'),
    # Добавить акцию
    path('promo-create/', views.Promo_create.as_view(), name='promo-create'),
    # Редактировать акцию
    path('promo-update/<int:pk>/', views.Promo_update.as_view(), name='promo-update'),
    # Удалить акцию
    path('promo-delete/<int:pk>/', views.Promo_delete.as_view(), name='promo-delete'),
    # Список заказов
    path('orders/', views.OrderListView.as_view(), name='orders'),
    # Подробности заказа
    path('order-detail/<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    # Статус заказа
    path('status/<int:pk>', views.StatusUpdate.as_view(), name='status'),
    # Карточки пользователей
    path('users-list/', views.UserListView.as_view(), name='users-list'),
    # Подробнее о пользователе
    path('users-detail-admin/<int:pk>', views.UserDetailView.as_view(), name='users-detail-admin'),
    # Редактировать данные пользователя
    path('users-update-admin/<int:pk>', views.UserUpdateView.as_view(), name='users-update-admin'),
    ]