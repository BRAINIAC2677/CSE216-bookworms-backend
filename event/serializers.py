from rest_framework import serializers

from .models import Event

class EventReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['eid', 'name']
        read_only_fields = ('__all__',)