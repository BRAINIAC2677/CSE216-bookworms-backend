from django.db import connection

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Book
from genre.models import Genre
from reader.models import Reader

class BookReadSerializer(serializers.ModelSerializer):
    genres = serializers.SerializerMethodField()
    authors = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = ['bid', 'title', 'description', 'photo_url', 'page_count', 'created_at', 'updated_at','genres', 'authors', 'avg_rating']
        read_only_fields = ('__all__',)
    
    def get_genres(self, obj):
        return [{genre.gid, genre.name} for genre in obj.genres.all()]
    
    def get_authors(self, obj):
        return [{author.user.get_full_name(), author.rid} for author in obj.authors.all()]

    def get_avg_rating(self, obj):
        with connection.cursor() as cursor:
            cursor.execute("SELECT AVG(rating) avg_rating FROM book_review WHERE book_id = %s", [obj.bid])
            row = cursor.fetchone()
        return row[0]

    


class BookCreateUpdateSerializer(serializers.ModelSerializer):
    bid = serializers.CharField(max_length=13,required=True, validators=[UniqueValidator(queryset=Book.objects.all())])
    genres = serializers.PrimaryKeyRelatedField(many = True, required=True, queryset = Genre.objects.all())
    authors = serializers.PrimaryKeyRelatedField(many = True, required=True, queryset = Reader.objects.all())

    class Meta:
        model = Book 
        fields = ['bid','title', 'description','photo_url','page_count', 'genres', 'authors']
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
    
    def validate_page_count(self, value):
        if value < 0:
            raise serializers.ValidationError("Page count must be greater than 0")
        return value
    
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
        instance.bid = validated_data.get('bid', instance.bid)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.photo_url = validated_data.get('photo_url', instance.photo_url)
        instance.page_count = validated_data.get('page_count', instance.page_count)
        instance.save()
        return instance
