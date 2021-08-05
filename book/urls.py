from django.urls import path
from .views import BookList, post_book, update_book, delete_book

urlpatterns = [
    path('', BookList),
    path('add/', post_book),
    path('update/<int:id>/', update_book),
    path('delete/<int:id>/', delete_book),
]
