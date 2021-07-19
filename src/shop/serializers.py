from rest_framework import serializers
from . import models

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['pk',
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
                  'rating',]