from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import ReaderDetailView,  ReaderUpdateView, ReaderDeleteView, ReaderRegisterAPIView

urlpatterns = [
    path('detail/', ReaderDetailView.as_view(), name='reader-detail'),
    path('update/', ReaderUpdateView.as_view(), name='reader-update'),
    path('delete/', ReaderDeleteView.as_view(), name='reader-delete'),
    path('register/', ReaderRegisterAPIView.as_view(), name='reader-register'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
