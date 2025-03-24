from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='api_book_list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='api_book_detail'),
]
