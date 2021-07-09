from django import forms

class OrderCreateForm(forms.Form):
    first_name = forms.CharField(
        label='Имя',
        max_length=15,
        required=True,
        widget=forms.TextInput,
    )
    last_name = forms.CharField(
        label='Фамилия',
        max_length=20,
        required=True,
        widget=forms.TextInput,
    )
    phone_number = forms.CharField(
        label='Телефон',
        required=True,
        widget=forms.TextInput,
    )