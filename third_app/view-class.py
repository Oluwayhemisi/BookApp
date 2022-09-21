# class BookList(APIView):
#     def get(self, request):
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#
#
# class BookDetail(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book, context={'request': request})
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book, data=request.data, partial=True, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#
#     def delete(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class PublisherList(APIView):
#     def get(self, request):
#         publisher = Publisher.objects.all()
#         serializer = PublisherSerializer(publisher, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PublisherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#
#
# class PublisherDetail(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = PublisherSerializer(book, context={'request': request})
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = PublisherSerializer(book, data=request.data, partial=True, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
#
#     def delete(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


