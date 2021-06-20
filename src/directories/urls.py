from django.urls import path
from . import views

urlpatterns = [
    # Справочники
    path('directories', views.HomePage.as_view(), name='directories'),

    # Авторы
    path('authors/', views.Authors.as_view(), name='authors'),
    path('authors/<int:pk>/', views.Author.as_view(), name='author'),
    path('authors-create/', views.Author_create.as_view(), name='authors-create'),
    path('authors-update/<int:pk>/', views.Author_update.as_view(), name='authors-update'),
    path('authors-delete/<int:pk>/', views.Author_delete.as_view(), name='authors-delete'),

    # Издательства
    path('publishers/', views.Publishers.as_view(), name='publishers'),
    path('publishers/<int:pk>/', views.Publisher.as_view(), name='publisher'),
    path('publishers-create/', views.Publishers_create.as_view(), name='publishers-create'),
    path('publishers-update/<int:pk>/', views.Publishers_update.as_view(), name='publishers-update'),
    path('publishers-delete/<int:pk>/', views.Publishers_delete.as_view(), name='publishers-delete'),

    #  Жанры
    path('genres/', views.Genres.as_view(), name='genres'),
    path('genres/<int:pk>/', views.Genre.as_view(), name='genre'),
    path('genres-create/', views.Genres_create.as_view(), name='genres-create'),
    path('genres-update/<int:pk>/', views.Genres_update.as_view(), name='genres-update'),
    path('genres-delete/<int:pk>/', views.Genres_delete.as_view(), name='genres-delete'),

    #  Серии
    path('series/', views.Series.as_view(), name='series'),
    path('series/<int:pk>/', views.Seria.as_view(), name='seria'),
    path('series-create/', views.Series_create.as_view(), name='series-create'),
    path('series-update/<int:pk>/', views.Series_update.as_view(), name='series-update'),
    path('series-delete/<int:pk>/', views.Series_delete.as_view(), name='series-delete'),

    ]