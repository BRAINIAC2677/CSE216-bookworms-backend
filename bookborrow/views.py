from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from reader.permissions import IsReaderUserPermission
from .permissions import IsBookLenderPermission
from .serializers import BookBorrowReadSerializer, BookBorrowCreateSerializer
from .models import BookBorrow

class BookBorrowListAPIView(ListAPIView):
    serializer_class = BookBorrowReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        rid = self.request.query_params.get('rid', None)
        lid = self.request.query_params.get('lid', None)
        if rid and lid:
            return BookBorrow.objects.raw(
                'SELECT * FROM book_borrow WHERE borrowed_by_id = %s AND borrowed_from_id = %s',
                [rid, lid]
            )
        elif rid:
            return BookBorrow.objects.raw(
                'SELECT * FROM book_borrow WHERE borrowed_by_id = %s',
                [rid]
            )
        elif lid:
            return BookBorrow.objects.raw(
                'SELECT * FROM book_borrow WHERE borrowed_from_id = %s',
                [lid]
            )
       # if the requested user is admin, return all the book borrows
        elif self.request.user.is_staff:
            return BookBorrow.objects.raw(
                'SELECT * FROM book_borrow'
            )
        else:
            # returns empty queryset
            return BookBorrow.objects.none()

class BookBorrowDetailAPIView(RetrieveAPIView):
    queryset = BookBorrow.objects.all()
    serializer_class = BookBorrowReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'bbid'

class BookBorrowCreateAPIView(CreateAPIView):
    queryset = BookBorrow.objects.all()
    serializer_class = BookBorrowCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderUserPermission]

class BookBorrowDeleteAPIView(DestroyAPIView):
    queryset = BookBorrow.objects.all()
    lookup_field = 'bbid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsBookLenderPermission]

