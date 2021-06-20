from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from . import models, forms
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

def home(request):
    books = models.Book.objects.all().order_by('-created')[0:3]
    raitings = models.Book.objects.all().order_by('-rating')[0:3]
    promo1 = models.Promo.objects.all()[0]
    promo2 = models.Promo.objects.all()[1]
    promo3 = models.Promo.objects.all()[2]
    context = {'books': books, 'raitings': raitings, 'promo1': promo1, 'promo2': promo2, 'promo3': promo3,}
    return render(request, 'shop/home.html', context=context)

class Administration(LoginRequiredMixin, TemplateView):
    template_name = 'shop/administration.html'
    login_url = '/login/'
    redirect_field_name = 'next'

class Book(DetailView):
    model = models.Book
    template_name = 'shop/book.html'

class Books(ListView):
    model = models.Book
    template_name = 'shop/books.html'

class BooksManagers(LoginRequiredMixin, ListView):
    model = models.Book
    template_name = 'shop/books-managers.html'
    login_url = '/login/'
    redirect_field_name = 'next'

class Book_create(PermissionRequiredMixin, CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'shop/book-create.html'
    login_url = '/login/'
    permission_required = 'shop.add_book'

class Book_update(PermissionRequiredMixin, UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'shop/book-update.html'
    login_url = '/login/'
    permission_required = 'shop.change_book' 

class Book_delete(PermissionRequiredMixin, DeleteView):
    model = models.Book
    success_url = reverse_lazy('books')
    template_name = 'shop/book-delete.html'
    login_url = '/login/'
    permission_required = 'shop.delete_book' 

class Promo_List(LoginRequiredMixin, ListView):
    model = models.Promo
    template_name = 'shop/promo.html'
    login_url = '/login/'
    redirect_field_name = 'next'

class Promo(DetailView):
    model = models.Promo
    template_name = 'shop/promo-detail.html'

class Promo_create(PermissionRequiredMixin, CreateView):
    model = models.Promo
    form_class = forms.PromoForm
    template_name = 'shop/promo-create.html'
    login_url = '/login/'
    permission_required = 'shop.add_promo'

class Promo_update(PermissionRequiredMixin, UpdateView):
    model = models.Promo
    form_class = forms.PromoForm
    template_name = 'shop/promo-update.html'
    login_url = '/login/'
    permission_required = 'shop.change_promo' 

class Promo_delete(PermissionRequiredMixin, DeleteView):
    model = models.Promo
    success_url = reverse_lazy('promo')
    template_name = 'shop/promo-delete.html'
    login_url = '/login/'
    permission_required = 'shop.delete_promo' 