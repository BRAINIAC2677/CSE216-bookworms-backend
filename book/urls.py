from django.urls import path 

from .views import BookListAPIView, BookCreateAPIView, BookRetrieveAPIView, BookUpdateAPIView, BookDestroyAPIView
urlpatterns = [
    path('list/', BookListAPIView.as_view(), name='book-list'),
    path('create/', BookCreateAPIView.as_view(), name='book-create'),
    path('detail/<str:bid>/', BookRetrieveAPIView.as_view(), name='book-detail'),
    path('update/<str:bid>/', BookUpdateAPIView.as_view(), name='book-update'),
    path('delete/<str:bid>/', BookDestroyAPIView.as_view(), name='book-delete'),
]