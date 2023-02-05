from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


from rest_framework.viewsets import ModelViewSet

from .model import BookModelSerializer
from .models import Book


class BooksView(APIView):
    """
    列出所有的snippets或者创建一个新的snippet。
    """

    def get(self, request, format=None):
        snippets = Book.objects.all()
        serializer = BookModelSerializer(snippets, many=True)
        return Response(serializer.data)

# class BooksViewSet(ModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookModelSerializer
