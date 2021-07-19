from rest_framework.views import APIView
from . import serializers, models
from rest_framework.response import Response
from rest_framework import viewsets

class BookAPIView(APIView):
    def get(self, request, pk, format=None):
        obj = models.Book.objects.get(pk=pk)
        ser_obj = serializers.BookSerializer(obj, many=False)
        return Response(ser_obj.data)

class BookAPIViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.BookSerializer
    queryset = models.Book.objects.all()
