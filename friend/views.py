from django.db.models import Q

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Friend
from .serializers import FriendReadSerializer, FriendCreateSerializer, FriendUpdateSerializer
from .permissions import IsFriendshipOwnerPermission
from reader.permissions import IsReaderUserPermission

class FriendListAPIView(ListAPIView):
    serializer_class = FriendReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        rid = self.request.query_params.get('rid', None)
        if rid:
            return Friend.objects.raw(
                'SELECT * FROM friend WHERE (is_pending = false) AND (friendship_from_id = %s OR friendship_to_id = %s)',
                [rid, rid]
            )
        elif self.request.user.is_staff:
            return Friend.objects.raw('SELECT * FROM friend')
        else:
            return Friend.objects.none()

class PendingFriendListAPIView(ListAPIView):
    serializer_class = FriendReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsFriendshipOwnerPermission]

    def get_queryset(self):
        return Friend.objects.raw('SELECT * FROM friend WHERE is_pending')

class FriendCreateAPIView(CreateAPIView):
    serializer_class = FriendCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderUserPermission]

class FriendUpdateAPIView(UpdateAPIView):
    queryset = Friend.objects.all()
    serializer_class = FriendUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsFriendshipOwnerPermission]
    lookup_field = 'fid'

class FriendDeleteAPIView(DestroyAPIView):
    queryset = Friend.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsFriendshipOwnerPermission]
    lookup_field = 'fid'

    
