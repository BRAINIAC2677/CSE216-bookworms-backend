from django.contrib.auth.models import User
from django.contrib.auth.models import Group

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

class ReaderReadSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Reader
        fields = ['rid','user','bio', 'photo_url', 'reputation']
        read_only_fields = ('__all__',)

    def get_user(self, obj):
        return {'username': obj.user.username, 'first_name': obj.user.first_name,'last_name': obj.user.last_name, 'email': obj.user.email}

class ReaderCreateSerializer(serializers.ModelSerializer):
    user = ReaderUserSerializer(required=True)

    class Meta:
        model = Reader
        fields = ['rid','user', 'photo_url', 'bio', 'reputation']
        read_only_fields = ('rid','reputation',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data.get('password'))
        reader = Reader.objects.create(user=user, **validated_data)
        if not Group.objects.filter(name='reader').exists():
            Group.objects.create(name='reader')
        user.groups.add(Group.objects.get(name='reader'))
        user.save()
        return reader

class ReaderUpdateSerializer(serializers.ModelSerializer):
    user = ReaderUserSerializer()

    class Meta:
        model = Reader
        fields = ['rid','user', 'photo_url', 'bio', 'reputation']
        read_only_fields = ('rid',)

    def update(self, instance, validated_data):
        if validated_data.get('user'):
            user_data = validated_data.pop('user')
            user = instance.user
            user.username = user_data.get('username', user.username)
            user.email = user_data.get('email', user.email)
            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.set_password(user_data.get('password', user.password))
            user.save()
        instance.photo_url = validated_data.get('photo_url', instance.photo_url)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance

class AdminReaderCreateSerializer(serializers.ModelSerializer):
    user = ReaderUserSerializer(required=True)

    class Meta:
        model = Reader
        fields = ['rid','user', 'photo_url', 'bio', 'reputation']
        read_only_fields = ('rid',)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data.get('password'))
        user.is_staff = True
        reader = Reader.objects.create(user=user, **validated_data)
        if not Group.objects.filter(name='reader').exists():
            Group.objects.create(name='reader')
        user.groups.add(Group.objects.get(name='reader'))
        user.save()
        return reader
