from django.contrib import admin
from .models import Book, Publisher


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['publisher']
    date_hierarchy = 'date_published'
    list_display = ('title', 'price', 'isbn')
    search_fields = ('title', 'isbn__exact', 'publisher_name_startswith')
    list_filter = ('publisher', 'date_published')
    list_select_related = ('publisher',)
    list_per_page = 10


admin.site.register(Publisher)
