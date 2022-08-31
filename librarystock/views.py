from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import LibraryStock
from .serializers import LibraryStockReadSerializer, LibraryStockCreateSerializer, LibraryStockUpdateSerializer
from library.permissions import IsLibraryUserPermission
from .permissions import IsLibraryStockOwnerPermission

class LibraryStockListAPIView(ListAPIView):
    serializer_class = LibraryStockReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        lid = self.request.query_params.get('lid', None)
        if lid:
            return LibraryStock.objects.raw(
                'SELECT * FROM get_library_stocks_l(%s)',
                [lid]
            )
        else:
            return LibraryStock.objects.raw('SELECT * FROM get_library_stocks()')

class LibraryStockDetailAPIView(RetrieveAPIView):
    queryset = LibraryStock.objects.all()
    serializer_class = LibraryStockReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'lsid'

class LibraryStockCreateAPIView(CreateAPIView):
    queryset = LibraryStock.objects.all()
    serializer_class = LibraryStockCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsLibraryUserPermission]

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
