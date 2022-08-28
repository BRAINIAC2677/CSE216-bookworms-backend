from rest_framework import serializers

from reader.models import Reader
from bookreview.models import BookReview
from .models import Comment

class CommentReadSerializer(serializers.ModelSerializer):
    commented_by = serializers.SerializerMethodField()
    commented_on = serializers.SerializerMethodField()
    love_react_count = serializers.SerializerMethodField()
    loved_by = serializers.SerializerMethodField()
    class Meta:
        model = Comment
        fields = ('cid', 'commented_by', 'commented_on', 'created_at', 'updated_at', 'love_react_count', 'loved_by')
        read_only_fields = ('__all__',)
    
    def get_commented_by(self, obj):
        return {'rid': obj.commented_by.rid}
    
    def get_commented_on(self, obj):
        return {'brid': obj.commented_on.brid}
    
    def get_love_react_count(self, obj):
        return obj.loved_by.count()
    
    def get_loved_by(self, obj):
        return {'rid': r.rid for r in obj.loved_by.all()}
    
class CommentCreateSerializer(serializers.ModelSerializer):
    commented_by = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all(), required = True)
    commented_on = serializers.PrimaryKeyRelatedField(queryset=BookReview.objects.all(), required = True)
    class Meta:
        model = Comment
        fields = ('cid', 'commented_by', 'commented_on', 'content')
        read_only_fileds = ('cid',)
        extra_kwargs = {
            'content': {'required': True},
        }
    
    def validate(self, attrs):
        if attrs['content'] == '':
            raise serializers.ValidationError("Content cannot be empty")
        return super().validate(attrs)
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content',)    
    
    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance

class CommentLoveUpdateSerializer(serializers.ModelSerializer):
    loved_by = serializers.PrimaryKeyRelatedField(queryset=Reader.objects.all(), required = True, many=True)
    class Meta:
        model = Comment
        fields = ('loved_by',)
    
    def validate(self, attrs):
        if len(attrs['loved_by']) != 1:
            raise serializers.ValidationError("Only one reader can love a comment at a time")
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        if instance.loved_by.filter(rid=validated_data['loved_by'][0].rid).exists():
            instance.loved_by.remove(validated_data['loved_by'][0])
        else:
            instance.loved_by.add(validated_data['loved_by'][0])
        return instance