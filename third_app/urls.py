from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views


app_name = 'third_app'

# router = SimpleRouter()
router = DefaultRouter()
router.register('books', views.BookViewSet)
urlpatterns = [
    # path('index/', views.index, name='index'),
    # path('first/', views.okay,name='get'),
    # path('', views.redirect),
    # path('about/', views.about, name='about'),
    # path('book-list/', views.book_list, name='book-list'),
    # path('book-detail/<int:pk>/', views.book_detail, name='book-detail'),

    #URL FOR CLASS VIEW
    # path('books/', views.BookList.as_view(), name="book-list"),
    # path('books/<int:pk>', views.BookDetail.as_view(), name="book-detail"),
    # path('publishers/', views.PublisherList.as_view(), name="publisher-list"),
    # path('publishers/<int:pk>', views.PublisherDetail.as_view(), name="publisher-detail"),



    #URL FOR FUNCTIONAL VIEW
    # path('books/', views.book_list, name="book-list"),
    # path('books/<int:pk>', views.book_detail, name="book-detail"),
    # path('publishers/', views.publisher_list, name="publisher-list"),
    # path('publishers/<int:pk>', views.publisher_detail, name="publisher-detail")

#     URL FOR GENERICS VIEW
    path('',include(router.urls))
]