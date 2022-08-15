from django.urls import path

from .views import LibraryRegisterAPIView, LibraryListAPIView, LibraryDetailAPIView, MyLibraryDetailAPIView, LibraryUpdateAPIView, LibraryDeleteAPIView

urlpatterns = [ 
    path('register/', LibraryRegisterAPIView.as_view(), name='library-register'),
    path('list/', LibraryListAPIView.as_view(), name='library-list'),
    path('my-detail/', MyLibraryDetailAPIView.as_view(), name='library-my-detail'),
    path('detail/<int:lid>/', LibraryDetailAPIView.as_view(), name='library-detail'),
    path('update/', LibraryUpdateAPIView.as_view(), name='library-update'),
    path('delete/', LibraryDeleteAPIView.as_view(), name='library-delete'),
]