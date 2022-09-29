from django_filters import FilterSet

from third_app.models import Book


class BookFilter(FilterSet):
    class Meta:
        model = Book
        fields = {
            'isbn': ['exact'],
            'title': ['exact', 'contains'],
            'date_published': ['isnull'],
            'price': ['gt', 'lt']
        }
