from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Book
from genre.models import Genre
from reader.models import Reader

class BookReadSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['isbn', 'title', 'description', 'photo_url', 'page_count', 'created_at', 'updated_at', 'genres', 'authors']
        read_only_fields = ('__all__',)
    
    def get_genres(self, obj):
        return [{genre.gid, genre.name} for genre in obj.genres.all()]
    
    def get_authors(self, obj):
        return [{author.user.get_full_name(), author.rid} for author in obj.authors.all()]
    


class BookWriteSerializer(serializers.ModelSerializer):
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
    
    def create(self, validated_data):
        book_genres = validated_data.pop('genres')
        book_authors = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)
        book.genres.set(book_genres)
        book.authors.set(book_authors)
        book.save()
        return book
    
    def update(self, instance, validated_data):
        if validated_data.get('genres'):
            book_genres = validated_data.pop('genres')
            instance.genres.set(book_genres)
        if validated_data.get('authors'):
            book_authors = validated_data.pop('authors')
            instance.authors.set(book_authors)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.photo_url = validated_data.get('photo_url', instance.photo_url)
        instance.page_count = validated_data.get('page_count', instance.page_count)
        instance.save()
        return instance
