from django.urls import path



from .views import MyReaderDetailAPIView,  ReaderUpdateAPIView, ReaderDeleteAPIView, ReaderRegisterAPIView, ReaderListAPIView, ReaderDetailAPIView

urlpatterns = [
    path('register/', ReaderRegisterAPIView.as_view(), name='reader-register'),
    path('list/', ReaderListAPIView.as_view(), name='reader-list'),
    path('my-detail/', MyReaderDetailAPIView.as_view(), name='reader-my-detail'),
    path('detail/<int:rid>/', ReaderDetailAPIView.as_view(), name='reader-detail'),
    path('update/', ReaderUpdateAPIView.as_view(), name='reader-update'),
    path('delete/', ReaderDeleteAPIView.as_view(), name='reader-delete'),
]
