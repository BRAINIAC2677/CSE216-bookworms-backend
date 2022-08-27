from django.urls import path

from .views import BookBorrowListAPIView, BookBorrowDetailAPIView, BookBorrowCreateAPIView, BookBorrowDeleteAPIView

urlpatterns = [
    path('list/', BookBorrowListAPIView.as_view(), name='bookborrow-list'),
    path('detail/<int:bbid>/', BookBorrowDetailAPIView.as_view(), name='bookborrow-detail'),
    path('create/', BookBorrowCreateAPIView.as_view(), name='bookborrow-create'),
    path('delete/<int:bbid>/', BookBorrowDeleteAPIView.as_view(), name='bookborrow-delete'),
]