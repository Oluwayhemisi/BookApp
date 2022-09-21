from rest_framework.viewsets import ModelViewSet

from third_app.models import Book
from third_app.serializer import BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
