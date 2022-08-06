from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from .models import BookReview 
from .serializers import BookReviewReadSerializer, BookReviewWriteSerializer, BookReviewLoveSerializer
from .permissions import IsBookReviewerPermission

class BookReviewListAPIView(ListAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewReadSerializer

class BookReviewDetailAPIView(RetrieveAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewReadSerializer
    lookup_field = 'brid'

class BookReviewCreateAPIView(CreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewWriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class BookReviewUpdateAPIView(UpdateAPIView):
    queryset = BookReview.objects.all()
    lookup_field = 'brid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.user.reader == self.get_object().reviewer:
            return BookReviewWriteSerializer
        return BookReviewLoveSerializer

class BookReviewDeleteAPIView(DestroyAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewReadSerializer
    lookup_field = 'brid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsBookReviewerPermission]

