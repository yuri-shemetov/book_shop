from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Главная страница
    path('', views.home, name='home'),
    # Книги
    path('books/', views.Books.as_view(), name='books'),
    # Карточка книги
    path('book/<int:pk>/', views.Book.as_view(), name='book'),
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
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)