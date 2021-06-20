from django import forms
from . import models
from django.core.exceptions import ValidationError

class AuthorsForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = (
            'number',
            'name',
        )

    def clean_number(self):
        value = self.cleaned_data.get('number')
        if value < 1:
            raise ValidationError("Минимальное количество не может быть меньше 1!!!")
        elif value > 9:
            raise ValidationError("Максимальное количество не может быть больше 9!!!")
        return value

class PublishersForm(forms.ModelForm):
    class Meta:
        model = models.Publisher
        fields = (
            'name',
            'city',
        )

class GenresForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = (
            'name',
            'description',
        )

class SeriesForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = (
            'series',
        )