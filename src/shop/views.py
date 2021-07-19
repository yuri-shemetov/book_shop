from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from . import models, forms
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from orders import models as models_orders
from carts import models as models_carts
from users import models as models_users
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    books = models.Book.objects.all().order_by('-created')[0:3]
    raitings = models.Book.objects.all().order_by('-rating')[0:3]
    if models.Promo.objects.count() == 3:
        promo1 = models.Promo.objects.all()[0]
        promo2 = models.Promo.objects.all()[1]
        promo3 = models.Promo.objects.all()[2]
    else:
        promo1 = None
        promo2 = None
        promo3 = None

    context = {
        'books': books,
        'raitings': raitings,
        'promo1': promo1,
        'promo2': promo2,
        'promo3': promo3,
    }
    return render(request, 'shop/home.html',  context=context)

class Administration(UserPassesTestMixin, TemplateView):
    template_name = 'shop/administration.html'
    login_url = '/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_staff

class Book(DetailView):
    model = models.Book
    template_name = 'shop/book.html'

class BookUpdateRaiting(LoginRequiredMixin, FormView):
    form_class = forms.RaitingBookForm
    template_name = 'comments/error.html'
    login_url = '/login/'
    redirect_field_name = 'next'

    def form_valid(self, form):
        book_id = form.cleaned_data.get('book_id')
        about_book = models.Book.objects.get(pk=book_id)
        rating = float(form.cleaned_data.get('rating'))
        old_rating = float(about_book.rating)
        count_users = float(User.objects.count())
        new_rating = (old_rating*(count_users-1)+rating)/count_users
        about_book.rating = round(new_rating, 1)
        about_book.save()
        messages.add_message(self.request, messages.INFO, 'Спасибо за вашу оценку! Рейтинг обновлен.')
        return HttpResponseRedirect(reverse_lazy('book', args=[book_id]))

class Books(ListView):
    model = models.Book
    template_name = 'shop/books.html'
    ordering = 'name'
    paginate_by = 9

    def get_queryset(self):
        qs = super().get_queryset()
        filter = self.request.GET.get('filter')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(year__icontains=q))
        return qs

    def get_context_data(self, **kwargs):
        q = self.request.GET.get('q')
        return super().get_context_data(**kwargs)

class Promo(DetailView):
    model = models.Promo
    template_name = 'shop/promo-detail.html'

class BooksManagers(UserPassesTestMixin, ListView):
    model = models.Book
    template_name = 'shop/books-managers.html'
    login_url = '/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_staff

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

class OrderListView(UserPassesTestMixin, ListView):
    model = models_orders.Order
    template_name = 'shop/orders.html'
    paginate_by = 10
    ordering = '-created'
    login_url = '/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_staff

class OrderDetailView(UserPassesTestMixin, DetailView):
    model = models_carts.BookInCart
    template_name = 'shop/order-detail.html'
    login_url = '/login/'
    redirect_field_name = 'next'

    def test_func(self):
        return self.request.user.is_staff

    def get_object(self, queryset=None):
        # get cart
        goods_id = self.request.GET.get('filter')
        cart_order = models_orders.Order.objects.get(pk=goods_id)
        cart = models_carts.Cart.objects.all()
        for i in cart:
            j = '"'+str(i)+'"'
            if j == str(cart_order):
                id = i.pk
        cart = models_carts.Cart.objects.get(pk=id)
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        goods_id = self.request.GET.get('filter')
        cart = models_orders.Order.objects.get(pk=goods_id)
        users = models_users.UserDetail.objects.all()
        i = -1
        for user_name in users:
            i += 1
            if str(user_name) == str(cart.login):
                pk = users[i].pk
        context['full_name'] = cart.first_name + ' ' + cart.last_name
        context['phone_number'] = cart.phone_number
        context['name_pk'] = cart.pk
        context['created'] = cart.created
        context['updated'] = cart.updated
        context['login'] = cart.login
        context['status'] = cart.status
        context['login_number'] = pk
        return context

class UserListView(UserPassesTestMixin, ListView):
    model = models_users.UserDetail
    template_name = 'shop/users-list.html'
    paginate_by = 10
    login_url = '/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_staff

class UserDetailView(UserPassesTestMixin, ListView):
    model = models_users.UserDetail
    template_name = 'shop/user-detail-admin.html'
    login_url = '/login/'
    redirect_field_name = 'next'
    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        qs = super(UserDetailView, self).get_queryset()
        user_id = self.request.GET.get('filter')
        return qs.filter(pk=int(user_id))

class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = models_users.UserDetail
    form_class = forms.UserAdminForm
    template_name = 'shop/user-update-admin.html'
    success_url = reverse_lazy('users-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        info_id = self.request.GET.get('filter')
        context['back_id'] = info_id
        return context
        
    def test_func(self):
        return self.request.user.is_staff

class StatusUpdate(UserPassesTestMixin, UpdateView):
    model = models_orders.Order
    template_name = 'shop/status.html'
    form_class = forms.StatusForm
    success_url = reverse_lazy('orders')
    def test_func(self):
        return self.request.user.is_staff