from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from reader.permissions import IsReaderUserPermission
from library.permissions import IsLibraryUserPermission
from .serializers import BookBorrowReadSerializer, BookBorrowWriteSerializer
from .models import BookBorrow

class BookBorrowListAPIView(ListAPIView):
    queryset = BookBorrow.objects.all()
    serializer_class = BookBorrowReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

class ReaderBookBorrowListAPIView(ListAPIView):
    serializer_class = BookBorrowReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderUserPermission]

    def get_queryset(self):
        return BookBorrow.objects.filter(borrowed_by=self.request.user.reader)

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
