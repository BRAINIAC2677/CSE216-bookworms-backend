from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Book
from genre.models import Genre
from reader.models import Reader

class BookReadSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True, read_only = True)
    authors = serializers.StringRelatedField(many=True, read_only = True)
    class Meta:
        model = Book
        fields = ['isbn', 'title', 'description', 'photo_url', 'page_count', 'created_at', 'updated_at', 'genres', 'authors']


class BookWriteSerializer(serializers.Serializer):
    isbn = serializers.CharField(max_length=13,required=True, validators=[UniqueValidator(queryset=Book.objects.all())])
    genres = serializers.PrimaryKeyRelatedField(many = True, queryset = Genre.objects.all())
    authors = serializers.PrimaryKeyRelatedField(many = True, queryset = Reader.objects.all())

    class Meta:
        model = Book 
        fields = ['isbn','title', 'description','photo_url','page_count', 'genres', 'authors']
        extra_kwargs = {
            'title': {
                'required': True,
            },
            'photo_url': {
                'required': True,
            },
            'page_count': {
                'required': True,
            },
        }

