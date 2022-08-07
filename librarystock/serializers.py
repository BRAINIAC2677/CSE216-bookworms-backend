from rest_framework import serializers

from book.models import Book
from library.models import Library
from .models import LibraryStock

class LibraryStockReadSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    library = serializers.StringRelatedField()
    class Meta:
        model = LibraryStock
        fields = ['book', 'library', 'quantity', 'borrow_fee_per_day']
        read_only_fields = '__all__'

class LibraryStockWriteSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    library = serializers.PrimaryKeyRelatedField(queryset=Library.objects.all())

    class Meta:
        model = LibraryStock
        fields = ['book', 'library', 'quantity', 'borrow_fee_per_day']
        write_only_fields = '__all__'
        extra_kwargs = {
            'borrow_fee_per_day': {
                'required': True,
            },
            'quantity': {
                'required': True,
            },
            'book': {
                'required': True,
            },
            'library': {
                'required': True,
            },
        }

        def validate(self, attrs):
            if attrs['quantity'] < 0:
                raise serializers.ValidationError("Quantity cannot be negative")
            if attrs['borrow_fee_per_day'] < 0:
                raise serializers.ValidationError("Borrow fee cannot be negative")
            if LibraryStock.objects.filter(library=attrs['library'], book=attrs['book']).exists():
                raise serializers.ValidationError("Library stock with same library and book already exists")
            return attrs
