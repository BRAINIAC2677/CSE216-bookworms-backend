from django.urls import path

from .views import BookBorrowListAPIView, ReaderBookBorrowListAPIView, LibraryBookBorrowListAPIView, BookBorrowCreateAPIView, BookBorrowDeleteAPIView

urlpatterns = [
    path('', BookBorrowListAPIView.as_view(), name='bookborrow-list'),
    path('reader/', ReaderBookBorrowListAPIView.as_view(), name='reader-bookborrow-list'),
    path('library/', LibraryBookBorrowListAPIView.as_view(), name='library-bookborrow-list'),
    path('create/', BookBorrowCreateAPIView.as_view(), name='bookborrow-create'),
    path('delete/<int:bbid>/', BookBorrowDeleteAPIView.as_view(), name='bookborrow-delete'),
]