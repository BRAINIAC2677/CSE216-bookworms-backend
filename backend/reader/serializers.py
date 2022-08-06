from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Reader

class ReaderUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    class Meta:
        model = User
        fields = ['username', 'password',
                  'email', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
            },
            'first_name': {
                'required': True,
            },
            'last_name': {
                'required': True,
            },
            'username': {
                'required': True,
            },
        }


class ReaderSerializer(serializers.ModelSerializer):
    user = ReaderUserSerializer(required=True)

    class Meta:
        model = Reader
        fields = ['user', 'photo_url', 'bio']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data.get('password'))
        user.groups.add('reader')
        user.save()
        reader = Reader.objects.create(user=user, **validated_data)
        return reader

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.set_password(user_data.get('password', user.password))
        user.save()
        instance.photo_url = validated_data.get(
            'photo_url', instance.photo_url)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance
