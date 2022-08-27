from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Comment
from .permissions import IsCommentOwnerPermission
from .serializers import CommentReadSerializer, CommentCreateSerializer, CommentUpdateSerializer, CommentLoveUpdateSerializer

class CommentListAPIView(ListAPIView):
    serializer_class = CommentReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        rid = self.request.query_params.get('rid', None)
        brid = self.request.query_params.get('brid', None)
        if rid and brid:
            return Comment.objects.raw(
                'SELECT * FROM comment WHERE commented_by_id = %s AND commented_on_id = %s',
                [rid, brid]
            )
        elif rid:
            return Comment.objects.raw(
                'SELECT * FROM comment WHERE commented_by_id = %s',
                [rid]
            )
        elif brid:
            return Comment.objects.raw(
                'SELECT * FROM comment WHERE commented_on_id = %s',
                [brid]
            )
        elif self.request.user.is_staff:
            return Comment.objects.raw('SELECT * FROM comment')
        else:
            return Comment.objects.none()

class CommentDetailAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentReadSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'cid'

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'cid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsCommentOwnerPermission]
    serializer_class = CommentUpdateSerializer

class CommentUpdateLovedByAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'cid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CommentLoveUpdateSerializer

class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'cid'
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsCommentOwnerPermission]
