from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import ReaderDetailView,  ReaderUpdateView, ReaderDeleteView, ReaderRegisterAPIView

urlpatterns = [
    path('detail/', ReaderDetailView.as_view()),
    path('update/', ReaderUpdateView.as_view()),
    path('delete/', ReaderDeleteView.as_view()),
    path('register/', ReaderRegisterAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]