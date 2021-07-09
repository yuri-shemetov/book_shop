from django.views.generic import FormView
from . import forms, models
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from carts import models as models_cart
from users import models as models_user
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateOrder(LoginRequiredMixin, FormView):
    form_class = forms.OrderCreateForm
    template_name = 'orders/create-order.html'
    success_url = reverse_lazy('orders:thanks')
    login_url = '/users/login/'
    redirect_field_name = 'next'

    def get_initial(self):
        if self.request.user.is_anonymous:
            return {}
        else:
            login = self.request.user.username
            first_name = self.request.user.first_name
            last_name = self.request.user.last_name
            for us in models_user.UserDetail.objects.all():
                user_string = str(us)
                if user_string == login:
                    phone_number = self.request.user.profile.phone_number
                    break
                else:
                    phone_number = ''
        return {'login': login, 'first_name': first_name, 'last_name': last_name, 'phone_number': phone_number}

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        cart, created = models_cart.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={},
        )
        if created:
            return HttpResponseRedirect(reverse_lazy('cart-edit'))
        status = models.Status.objects.get(pk=1)
        login = self.request.user.username
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        phone_number = form.cleaned_data.get('phone_number')
        models.Order.objects.create(
            cart=cart,
            status=status,
            login=login,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        # Проверка карточки пользователя. Если ее нет - создаем карточку.
        number = 0
        pk_user = self.request.user.pk
        all_users_list = models_user.UserDetail.objects.values('username')
        for all_user in all_users_list:
            for key, value in all_user.items():
                if value == pk_user:
                    number += 1
        if number == 0:
            models_user.UserDetail.objects.create(
                username=self.request.user,
                phone_number=phone_number,
            )

        self.request.session.pop('cart_id')
        
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id')
        cart, created = models_cart.Cart.objects.get_or_create(
            pk=cart_id,
            defaults={},
        )
        context['object'] = cart
        return context

class Thanks(TemplateView):
    template_name = 'orders/thanks.html'
