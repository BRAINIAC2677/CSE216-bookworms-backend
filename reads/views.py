from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Reads
from .serializers import ReadsReadSerializer, ReadsWriteSerializer, ReadsUpdateSerializer
from .permissions import IsReadsOwnerPermission
# Create your views here.

class ReadsListAPIView(ListAPIView):
    queryset = Reads.objects.all()
    serializer_class = ReadsReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ReadsDetailAPIView(RetrieveAPIView):
    queryset = Reads.objects.all()
    serializer_class = ReadsReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'rsid'

class ReadsCreateAPIView(CreateAPIView):
    queryset = Reads.objects.all()
    serializer_class = ReadsWriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ReadsUpdateAPIView(UpdateAPIView):
    queryset = Reads.objects.all()
    serializer_class = ReadsUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReadsOwnerPermission]
    lookup_field = 'rsid'

class ReadsDeleteAPIView(DestroyAPIView):
    queryset = Reads.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReadsOwnerPermission]
    lookup_field = 'rsid'
