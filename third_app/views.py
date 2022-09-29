from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path, reverse
from django.db import connection
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter,OrderingFilter
from .filter import BookFilter
from .pagination import BookPagination
from .serializer import BookSerializer, PublisherSerializer
from rest_framework import status, request
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin

# Create your views here.
from third_app.models import Book, Publisher


#
# def index(request):
#     head = "yemisi!!!"
#     context = [1, 2, 3, 4, 5, 9, 11]
#     return render(request, 'third_app/index.html', context={"name": head})
#
#
# def about(request):
#     return render(request, 'third_app/about.html')
#
#
# def okay(request):
#     return HttpResponse("Hmm!")
#
#
# def redirect(request):
#     print(reverse('my_app:get'))
#     return HttpResponseRedirect((reverse('third_app:get')))
#
#
# def book_list(request):
#     books = Book.objects.all()
# books = Book.objects.filter(genre='FICTION')
# books = Book.objects.filter(price__gt=50.00)
# books = Book.objects.filter(title__contains='and')
# books = Book.objects.filter(publisher__id__in='7,80,44').order_by('title','price').reverse()
# books = Book.objects.filter(publisher__id__in='7,80,44')[3]
# books = Book.objects.filter(publisher__id__in='7,80,44').values('title','price')
# books = Book.objects.filter(publisher__id__in='7,80,44').only('title','price')
# books = Book.objects.defer('title','price')
# books = Book.objects.select_related('publisher').all()

# cursor = connection.cursor()
# result = cursor.execute("select * from third_app_book")
# books = result.fetchall()
# return render(request, 'third_app/book-list.html', {'books': list(books)})


# def book_detail(request, pk):
#     book = get_object_or_404(Book,pk=pk)
#     return render(request, 'third_app/book-detail.html', {'book': book})

# def story(request):
#     return HttpResponseRedirect("The title of my story is, ")
#


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['price']
    ordering_fields  = ['title', 'price']
    pagination_class = BookPagination
