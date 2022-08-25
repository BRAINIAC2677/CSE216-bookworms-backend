from django.urls import path

from .views import BookBorrowListAPIView, BookBorrowQueryListAPIView, BookBorrowCreateAPIView, BookBorrowDeleteAPIView

urlpatterns = [
    path('list/', BookBorrowListAPIView.as_view(), name='bookborrow-list'),
    path('querylist/', BookBorrowQueryListAPIView.as_view(), name='bookborrow-querylist'),
    path('create/', BookBorrowCreateAPIView.as_view(), name='bookborrow-create'),
    path('delete/<int:bbid>/', BookBorrowDeleteAPIView.as_view(), name='bookborrow-delete'),
]