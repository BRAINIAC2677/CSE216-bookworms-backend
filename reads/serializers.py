from rest_framework import serializers

from .models import Reads
from book.models import Book
from reader.models import Reader

class ReadsReadSerializer(serializers.Serializer):
    book = serializers.StringRelatedField()
    reader = serializers.StringRelatedField()
    class Meta:
        model = Reads
        fields = ['rid','reader', 'book', 'created_at', 'updated_at', 'status']
        read_only_fields = ('__all__',)



class ReadsWriteSerializer(serializers.Serializer):
    reader = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all())
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    class Meta:
        model = Reads
        fields = ['reader', 'book', 'status']
        write_only_fields = '__all__'
    
    def validate(self, attrs):
        req_reader = self.context['request'].user.reader
        reader = attrs['reader']
        if req_reader != reader:
            raise serializers.ValidationError("You are not the owner of this reads.")
        return super().validate(attrs)
