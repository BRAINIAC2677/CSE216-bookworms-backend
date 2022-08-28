from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Read
from .serializers import ReadsReadSerializer, ReadsCreateSerializer, ReadsUpdateSerializer
from reader.permissions import IsReaderUserPermission
from .permissions import IsReadsOwnerPermission
# Create your views here.

class ReadsListAPIView(ListAPIView):
    serializer_class = ReadsReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        rid = self.request.query_params.get('rid')
        if rid:
            return Read.objects.raw(
                'SELECT * FROM read R WHERE R.reader_id = %s',
                [rid]
            )
        return Read.objects.all()

class ReadsDetailAPIView(RetrieveAPIView):
    queryset = Read.objects.all()
    serializer_class = ReadsReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'rsid'

class ReadsCreateAPIView(CreateAPIView):
    queryset = Read.objects.all()
    serializer_class = ReadsCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderUserPermission]

class ReadsUpdateAPIView(UpdateAPIView):
    queryset = Read.objects.all()
    serializer_class = ReadsUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderUserPermission, IsReadsOwnerPermission]
    lookup_field = 'rsid'

class ReadsDeleteAPIView(DestroyAPIView):
    queryset = Read.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderUserPermission, IsReadsOwnerPermission]
    lookup_field = 'rsid'
