from rest_framework import serializers

from .models import Notification

class NotificationReadSerializer(serializers.ModelSerializer):
    notification_to = serializers.SerializerMethodField()
    notification_from = serializers.SerializerMethodField()
    class Meta:
        model = Notification
        fields = ['nid', 'created_at', 'notification_to', 'notification_from', 'event_id', 'content_id']
        read_only_fields = ('__all__',)
    
    def get_notification_to(self, obj):
        if obj.notification_to.groups.filter(name='reader').exists():
            return {'rid': obj.notification_to.reader.rid}
        elif obj.notification_to.groups.filter(name='library').exists():
            return {'lid': obj.notification_to.library.lid}
    
    def get_notification_from(self, obj):
        if obj.notification_from.groups.filter(name='reader').exists():
            return {'rid': obj.notification_from.reader.rid}
        elif obj.notification_from.groups.filter(name='library').exists():
            return {'lid': obj.notification_from.library.lid}