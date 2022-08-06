from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import LibraryStock
from .serializers import LibraryStockReadSerializer, LibraryStockWriteSerializer
from .permissions import IsLibraryStockOwnerPermission

class LibraryStockListAPIView(ListAPIView):
    queryset = LibraryStock.objects.all()
    serializer_class = LibraryStockReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class MyLibraryStockListAPIView(ListAPIView):
    serializer_class = LibraryStockReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryStockOwnerPermission]
    
    def get_queryset(self):
        return self.queryset.filter(library=self.request.user.library)

class LibraryStockDetailAPIView(RetrieveAPIView):
    queryset = LibraryStock.objects.all()
    serializer_class = LibraryStockReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'lsid'

class LibraryStockCreateAPIView(CreateAPIView):
    queryset = LibraryStock.objects.all()
    serializer_class = LibraryStockWriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class LibraryStockUpdateAPIView(UpdateAPIView):
    queryset = LibraryStock.objects.all()
    serializer_class = LibraryStockWriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryStockOwnerPermission]
    lookup_field = 'lsid'

class LibraryStockDeleteAPIView(DestroyAPIView):
    queryset = LibraryStock.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryStockOwnerPermission]
    lookup_field = 'lsid'
