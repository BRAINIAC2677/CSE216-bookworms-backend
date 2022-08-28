import datetime 
from rest_framework import serializers

from .models import BookBorrow
from book.models import Book 
from library.models import Library
from reader.models import Reader

class BookBorrowReadSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()
    borrowed_by = serializers.SerializerMethodField()
    borrowed_from = serializers.SerializerMethodField()
    class Meta:
        model = BookBorrow 
        fields = ['bbid','book', 'borrowed_from','borrowed_by', 'borrowed_date', 'returned_date', 'fee']
        read_only_fields = ('__all__',)
    
    def get_book(self, obj):
        return {'bid': obj.book.bid}

    def get_borrowed_by(self, obj):
        return {'rid': obj.borrowed_by.rid}
    
    def get_borrowed_from(self, obj):
        return {'lid': obj.borrowed_from.lid}

class BookBorrowCreateSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    borrowed_from = serializers.PrimaryKeyRelatedField(queryset=Library.objects.all())
    borrowed_by = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all())
    class Meta:
        model = BookBorrow
        fields = ['bbid', 'book', 'borrowed_from','borrowed_by', 'returned_date', 'fee']
        read_only_fields = ('bbid',)
        extra_kwargs = {
            'book':{
                'required':True,
            },
            'borrowed_from':{
                'required':True,
            },
            'borrowed_by':{
                'required':True,
            },
            'returned_date':{
                'required':True,
            },
            'fee':{
                'required':True,
            },
        }

    def validate_returned_date(self, value):
        #check if value is a datetime value
        if not isinstance(value, datetime.datetime):
            raise serializers.ValidationError('Returned date must be a datetime value')

    def create(self, validated_data):
        return BookBorrow.objects.create(**validated_data)