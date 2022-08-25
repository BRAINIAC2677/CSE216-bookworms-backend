from rest_framework import serializers

from .models import Genre 

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre 
        fields = ['gid', 'name']
        read_only_fields = ('gid',)
        extra_kwargs = {
            'name': {
                'required': True,
            }
        }
    
    def create(self, validated_data):
        return Genre.objects.create(**validated_data)
