from django import forms
from . import models
from django.core.exceptions import ValidationError

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = (
            'picture',
            'name',
            'price',
            'author',
            'seria',
            'genre',
            'year',
            'pages',
            'binding',
            'form',
            'isbn',
            'weight',
            'age',
            'publisher',
            'quantity',
            'avtive',
            'rating',
        )
    def clean_number(self):
        value = self.cleaned_data.get('year')
        if value < 1900:
            raise ValidationError("Минимальный год не может быть меньше 1900!!!")
        elif value > 2021:
            raise ValidationError("Максимальный год не может быть больше 2021!!!")
        return value

class PromoForm(forms.ModelForm):
    class Meta:
        model = models.Promo
        fields = (
            'picture',
            'name',
            'description',
        )