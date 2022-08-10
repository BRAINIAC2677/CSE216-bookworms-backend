from rest_framework import serializers

from .models import BookBorrow
from book.models import Book 
from library.models import Library
from reader.models import Reader

class BookBorrowReadSerializer(serializers.Serializer):
    book = serializers.StringRelatedField()
    borrowed_by = serializers.StringRelatedField()
    borrowed_from = serializers.StringRelatedField()
    class Meta:
        model = BookBorrow 
        fields = ['bbid','book', 'borrowed_from','borrowed_by', 'borrowed_date', 'returned_date', 'fee']
        read_only_fields = ('__all__',)


class BookBorrowWriteSerializer(serializers.Serializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    borrowed_from = serializers.PrimaryKeyRelatedField(queryset=Library.objects.all())
    borrowed_by = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all())
    class Meta:
        model = BookBorrow
        fields = ['book', 'borrowed_from','borrowed_by', 'returned_date', 'fee']
        write_only_fields = '__all__'
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