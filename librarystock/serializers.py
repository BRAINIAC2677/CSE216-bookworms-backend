from rest_framework import serializers

from book.models import Book
from library.models import Library
from .models import LibraryStock

class LibraryStockReadSerializer(serializers.ModelSerializer):
    book = serializers.StringRelatedField()
    library = serializers.StringRelatedField()
    class Meta:
        model = LibraryStock
        fields = ['lsid', 'book', 'library', 'quantity', 'borrow_fee_per_day']
        read_only_fields = ('__all__',)

class LibraryStockCreateSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all())
    library = serializers.PrimaryKeyRelatedField(queryset=Library.objects.all())

    class Meta:
        model = LibraryStock
        fields = ['lsid', 'book','library', 'quantity', 'borrow_fee_per_day']
        read_only_fields = ('lsid',)
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

        def validate_quantity(self, value):
            if value < 0:
                raise serializers.ValidationError("Quantity cannot be negative")
            return value

        def create(self, validated_data):
            return LibraryStock.objects.create(**validated_data)

class LibraryStockUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibraryStock
        fields = ['lsid','book', 'library', 'quantity', 'borrow_fee_per_day']
        read_only_fields = ('lsid','book', 'library',)

        def validate_quantity(self, value):
            if value < 0:
                raise serializers.ValidationError("Quantity cannot be negative")
            return value

        def update(self, instance, validated_data):
            instance.quantity = validated_data.get('quantity', instance.quantity)
            instance.borrow_fee_per_day = validated_data.get('borrow_fee_per_day', instance.borrow_fee_per_day)
            instance.save()
            return instance