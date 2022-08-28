from django.urls import path



from .views import MyReaderDetailAPIView,  ReaderUpdateAPIView, ReaderDeleteAPIView, ReaderRegisterAPIView, ReaderListAPIView, ReaderDetailAPIView, AdminReaderRegisterAPIView

urlpatterns = [
    path('register/', ReaderRegisterAPIView.as_view(), name='reader-register'),
    path('admin-register/', AdminReaderRegisterAPIView.as_view(), name='admin-reader-register'),
    path('list/', ReaderListAPIView.as_view(), name='reader-list'),
    path('my-detail/', MyReaderDetailAPIView.as_view(), name='reader-my-detail'),
    path('detail/<int:rid>/', ReaderDetailAPIView.as_view(), name='reader-detail'),
    path('update/', ReaderUpdateAPIView.as_view(), name='reader-update'),
    path('delete/', ReaderDeleteAPIView.as_view(), name='reader-delete'),
]
