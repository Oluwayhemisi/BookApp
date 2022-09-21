from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from third_app.models import Publisher, Book
from third_app.serializer import PublisherSerializer, BookSerializer


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
        serializer = BookSerializer(book, context={'request': request})
        return Response(serializer.data)
    elif request.method in ('PUT', 'PATCH'):
        serializer = BookSerializer(Book, data=request.data, partial=True, context={'request': request})
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


@api_view(['GET', 'POST'])
def publisher_list(request):
    if request.method == 'GET':
        publisher = Publisher.objects.all()
        serializer = PublisherSerializer(publisher, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PublisherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', ' PATCH', 'DELETE'])
def publisher_detail(request, pk):
    book = get_object_or_404(Publisher, pk=pk)
    if request.method == 'GET':
        serializer = PublisherSerializer(book, context={'request': request})
        return Response(serializer.data)
    elif request.method in ('PUT', 'PATCH'):
        serializer = PublisherSerializer(Book, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = PublisherSerializer(book)
    return Response(serializer.data)
