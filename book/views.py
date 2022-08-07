from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Book
from .serializers import BookReadSerializer, BookWriteSerializer

class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookReadSerializer

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
