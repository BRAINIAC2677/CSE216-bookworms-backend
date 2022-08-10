from rest_framework import serializers

from reader.models import Reader
from .models import Friend

class FriendReadSerializer(serializers.Serializer):
    friendship_from = serializers.StringRelatedField()
    friendship_to = serializers.StringRelatedField()
    class Meta:
        model = Friend 
        fields = ['friendship_from', 'friendship_to', 'created_at', 'is_pending']
        read_only_fields = ('__all__',)

class FriendWriteSerializer(serializers.Serializer):
    friendship_from = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all())
    friendship_to = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all())
    class Meta:
        model = Friend
        fields = ['friendship_from', 'friendship_to','is_pending']
        write_only_fields = '__all__'
        extra_kwargs = {
            'friendship_from': {'required': True},
            'friendship_to': {'required': True},
            'is_pending': {'required': True}
        }