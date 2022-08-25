from django.urls import path

from .views import ReadsListAPIView, ReadsDetailAPIView, ReadsCreateAPIView, ReadsUpdateAPIView, ReadsDeleteAPIView

urlpatterns = [
    path('list/', ReadsListAPIView.as_view(), name='reads-list'),
    path('detail/<int:rsid>/', ReadsDetailAPIView.as_view(), name='reads-detail'),
    path('create/', ReadsCreateAPIView.as_view(), name='reads-create'),
    path('update/<int:rsid>/', ReadsUpdateAPIView.as_view(), name='reads-update'),
    path('delete/<int:rsid>/', ReadsDeleteAPIView.as_view(), name='reads-delete'),
]