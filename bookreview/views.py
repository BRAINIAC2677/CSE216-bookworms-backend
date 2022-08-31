from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import BookReview 
from .serializers import BookReviewReadSerializer, BookReviewCreateSerializer, BookReviewLoveUpdateSerializer, BookReviewUpdateSerializer
from .permissions import IsBookReviewerPermission

class BookReviewListAPIView(ListAPIView):
    serializer_class = BookReviewReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        bid = self.request.query_params.get('bid', None)
        rid = self.request.query_params.get('rid', None)

        if bid and rid is None:
            return BookReview.objects.raw(
                'SELECT * FROM book_review WHERE book_id = %s',
                [bid]
            )
        elif rid and bid is None:
            return BookReview.objects.raw(
                'SELECT * FROM get_book_reviews_r(%s)',
                [rid]
            )
        else:
            return BookReview.objects.raw('SELECT * FROM get_book_reviews()')

class BookReviewDetailAPIView(RetrieveAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'brid'

class BookReviewCreateAPIView(CreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class BookReviewUpdateAPIView(UpdateAPIView):
    queryset = BookReview.objects.all()
    lookup_field = 'brid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsBookReviewerPermission]
    serializer_class = BookReviewUpdateSerializer

class BookReviewUpdateLovedByAPIView(UpdateAPIView):
    queryset = BookReview.objects.all()
    lookup_field = 'brid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewLoveUpdateSerializer

class BookReviewDeleteAPIView(DestroyAPIView):
    queryset = BookReview.objects.all()
    lookup_field = 'brid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsBookReviewerPermission]

