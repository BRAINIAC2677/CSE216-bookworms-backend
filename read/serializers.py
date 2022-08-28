from rest_framework import serializers

from .models import Read
from book.models import Book
from reader.models import Reader

class ReadsReadSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()
    reader = serializers.SerializerMethodField()
    class Meta:
        model = Read
        fields = ['rsid','reader', 'book', 'created_at', 'updated_at', 'status']
        read_only_fields = ('__all__',)
    
    def get_book(self, obj):
        return {'bid': obj.book.bid}

    def get_reader(self, obj):
        return {'rid': obj.reader.rid}

class ReadsCreateSerializer(serializers.ModelSerializer):
    reader = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all(), required = True)
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), required = True)
    class Meta:
        model = Read
        fields = ['rsid','reader', 'book', 'status']
        read_only_fields = ('rsid',) 
        extra_kwargs = {
            'status': {
                'required': True,
            },
        }

    def create(self, validated_data):
        return Read.objects.create(**validated_data)

class ReadsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Read
        fields = ['rsid','reader', 'book', 'status']
        read_only_fields = ('rsid','reader', 'book',) 

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance