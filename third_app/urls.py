from django.urls import path
from . import views


app_name = 'third_app'
urlpatterns = [
    # path('index/', views.index, name='index'),
    # path('first/', views.okay,name='get'),
    # path('', views.redirect),
    # path('about/', views.about, name='about'),
    # path('book-list/', views.book_list, name='book-list'),
    # path('book-detail/<int:pk>/', views.book_detail, name='book-detail'),

    #URL FOR CLASS VIEW
    path('books/', views.BookList.as_view(), name="book-list"),
    path('books/<int:pk>', views.BookList.as_view(), name="book-detail"),
    path('publishers/', views.publisher_list, name="publisher-list"),
    path('publishers/<int:pk>', views.publisher_detail, name="publisher-detail"),



    #URL FOR FUNCTIONAL VIEW
    # path('books/', views.book_list, name="book-list"),
    # path('books/<int:pk>', views.book_detail, name="book-detail"),
    # path('publishers/', views.publisher_list, name="publisher-list"),
    # path('publishers/<int:pk>', views.publisher_detail, name="publisher-detail")
]