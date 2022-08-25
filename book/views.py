from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Book
from .serializers import BookReadSerializer, BookWriteSerializer

class BookListAPIView(ListAPIView):
    serializer_class = BookReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        isbn = self.request.query_params.get('isbn')
        title = self.request.query_params.get('title')
        gte_page_count = self.request.query_params.get('gte_page_count')
        lte_page_count = self.request.query_params.get('lte_page_count')
        genre_ids = self.request.query_params.get('genre_ids')
        author_ids = self.request.query_params.get('author_ids')
        if isbn and title and gte_page_count and lte_page_count and genre_ids and author_ids:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE isbn = %s AND title = %s AND page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.id) AND %s IN (SELECT author_id FROM book_authors BA WHERE BA.book_id = B.id)',
                [isbn, title, gte_page_count, lte_page_count, genre_ids, author_ids]
            )
        return Book.objects.all()

    

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookWriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookReadSerializer
    lookup_field = 'isbn'

class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookWriteSerializer
    lookup_field = 'isbn'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = 'isbn'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
