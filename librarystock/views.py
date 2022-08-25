from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import LibraryStock
from .serializers import LibraryStockReadSerializer, LibraryStockWriteSerializer, LibraryStockUpdateSerializer
from .permissions import IsLibraryStockOwnerPermission

class LibraryStockListAPIView(ListAPIView):
    queryset = LibraryStock.objects.all()
    serializer_class = LibraryStockReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

#todo: only library user can access this view
class MyLibraryStockListAPIView(ListAPIView):
    serializer_class = LibraryStockReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryStockOwnerPermission]
    
    def get_queryset(self):
        return LibraryStock.objects.all().filter(library=self.request.user.library)

class LibraryStockDetailAPIView(RetrieveAPIView):
    queryset = LibraryStock.objects.all()
    serializer_class = LibraryStockReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'lsid'

#todo: permit only library account to create library stock
class LibraryStockCreateAPIView(CreateAPIView):
    queryset = LibraryStock.objects.all()
    serializer_class = LibraryStockWriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class LibraryStockUpdateAPIView(UpdateAPIView):
    queryset = LibraryStock.objects.all()
    serializer_class = LibraryStockUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryStockOwnerPermission]
    lookup_field = 'lsid'

class LibraryStockDeleteAPIView(DestroyAPIView):
    queryset = LibraryStock.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryStockOwnerPermission]
    lookup_field = 'lsid'
