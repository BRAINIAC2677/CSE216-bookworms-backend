from rest_framework import serializers

from book.models import Book
from reader.models import Reader
from .models import BookReview

class BookReviewReadSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField()
    book = serializers.StringRelatedField()
    love_react_count = serializers.SerializerMethodField()
    class Meta:
        model = BookReview
        fields = ['brid', 'book', 'reviewer', 'rating', 'content', 'created_at', 'updated_at', 'love_react_count']
        read_only_fields = ('__all__',)   

    def get_love_react_count(self, obj):
        return obj.loved_by.count()

class BookReviewWriteSerializer(serializers.Serializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), allow_null = False)
    reviewer = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all(), allow_null = False)
    class Meta:
        model = BookReview 
        fields = ['book', 'reviewer', 'rating', 'content']
        write_only_fields = '__all__'
        extra_kwargs = {
            'content': {'required': True},
            'rating': {'required': True},
        }
    
    def validate(self, attrs):
        if attrs['rating'] < 0 or attrs['rating'] > 5:
            raise serializers.ValidationError("Rating must be between 0 and 5")
        return super().validate(attrs)

class BookReviewLoveSerializer(serializers.Serializer):
    brid = serializers.PrimaryKeyRelatedField(queryset=BookReview.objects.all(), allow_null = False)
    reader = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all(), allow_null = False)
    class Meta:
        model = BookReview 
        fields = ['brid', 'reader']
        write_only_fields = '__all__'
        extra_kwargs = {
            'brid': {'required': True},
            'reader': {'required': True},
        }
    
    def validate(self, attrs):
        if attrs['brid'].loved_by.filter(pk=attrs['reader'].pk).exists():
            raise serializers.ValidationError("You already love this review")
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        instance.loved_by.add(validated_data['reader'])
        instance.save()
        return instance