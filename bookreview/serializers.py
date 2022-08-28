from rest_framework import serializers

from book.models import Book
from reader.models import Reader
from .models import BookReview

class BookReviewReadSerializer(serializers.ModelSerializer):
    reviewer = serializers.SerializerMethodField()
    book = serializers.SerializerMethodField()
    love_react_count = serializers.SerializerMethodField()
    loved_by = serializers.SerializerMethodField()
    class Meta:
        model = BookReview
        fields = ['brid', 'book', 'reviewer', 'rating', 'content', 'created_at', 'updated_at', 'love_react_count', 'loved_by']
        read_only_fields = ('__all__',)   

    def get_reviewer(self, obj):
        return {'rid': obj.reviewer.rid}
    def get_book(self, obj):
        return {'bid': obj.book.bid}
    def get_love_react_count(self, obj):
        return obj.loved_by.count()
    def get_loved_by(self, obj):
        return [{'rid': r.rid} for r in obj.loved_by.all()]


class BookReviewCreateSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), required = True)
    reviewer = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all(), required = True)
    class Meta:
        model = BookReview 
        fields = ['brid', 'book', 'reviewer', 'rating', 'content']
        read_only_fileds = ('brid',)
        extra_kwargs = {
            'content': {'required': True},
            'rating': {'required': True},
        }
    
    def validate(self, attrs):
        if attrs['rating'] < 0 or attrs['rating'] > 5:
            raise serializers.ValidationError("Rating must be between 0 and 5")
        return super().validate(attrs)
    
    def create(self, validated_data):
        return BookReview.objects.create(**validated_data)
    
class BookReviewUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookReview 
        fields = ['rating', 'content']
    
    def validate(self, attrs):
        if attrs.get('rating'):
            if attrs['rating'] < 0 or attrs['rating'] > 5:
                raise serializers.ValidationError("Rating must be between 0 and 5")
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating', instance.rating)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
   
class BookReviewLoveUpdateSerializer(serializers.ModelSerializer):
    loved_by = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all(), many = True, required = True)
    class Meta:
        model = BookReview 
        fields = ['loved_by']
    
    def validate(self, attrs):
        if len(attrs['loved_by']) != 1:
            raise serializers.ValidationError("Only one reader can love a review at a time")
        return super().validate(attrs)

    def update(self, instance, validated_data):
        if instance.loved_by.filter(pk=validated_data['loved_by'][0].pk).exists():
            instance.loved_by.remove(validated_data['loved_by'][0])
        else:
            instance.loved_by.add(validated_data['loved_by'][0])
        return instance
    
