from django.urls import path

from .views import CommentListAPIView, CommentDetailAPIView, CommentCreateAPIView, CommentUpdateAPIView, CommentDeleteAPIView, CommentUpdateLovedByAPIView

urlpatterns = [
    path('list/', CommentListAPIView.as_view(), name='comment-list'),
    path('detail/<int:cid>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('update/<int:cid>/', CommentUpdateAPIView.as_view(), name='comment-update'),
    path('update/lovedby/<int:cid>/', CommentUpdateLovedByAPIView.as_view(), name='comment-update-lovedby'),
    path('<int:cid>/delete/', CommentDeleteAPIView.as_view(), name='comment-delete'),
]