from rest_framework import serializers

from reader.models import Reader
from .models import Friend

class FriendReadSerializer(serializers.ModelSerializer):
    friendship_from = serializers.SerializerMethodField()
    friendship_to = serializers.SerializerMethodField()
    class Meta:
        model = Friend 
        fields = ['fid','friendship_from', 'friendship_to', 'created_at', 'is_pending']
        read_only_fields = ('__all__',)
    
    def get_friendship_from(self, obj):
        return {'rid': obj.friendship_from.rid}
    
    def get_friendship_to(self, obj):
        return {'rid': obj.friendship_to.rid}

class FriendCreateSerializer(serializers.ModelSerializer):
    friendship_from = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all())
    friendship_to = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all())
    class Meta:
        model = Friend
        fields = ['fid', 'friendship_from', 'friendship_to','is_pending']
        read_only_fields = ('fid','is_pending',)
        extra_kwargs = {
            'friendship_from': {'required': True},
            'friendship_to': {'required': True},
        }
    
    def validate_friendship_from(self, value):
        if value.rid != self.context['request'].user.reader.rid:
            raise serializers.ValidationError('friendship_from must be the same as the request user')
        return value
    
    def create(self, validated_data):
        return Friend.objects.create(**validated_data)

class FriendUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['fid', 'friendship_from', 'friendship_to', 'is_pending']
        read_only_fields = ('fid','friendship_from', 'friendship_to',)
        extra_kwargs = {
            'is_pending': {'required': True}
        }

    def update(self, instance, validated_data):
        instance.is_pending = validated_data.get('is_pending', instance.is_pending)
        instance.save()
        return instance