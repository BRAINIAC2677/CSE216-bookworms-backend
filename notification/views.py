from rest_framework.generics import ListAPIView 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Notification
from .serializers import NotificationReadSerializer

class NotificationListAPIView(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NotificationReadSerializer

    def get_queryset(self):
        return Notification.objects.raw(
            'SELECT * FROM notification WHERE notification_to_id = %s',
            [self.request.user.id]
        ) 