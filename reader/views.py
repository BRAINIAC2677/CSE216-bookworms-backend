from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .models import Reader
from .serializers import ReaderWriteSerializer, ReaderReadSerializer
from .permissions import IsReaderAccountOwnerPermission


class ReaderRegisterAPIView(CreateAPIView):
    serializer_class = ReaderWriteSerializer
    permission_classes = [AllowAny]


class ReaderListAPIView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class MyReaderDetailAPIView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reader.objects.all()
    serializer_class = ReaderReadSerializer

    def get_object(self):
        return self.request.user.reader

class ReaderDetailAPIView(RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'rid'

class ReaderUpdateAPIView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reader.objects.all()
    serializer_class = ReaderWriteSerializer

    def get_object(self):
        return self.request.user.reader


class ReaderDeleteAPIView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reader.objects.all()

    def get_object(self):
        return self.request.user.reader

    def perform_destroy(self, instance):
        instance.user.delete()
        return super().perform_destroy(instance)
