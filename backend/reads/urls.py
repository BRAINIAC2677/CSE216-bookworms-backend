from django.urls import path

from .views import ReadsListAPIView, ReadsDetailAPIView, ReadsCreateAPIView, ReadsUpdateAPIView, ReadsDeleteAPIView

urlpatterns = [
    path('', ReadsListAPIView.as_view(), name='reads-list'),
    path('<int:rid>/', ReadsDetailAPIView.as_view(), name='reads-detail'),
    path('create/', ReadsCreateAPIView.as_view(), name='reads-create'),
    path('<int:rid>/update/', ReadsUpdateAPIView.as_view(), name='reads-update'),
    path('<int:rid>/delete/', ReadsDeleteAPIView.as_view(), name='reads-delete'),
]