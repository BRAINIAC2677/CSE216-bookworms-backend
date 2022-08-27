from django.urls import path

from .views import FriendListAPIView, PendingFriendListAPIView, FriendCreateAPIView, FriendUpdateAPIView, FriendDeleteAPIView

urlpatterns = [ 
    path('list/', FriendListAPIView.as_view(), name='friend-list'),
    path('pending-list/', PendingFriendListAPIView.as_view(), name='friend-pending-list'),
    path('create/', FriendCreateAPIView.as_view(), name='friend-create'),
    path('update/<int:fid>/', FriendUpdateAPIView.as_view(), name='friend-update'),
    path('delete/<int:fid>/', FriendDeleteAPIView.as_view(), name='friend-delete'),
]