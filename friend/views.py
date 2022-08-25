from django.db.models import Q

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Friend
from .serializers import FriendReadSerializer, FriendWriteSerializer

# have to add custom permissions to the views
class FriendListAPIView(ListAPIView):
    serializer_class = FriendReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Friend.objects.filter(Q(friendship_from__exact=self.request.user) | Q(friendship_to__exact=self.request.user), Q(is_pending__exact=False))

class PendingFriendListAPIView(ListAPIView):
    serializer_class = FriendReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Friend.objects.filter(Q(friendship_from__exact=self.request.user) | Q(friendship_to__exact=self.request.user), Q(is_pending__exact=True))

class FriendCreateAPIView(CreateAPIView):
    serializer_class = FriendWriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(friendship_from=self.request.user)

class FriendUpdateAPIView(UpdateAPIView):
    serializer_class = FriendWriteSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'fid'

    def get_queryset(self):
        return Friend.objects.filter(Q(friendship_from__exact=self.request.user) | Q(friendship_to__exact=self.request.user), Q(is_pending__exact=False))

class FriendDeleteAPIView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'fid'

    def get_queryset(self):
        return Friend.objects.filter(Q(friendship_from__exact=self.request.user) | Q(friendship_to__exact=self.request.user))
    
