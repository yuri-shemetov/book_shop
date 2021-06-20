from django.contrib.auth import login, logout, models, views
from .forms import RegisterForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.contrib.auth import forms
from django.contrib.auth import views as auth_views


class MyLogin(views.LoginView):
    login_url = '/login/'
    template_name = 'users/login.html'
    redirect_field_name = 'next'

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'users/register.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if models.User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif models.User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
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
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.country = form.cleaned_data['country']
                user.city = form.cleaned_data['city']
                user.index = form.cleaned_data['index']
                user.address_1 = form.cleaned_data['address_1']
                user.address_2 = form.cleaned_data['address_2']
                user.groups.add(models.Group.objects.get(name='Customers'))

                user.save()

                # Login the user
                login(request, user)

                # redirect to accounts page:
                return HttpResponseRedirect('/')

    # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

class User(TemplateView):
    template_name = 'users/user.html'

class ChP(auth_views.PasswordChangeView):
    form_class = forms.PasswordChangeForm
    template_name='users/change-password.html'