from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Book
from genre.models import Genre
from reader.models import Reader

class BookReadSerializer(serializers.ModelSerializer):
    genres = serializers.StringRelatedField(many=True, read_only = True)
    authors = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['isbn', 'title', 'description', 'photo_url', 'page_count', 'created_at', 'updated_at', 'genres', 'authors']
        read_only_fields = '__all__'
    
    def get_authors(self, obj):
        return [{author.user.get_full_name(), author.rid} for author in obj.authors.all()]


class BookWriteSerializer(serializers.Serializer):
    isbn = serializers.CharField(max_length=13,required=True, validators=[UniqueValidator(queryset=Book.objects.all())])
    genres = serializers.PrimaryKeyRelatedField(many = True, queryset = Genre.objects.all())
    authors = serializers.PrimaryKeyRelatedField(many = True, queryset = Reader.objects.all())

    class Meta:
        model = Book 
        fields = ['isbn','title', 'description','photo_url','page_count', 'genres', 'authors']
        write_only_fields = '__all__'
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

