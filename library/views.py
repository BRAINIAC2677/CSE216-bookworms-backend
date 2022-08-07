from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication

# Create your views here.
from .models import Library 
from .serializers import LibraryReadSerializer, LibraryWriteSerializer
from .permissions import IsLibraryAccountOwnerPermission

class LibraryRegisterAPIView(CreateAPIView):
    serializer_class = LibraryWriteSerializer
    permission_classes = [AllowAny]

class LibraryListAPIView(ListAPIView):
    queryset = Library.objects.all()
    serializer_class = LibraryReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class LibraryDetailAPIView(RetrieveAPIView):
    queryset = Library.objects.all()
    serializer_class = LibraryReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'lid'

class MyLibraryDetailAPIView(RetrieveAPIView):
    queryset = Library.objects.all()
    serializer_class = LibraryReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryAccountOwnerPermission]

    def get_object(self):
        return self.request.user.library

class LibraryUpdateAPIView(UpdateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibraryWriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryAccountOwnerPermission]

    def get_object(self):
        return self.request.user.library

class LibraryDeleteAPIView(DestroyAPIView):
    queryset = Library.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryAccountOwnerPermission]

    def get_object(self):
        return self.request.user.library
    
    def perform_destroy(self, instance): 
        instance.user.delete()
        return super().perform_destroy(instance)
