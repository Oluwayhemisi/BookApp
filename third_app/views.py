from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path, reverse
from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BookSerializer, PublisherSerializer
from rest_framework import status

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


@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        queryset = Book.objects.all()
        serializer = BookSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', ' PATCH', 'DELETE'])
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # book = Book.objects.get(pk=pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    elif request.method in ('PUT', 'PATCH'):
        serializer = BookSerializer(Book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # try:
    #     book =Book.objects.get(pk=pk)
    #     serializer = BookSerializer(book)
    #     return Response(serializer.data)
    # except:Book.DoesNotExist:
    #     return Response({"error":"could not find resource"}, status= status.HTTP_404_NOT_FOUND)


@api_view()
def publisher_list(request):
    publisher = Publisher.objects.all()
    serializer = PublisherSerializer(publisher, many=True)
    return Response(serializer.data)


@api_view()
def publisher_detail(request, pk):
    book = get_object_or_404(Publisher, pk=pk)
    serializer = PublisherSerializer(book)
    return Response(serializer.data)
