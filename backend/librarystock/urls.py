from django.urls import path

from .views import LibraryStockListAPIView,MyLibraryStockListAPIView, LibraryStockDetailAPIView, LibraryStockCreateAPIView, LibraryStockUpdateAPIView, LibraryStockDeleteAPIView

urlpatterns = [ 
    path('', LibraryStockListAPIView.as_view(), name='librarystock-list'),
    path('my-list/', MyLibraryStockListAPIView.as_view(), name='my-librarystock-list'),
    path('detail/<int:lsid>/', LibraryStockDetailAPIView.as_view(), name='librarystock-detail'),
    path('create/', LibraryStockCreateAPIView.as_view(), name='librarystock-create'),
    path('update/<int:lsid>/', LibraryStockUpdateAPIView.as_view(), name='librarystock-update'),
    path('delete/<int:lsid>/', LibraryStockDeleteAPIView.as_view(), name='librarystock-delete'),
]