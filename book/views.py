from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Book
from .serializers import BookReadSerializer, BookCreateUpdateSerializer

class BookListAPIView(ListAPIView):
    serializer_class = BookReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        id = self.request.query_params.get('id')
        title = self.request.query_params.get('title')
        gte_page_count = self.request.query_params.get('gte_page_count')
        lte_page_count = self.request.query_params.get('lte_page_count')
        genre_ids = self.request.query_params.get('genre_ids')
        author_ids = self.request.query_params.get('author_ids')
        if id and title and gte_page_count and lte_page_count and genre_ids and author_ids:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE id = %s AND title = %s AND page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.id) AND %s IN (SELECT reader_id FROM book_authors BA WHERE BA.book_id = B.id)',
                [id, title, gte_page_count, lte_page_count, genre_ids, author_ids]
            )
        elif id and title and gte_page_count and lte_page_count and genre_ids:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE id = %s AND title = %s AND page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.id)',
                [id, title, gte_page_count, lte_page_count, genre_ids]
            )
        elif id and title and gte_page_count and lte_page_count:
            return Book.objects.raw(
                'SELECT * FROM book WHERE id = %s AND title = %s AND page_count >= %s AND page_count <= %s',
                [id, title, gte_page_count, lte_page_count]
            )
        elif id and title and gte_page_count:
            return Book.objects.raw(
                'SELECT * FROM book WHERE id = %s AND title = %s AND page_count >= %s',
                [id, title, gte_page_count]
            )
        elif id and title:
            return Book.objects.raw(
                'SELECT * FROM book WHERE id = %s AND title = %s',
                [id, title]
            )
        elif id:
            return Book.objects.raw(
                'SELECT * FROM book WHERE id = %s',
                [id]
            )
        elif title and gte_page_count and lte_page_count and genre_ids and author_ids:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE title = %s AND page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.id) AND %s IN (SELECT reader_id FROM book_authors BA WHERE BA.book_id = B.id)',
                [title, gte_page_count, lte_page_count, genre_ids, author_ids]
            )
        elif title and gte_page_count and lte_page_count and genre_ids:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE title = %s AND page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.id)',
                [title, gte_page_count, lte_page_count, genre_ids]
            )
        elif title and gte_page_count and lte_page_count:
            return Book.objects.raw(
                'SELECT * FROM book WHERE title = %s AND page_count >= %s AND page_count <= %s',
                [title, gte_page_count, lte_page_count]
            )
        elif title and gte_page_count:
            return Book.objects.raw(
                'SELECT * FROM book WHERE title = %s AND page_count >= %s',
                [title, gte_page_count]
            )
        elif title:
            return Book.objects.raw(
                'SELECT * FROM book WHERE title = %s',
                [title]
            )
        elif gte_page_count and lte_page_count and genre_ids and author_ids:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.id) AND %s IN (SELECT reader_id FROM book_authors BA WHERE BA.book_id = B.id)',
                [gte_page_count, lte_page_count, genre_ids, author_ids]
            )
        elif gte_page_count and lte_page_count and genre_ids:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.id)',
                [gte_page_count, lte_page_count, genre_ids]
            )
        elif gte_page_count and lte_page_count:
            return Book.objects.raw(
                'SELECT * FROM book WHERE page_count >= %s AND page_count <= %s',
                [gte_page_count, lte_page_count]
            )
        elif gte_page_count:
            return Book.objects.raw(
                'SELECT * FROM book WHERE page_count >= %s',
                [gte_page_count]
            )
        elif genre_ids and author_ids:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.id) AND %s IN (SELECT reader_id FROM book_authors BA WHERE BA.book_id = B.id)',
                [genre_ids, author_ids]
            )
        elif genre_ids:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.id)',
                [genre_ids]
            )
        elif author_ids:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE %s IN (SELECT reader_id FROM book_authors BA WHERE BA.book_id = B.id)',
                [author_ids]
            )
        else:
            return Book.objects.raw(
                'SELECT * FROM book'
            )

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
