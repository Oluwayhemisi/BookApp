from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AdminUser

from .models import Book, Publisher, User


# Register your models here.
@admin.register(User)
class UserAdmin(AdminUser):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),

            },
        ),
    )


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
