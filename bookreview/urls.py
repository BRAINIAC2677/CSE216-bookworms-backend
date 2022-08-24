from django.urls import path 

from .views import BookReviewListAPIView, BookReviewDetailAPIView, BookReviewCreateAPIView, BookReviewUpdateAPIView, BookReviewDeleteAPIView, BookReviewUpdateLovedByAPIView

urlpatterns = [ 
    path('list/', BookReviewListAPIView.as_view(), name='bookreview-list'),
    path('detail/<int:brid>/', BookReviewDetailAPIView.as_view(), name='bookreview-detail'),
    path('create/', BookReviewCreateAPIView.as_view(), name='bookreview-create'),
    path('update/<int:brid>/', BookReviewUpdateAPIView.as_view(), name='bookreview-update'),
    path('update/lovedby/<int:brid>/', BookReviewUpdateLovedByAPIView.as_view(), name='bookreview-update-lovedby'),
    path('<int:brid>/delete/', BookReviewDeleteAPIView.as_view(), name='bookreview-delete'),
]