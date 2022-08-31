from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from .models import Reader
from .serializers import ReaderReadSerializer, ReaderCreateSerializer, ReaderUpdateSerializer, AdminReaderCreateSerializer
from .permissions import IsReaderAccountOwnerPermission, IsReaderUserPermission, HasReaderDeletePermission


class ReaderRegisterAPIView(CreateAPIView):
    serializer_class = ReaderCreateSerializer
    permission_classes = [AllowAny]

class AdminReaderRegisterAPIView(CreateAPIView):
    serializer_class = AdminReaderCreateSerializer
    permission_classes = [AllowAny]

class ReaderListAPIView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class MyReaderDetailAPIView(RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderAccountOwnerPermission]
    queryset = Reader.objects.all()
    serializer_class = ReaderReadSerializer

    def get_object(self):
        return self.request.user.reader

class ReaderDetailAPIView(RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'rid'

class ReaderUpdateAPIView(UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsReaderUserPermission]
    queryset = Reader.objects.all()
    serializer_class = ReaderUpdateSerializer

    def get_object(self):
        return self.request.user.reader

class ReaderDeleteAPIView(DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, HasReaderDeletePermission]
    queryset = Reader.objects.all()
    lookup_field = 'rid'

    def perform_destroy(self, instance):
        instance.user.delete()
        return super().perform_destroy(instance)


# overriding ObtainAuthToken 
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView


class ObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="username",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Username",
                        description="Valid username for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        if user.groups.filter(name='library').exists():        
            response_data = {
                'token': token.key,
                'is_staff': user.is_staff,
                'acc_type': 'library',
            }
        elif user.groups.filter(name='reader').exists():
            response_data = {
                'token': token.key,
                'is_staff': user.is_staff,
                'acc_type': 'reader',
            }
        return Response(response_data)


obtain_auth_token = ObtainAuthToken.as_view()

