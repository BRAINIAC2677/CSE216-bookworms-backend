from django.urls import path 

from .views import BookListAPIView, BookCreateAPIView, BookRetrieveAPIView, BookUpdateAPIView, BookDestroyAPIView
urlpatterns = [
    path('', BookListAPIView.as_view(), name='book-list'),
    path('create/', BookCreateAPIView.as_view(), name='book-create'),
    path('<int:isbn>/', BookRetrieveAPIView.as_view(), name='book-detail'),
    path('<int:isbn>/update/', BookUpdateAPIView.as_view(), name='book-update'),
    path('<int:isbn>/delete/', BookDestroyAPIView.as_view(), name='book-delete'),
]