from rest_framework import serializers

from .models import Reads
from book.models import Book
from reader.models import Reader

class ReadsReadSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    reader = serializers.StringRelatedField()
    class Meta:
        model = Reads
        fields = ['rsid','reader', 'book', 'created_at', 'updated_at', 'status']
        read_only_fields = ('__all__',)



class ReadsWriteSerializer(serializers.ModelSerializer):
    reader = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    class Meta:
        model = Reads
        fields = ['rsid','reader', 'book', 'status']
        read_only_fields = ('rsid',) 

    def create(self, validated_data):
        return Reads.objects.create(**validated_data)

class ReadsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reads
        fields = ['rsid','reader', 'book', 'status']
        read_only_fields = ('rsid','reader', 'book',) 

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance