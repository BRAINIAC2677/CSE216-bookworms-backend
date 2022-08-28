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
        bid = self.request.query_params.get('bid')
        title = self.request.query_params.get('title')
        gte_page_count = self.request.query_params.get('gte_page_count')
        lte_page_count = self.request.query_params.get('lte_page_count')
        genre_id = self.request.query_params.get('genre_id')
        author_id = self.request.query_params.get('author_id')
        if bid and title and gte_page_count and lte_page_count and genre_id and author_id:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE bid = %s AND title = %s AND page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.bid) AND %s IN (SELECT reader_id FROM book_authors BA WHERE BA.book_id = B.bid)',
                [bid, title, gte_page_count, lte_page_count, genre_id, author_id]
            )
        elif bid and title and gte_page_count and lte_page_count and genre_id:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE bid = %s AND title = %s AND page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.bid)',
                [bid, title, gte_page_count, lte_page_count, genre_id]
            )
        elif bid and title and gte_page_count and lte_page_count:
            return Book.objects.raw(
                'SELECT * FROM book WHERE bid = %s AND title = %s AND page_count >= %s AND page_count <= %s',
                [bid, title, gte_page_count, lte_page_count]
            )
        elif bid and title and gte_page_count:
            return Book.objects.raw(
                'SELECT * FROM book WHERE bid = %s AND title = %s AND page_count >= %s',
                [bid, title, gte_page_count]
            )
        elif bid and title:
            return Book.objects.raw(
                'SELECT * FROM book WHERE bid = %s AND title = %s',
                [bid, title]
            )
        elif bid:
            return Book.objects.raw(
                'SELECT * FROM book WHERE bid = %s',
                [bid]
            )
        elif title and gte_page_count and lte_page_count and genre_id and author_id:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE title = %s AND page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.bid) AND %s IN (SELECT reader_id FROM book_authors BA WHERE BA.book_id = B.bid)',
                [title, gte_page_count, lte_page_count, genre_id, author_id]
            )
        elif title and gte_page_count and lte_page_count and genre_id:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE title = %s AND page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.bid)',
                [title, gte_page_count, lte_page_count, genre_id]
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
        elif gte_page_count and lte_page_count and genre_id and author_id:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.bid) AND %s IN (SELECT reader_id FROM book_authors BA WHERE BA.book_id = B.bid)',
                [gte_page_count, lte_page_count, genre_id, author_id]
            )
        elif gte_page_count and lte_page_count and genre_id:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE page_count >= %s AND page_count <= %s AND %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.bid)',
                [gte_page_count, lte_page_count, genre_id]
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
        elif genre_id and author_id:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.bid) AND %s IN (SELECT reader_id FROM book_authors BA WHERE BA.book_id = B.bid)',
                [genre_id, author_id]
            )
        elif genre_id:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE %s IN (SELECT genre_id FROM book_genres BG WHERE BG.book_id = B.bid)',
                [genre_id]
            )
        elif author_id:
            return Book.objects.raw(
                'SELECT * FROM book B WHERE %s IN (SELECT reader_id FROM book_authors BA WHERE BA.book_id = B.bid)',
                [author_id]
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
    lookup_field = 'bid'

class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateUpdateSerializer
    lookup_field = 'bid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    lookup_field = 'bid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
