from django.urls import path
from . import views
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    # Web Views
    path('', views.view_books, name='view_books'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:pk>/edit/', views.update_book, name='update_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),

    # API Endpoints
    path('api/books/', BookListCreateAPIView.as_view(), name='api_book_list_create'),
    path('api/books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='api_book_detail'),
]
