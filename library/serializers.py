from django.contrib.auth.models import User 

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Library

class LibraryUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User 
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
            },
            'username': {
                'required': True,
            },
        }

class LibraryWriteSerializer(serializers.ModelSerializer):
    user = LibraryUserSerializer(required=True)

    class Meta:
        model = Library
        fields = ['user', 'library_name', 'photo_url', 'longitude', 'latitude']
        write_only_fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data.get('password'))
        user.groups.add('library')
        user.save()
        library = Library.objects.create(user=user, **validated_data)
        return library

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.set_password(user_data.get('password', user.password))
        user.save()
        instance.library_name = validated_data.get('library_name', instance.library_name)
        instance.photo_url = validated_data.get('photo_url', instance.photo_url)
        instance.longitude = validated_data.get('longitude', instance.longitude)
        instance.latitude = validated_data.get('latitude', instance.latitude)
        instance.save()
        return instance

class LibraryReadSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Library
        fields = ['user', 'library_name', 'photo_url', 'longitude', 'latitude']
        read_only_fields = '__all__'

    def get_user(self, obj):
        return {'username': obj.user.username, 'email': obj.user.email}
