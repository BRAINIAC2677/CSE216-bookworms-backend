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
        gte_page_count = self.request.query_params.get('gte_page_count')
        lte_page_count = self.request.query_params.get('lte_page_count')
        genre_id = self.request.query_params.get('genre_id')
        author_id = self.request.query_params.get('author_id')
        if gte_page_count and lte_page_count and genre_id and author_id:
            return Book.objects.raw(
                'SELECT * FROM get_books_glga(%s, %s, %s, %s)',
                [gte_page_count, lte_page_count, genre_id, author_id]
            )
        elif gte_page_count and lte_page_count and genre_id:
            return Book.objects.raw(
                'SELECT * FROM get_books_glg(%s, %s, %s)',
                [gte_page_count, lte_page_count, genre_id]
            )
        elif gte_page_count and lte_page_count:
            return Book.objects.raw(
                'SELECT * FROM get_books_gl(%s, %s)',
                [gte_page_count, lte_page_count]
            )
        elif gte_page_count:
            return Book.objects.raw(
                'SELECT * FROM get_books_g(%s)',
                [gte_page_count]
            )
        elif lte_page_count and genre_id and author_id:
            return Book.objects.raw(
                'SELECT * FROM get_books_lga(%s, %s, %s)',
                [lte_page_count, genre_id, author_id]
            )
        elif lte_page_count and genre_id:
            return Book.objects.raw(
                'SELECT * FROM get_books_lg(%s, %s)',
                [lte_page_count, genre_id]
            )
        elif lte_page_count:
            return Book.objects.raw(
                'SELECT * FROM get_books_l(%s)',
                [lte_page_count]
            )
        elif genre_id and author_id:
            return Book.objects.raw(
                'SELECT * FROM get_books_ga(%s, %s)',
                [genre_id, author_id]
            )
        elif genre_id:
            return Book.objects.raw(
                'SELECT * FROM get_books_gn(%s)',
                [genre_id]
            )
        elif author_id:
            return Book.objects.raw(
                'SELECT * FROM get_books_a(%s)',
                [author_id]
            )
        else:
            return Book.objects.raw(
                'SELECT * FROM get_books()'
            )

class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.raw('SELECT * FROM get_books()')
    serializer_class = BookCreateUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.raw('SELECT * FROM get_books()')
    serializer_class = BookReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'bid'

class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.raw('SELECT * FROM get_books()')
    serializer_class = BookCreateUpdateSerializer
    lookup_field = 'bid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.raw('SELECT * FROM get_books()')
    lookup_field = 'bid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
