from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .models import Reader
from .serializers import ReaderSerializer
from .permissions import IsReaderAccountOwnerPermission


class ReaderRegisterAPIView(CreateAPIView):
    serializer_class = ReaderSerializer
    permission_classes = [AllowAny]


class ReaderListView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderDetailView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderAccountOwnerPermission]
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

    def get_object(self):
        return self.request.user.reader


class ReaderUpdateView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderAccountOwnerPermission]
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

    def get_object(self):
        return self.request.user.reader


class ReaderDeleteView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderAccountOwnerPermission]
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

    def get_object(self):
        return self.request.user.reader
