from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from reader.permissions import IsReaderUserPermission
from library.permissions import IsLibraryUserPermission
from .serializers import BookBorrowReadSerializer, BookBorrowWriteSerializer
from .models import BookBorrow

class BookBorrowListAPIView(ListAPIView):
    serializer_class = BookBorrowReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return BookBorrow.objects.all()

class BookBorrowQueryListAPIView(ListAPIView):
    serializer_class = BookBorrowReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.query_params.get('borrowed_by_id') and self.request.query_params.get('borrowed_from_id'):
            borrowed_by_id = self.request.query_params.get('borrowed_by_id')
            borrowed_from_id = self.request.query_params.get('borrowed_from_id')
            return BookBorrow.objects.raw('SELECT * FROM book_borrow WHERE borrowed_by_id = %s AND borrowed_from_id = %s', [borrowed_by_id, borrowed_from_id])
        elif self.request.query_params.get('borrowed_by_id'):
            borrowed_by_id = self.request.query_params.get('borrowed_by_id')
            return BookBorrow.objects.raw('SELECT * FROM book_borrow WHERE borrowed_by_id = %s', [borrowed_by_id])
        elif self.request.query_params.get('borrowed_from_id'):
            borrowed_from_id = self.request.query_params.get('borrowed_from_id')
            return BookBorrow.objects.raw('SELECT * FROM book_borrow WHERE borrowed_from_id = %s', [borrowed_from_id])
        else:
            # returns empty queryset
            return BookBorrow.objects.none()

class LibraryBookBorrowListAPIView(ListAPIView):
    serializer_class = BookBorrowReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryUserPermission]

    def get_queryset(self):
        return BookBorrow.objects.filter(borrowed_from=self.request.user.library)

class BookBorrowCreateAPIView(CreateAPIView):
    queryset = BookBorrow.objects.all()
    serializer_class = BookBorrowWriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderUserPermission]

class BookBorrowDeleteAPIView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryUserPermission]
    lookup_field = 'bbid'

    def get_queryset(self):
        return BookBorrow.objects.filter(borrowed_from=self.request.user.library)
