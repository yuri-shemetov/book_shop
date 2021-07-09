from . import models
from . import forms
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

# Справочники

class HomePage(TemplateView):
    template_name = 'directories/directories.html'

# Авторы

class Authors(ListView):
    model = models.Author
    template_name = 'directories/authors.html'

class Author(DetailView):
    model = models.Author
    template_name = 'directories/author.html'

class Author_create(PermissionRequiredMixin, CreateView):
    model = models.Author
    form_class = forms.AuthorsForm
    template_name = 'directories/authors_create.html'
    login_url = '/login/'
    permission_required = 'directories.add_author'

class Author_update(PermissionRequiredMixin, UpdateView):
    model = models.Author
    form_class = forms.AuthorsForm
    template_name = 'directories/authors_update.html'
    login_url = '/login/'
    permission_required = 'directories.change_author'

class Author_delete(PermissionRequiredMixin, DeleteView):
    model = models.Author
    success_url = reverse_lazy('authors')
    template_name = 'directories/authors_delete.html'
    login_url = '/login/'
    permission_required = 'directories.delete_author'

# Издательства

class Publishers(ListView):
    model = models.Publisher
    template_name = 'directories/publishers.html'

class Publisher(DetailView):
    model = models.Publisher
    template_name = 'directories/publisher.html'

class Publishers_create(PermissionRequiredMixin, CreateView):
    model = models.Publisher
    form_class = forms.PublishersForm
    template_name = 'directories/publishers_create.html'
    login_url = '/login/'
    permission_required = 'directories.add_publisher'

class Publishers_update(PermissionRequiredMixin, UpdateView):
    model = models.Publisher
    form_class = forms.PublishersForm
    template_name = 'directories/publishers_update.html'
    login_url = '/login/'
    permission_required = 'directories.change_publisher'

class Publishers_delete(PermissionRequiredMixin, DeleteView):
    model = models.Publisher
    success_url = reverse_lazy('publishers')
    template_name = 'directories/publishers_delete.html'
    login_url = '/login/'
    permission_required = 'directories.delete_publisher'

# Жанры

class Genres(ListView):
    model = models.Genre
    template_name = 'directories/genres.html'

class Genre(DetailView):
    model = models.Genre
    template_name = 'directories/genre.html'

class Genres_create(PermissionRequiredMixin, CreateView):
    model = models.Genre
    form_class = forms.GenresForm
    template_name = 'directories/genres_create.html'
    login_url = '/login/'
    permission_required = 'directories.add_genre'

class Genres_update(PermissionRequiredMixin, UpdateView):
    model = models.Genre
    form_class = forms.GenresForm
    template_name = 'directories/genres_update.html'
    login_url = '/login/'
    permission_required = 'directories.change_genre'

class Genres_delete(PermissionRequiredMixin, DeleteView):
    model = models.Genre
    success_url = reverse_lazy('genres')
    template_name = 'directories/genres_delete.html'
    login_url = '/login/'
    permission_required = 'directories.delete_genre'

# Серии

class Series(ListView):
    model = models.Series
    template_name = 'directories/series.html'

class Seria(DetailView):
    model = models.Series
    template_name = 'directories/seria.html'

class Series_create(PermissionRequiredMixin, CreateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'directories/series_create.html'
    login_url = '/login/'
    permission_required = 'directories.add_series'

class Series_update(PermissionRequiredMixin, UpdateView):
    model = models.Series
    form_class = forms.SeriesForm
    template_name = 'directories/series_update.html'
    login_url = '/login/'
    permission_required = 'directories.change_series'

class Series_delete(PermissionRequiredMixin, DeleteView):
    model = models.Series
    success_url = reverse_lazy('series')
    template_name = 'directories/series_delete.html'
    login_url = '/login/'
    permission_required = 'directories.delete_series'
