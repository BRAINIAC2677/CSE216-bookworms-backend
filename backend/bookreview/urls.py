from django.urls import path 

from .views import BookReviewListAPIView, BookReviewDetailAPIView, BookReviewCreateAPIView, BookReviewUpdateAPIView, BookReviewDeleteAPIView

urlpatterns = [ 
    path('', BookReviewListAPIView.as_view(), name='bookreview-list'),
    path('<int:brid>/', BookReviewDetailAPIView.as_view(), name='bookreview-detail'),
    path('create/', BookReviewCreateAPIView.as_view(), name='bookreview-create'),
    path('<int:brid>/update/', BookReviewUpdateAPIView.as_view(), name='bookreview-update'),
    path('<int:brid>/delete/', BookReviewDeleteAPIView.as_view(), name='bookreview-delete'),
]