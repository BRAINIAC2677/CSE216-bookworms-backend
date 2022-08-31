from django.urls import path 

from .views import EventListAPIView 

urlpatterns = [
    path('list/', EventListAPIView.as_view(), name='event-list'),
]