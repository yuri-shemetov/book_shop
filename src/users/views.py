from django.contrib.auth import login, logout, views, forms, models
from .forms import RegisterForm, UserForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView, ListView, CreateView
from . import models as my_models
from carts import models as models_cart
from orders import models as models_order
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User



class MyLogin(views.LoginView):
    login_url = '/login/'
    template_name = 'users/login.html'
    redirect_field_name = 'next'

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def user_register(request):
    template = 'users/register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if models.User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = models.User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['password'],
                    form.cleaned_data['password_repeat'],
                )
                user.email = form.cleaned_data['email']
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.groups.add(models.Group.objects.get(name='Customers'))
                user.save()
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = RegisterForm()

    messages.add_message(request, messages.INFO, 'Поздравляем Вас с успешной регистрацией!')

    return render(request, template, {'form': form})

class User(LoginRequiredMixin, ListView):
    model = models_order.Order
    template_name = 'users/user.html'
    ordering = '-created'
    login_url = '/users/login/'
    redirect_field_name = 'next'

    def get_queryset(self):
        qs = super(User, self).get_queryset()
        user_name = self.request.user.username
        return qs.filter(login=user_name)

class UserOrderList(LoginRequiredMixin, DetailView):
    model = models_cart.BookInCart
    template_name = 'users/user-order-detail.html'
    login_url = '/users/login/'
    redirect_field_name = 'next'

    def get_object(self, queryset=None):
        # get cart
        goods_id = self.request.GET.get('filter')
        cart_order = models_order.Order.objects.get(pk=goods_id)
        cart = models_cart.Cart.objects.all()
        for i in cart:
            j = '"'+str(i)+'"'
            if j == str(cart_order):
                id = i.pk

        cart = models_cart.Cart.objects.get(pk=id)
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        goods_id = self.request.GET.get('filter')
        cart_order = models_order.Order.objects.get(pk=goods_id)
        context['cart_pk'] = cart_order.pk
        context['status'] = cart_order.status
        return context

class StatusCancel(LoginRequiredMixin, DetailView):
    model = models_order.Order
    template_name = 'users/status-cancel.html'
    login_url = '/users/login/'
    redirect_field_name = 'next'
    def get_object(self, queryset=None):
        # get order
        goods_id = self.request.GET.get('filter')
        cart_order = models_order.Order.objects.get(pk=goods_id)
        status = models_order.Status.objects.get(pk=4) # pk = 4 - СТАТУС ОТМЕНЕН!!!
        cart_order.status = status
        cart_order.save()
        return cart_order

class ChP(views.PasswordChangeView):
    form_class = forms.PasswordChangeForm
    template_name = 'users/change-password.html'

class UserListView(LoginRequiredMixin, ListView):
    model = my_models.UserDetail
    template_name = 'users/user-detail.html'
    login_url = '/users/login/'
    redirect_field_name = 'next'

class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = my_models.UserDetail
    form_class = UserForm
    template_name = 'users/user-update.html'

    def form_valid(self, form):
        user_add = self.request.user
        user_add.email = form.cleaned_data.get('email')
        user_add.first_name = form.cleaned_data.get('first_name')
        user_add.last_name = form.cleaned_data.get('last_name')
        user_add.save()
        return super().form_valid(form)
   
    def get_initial(self):
        username = self.request.user
        first_name = self.request.user.first_name
        last_name = self.request.user.last_name
        email = self.request.user.email
        return {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email}

    def get_success_message(self, cleaned_data):
        return f'Ваши данные успешно обновлены!'
    
class UserCreateView(SuccessMessageMixin, CreateView):
    model = my_models.UserDetail
    form_class = UserForm
    template_name = 'users/user-create.html'

    def get_initial(self):
        username = self.request.user
        first_name = self.request.user.first_name
        last_name = self.request.user.last_name
        email = self.request.user.email
        phone_number = f'+375(29)...'
        return {'username': username, 'first_name': first_name, 'last_name': last_name, 'email': email}

    def form_valid(self, form):
        user_add = self.request.user
        user_add.email = form.cleaned_data.get('email')
        user_add.first_name = form.cleaned_data.get('first_name')
        user_add.last_name = form.cleaned_data.get('last_name')
        user_add.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return f'Ваши данные успешно добавлены!'

class UsersAllView(LoginRequiredMixin, ListView):
    model = models.User
    template_name = 'users/users-all.html'
    login_url = '/users/login/'
    redirect_field_name = 'next'

class UserOtherView(LoginRequiredMixin, ListView):
    model = my_models.UserDetail
    template_name = 'users/other-user.html'
    login_url = '/users/login/'
    redirect_field_name = 'next'
    def get_queryset(self):
        qs = super(UserOtherView, self).get_queryset()
        user_id = self.request.GET.get('filter')
        login_user = models.User.objects.get(pk=user_id)
        about_users = my_models.UserDetail.objects.all()
        pk=0
        for this_user in about_users:
            if str(this_user) == str(login_user):
                pk = this_user.pk
        if pk == 0:
            messages.add_message(self.request, messages.INFO, 'Карточка данного пользователя отсутствует!')
        else:
            return qs.filter(pk=pk)

class UserAdminView(LoginRequiredMixin, ListView):
    model = my_models.UserDetail
    template_name = 'users/admin-user.html'
    login_url = '/users/login/'
    redirect_field_name = 'next'
    def get_queryset(self):
        qs = super(UserAdminView, self).get_queryset()
        user_id = self.request.GET.get('filter')
        login_user = models.User.objects.get(pk=user_id)
        about_users = my_models.UserDetail.objects.all()
        for this_user in about_users:
            if str(this_user) == str(login_user):
                pk = this_user.pk
        return qs.filter(pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.GET.get('filter')
        login_user = models.User.objects.get(pk=user_id)
        context['first_name'] = login_user.first_name
        context['last_name'] = login_user.last_name
        context['email'] = login_user.email
        return context