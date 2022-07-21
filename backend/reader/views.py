from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .models import Reader
from .serializers import ReaderSerializer, ReaderRegisterSerializer

class ReaderRegisterAPIView(CreateAPIView):
    serializer_class = ReaderRegisterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        username = serializer.validated_data['username']
        first_name = serializer.validated_data['first_name']
        last_name = serializer.validated_data['last_name']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = User(username=username, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        photo_url = serializer.validated_data['photo_url']
        bio = serializer.validated_data['bio']
        reader = Reader(user=user, photo_url=photo_url, bio=bio)
        reader.save()

class ReaderListView(ListAPIView):
    permission_classes = [IsAdminUser]

    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer

class ReaderDetailView(APIView):
    queryset = Reader.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        reader = self.get_reader()
        user = User.objects.get(pk=reader.user.id)
        all_data = {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'photo_url': reader.photo_url,
            'bio': reader.bio
        }
        return Response(all_data)
    
    def get_reader(self):
        return self.request.user.reader
   
class ReaderUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        reader = self.get_reader()
        if request.data.get('first_name'):
            reader.user.first_name = request.data.get('first_name')
        if request.data.get('last_name'):
            reader.user.last_name = request.data.get('last_name')
        if request.data.get('email'):
            reader.user.email = request.data.get('email')
        if request.data.get('password'):
            reader.user.set_password(request.data.get('password'))
        if request.data.get('photo_url'):
            reader.photo_url = request.data.get('photo_url')
        if request.data.get('bio'):
            reader.bio = request.data.get('bio')
        reader.user.save()
        reader.save()
        return Response({'message': 'Reader updated successfully'})

    def get_reader(self):
        return self.request.user.reader

class ReaderDeleteView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        reader = self.get_reader()
        user = User.objects.get(pk=reader.user.id)
        user.delete()
        reader.delete()
        return Response({'message': 'Reader deleted successfully'})

    def get_reader(self):
        return self.request.user.reader
