from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Book
from .forms import BookForm
from rest_framework import generics
from .serializers import BookSerializer


# ✅ Check if user is an admin
def is_admin(user):
    return user.is_authenticated and user.is_staff


# 📚 View all books (Student & Admin)
def view_books(request):
    books = Book.objects.all().order_by('title')  # Order by title for better UI
    return render(request, 'books/book_list.html', {'books': books})


# 📖 View book details (Student & Admin)
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


# ➕ Add a new book (Admin only)
@login_required
@user_passes_test(is_admin)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_books')  # Redirect to book list after saving
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})


# ✏️ Update a book (Admin only)
@login_required
@user_passes_test(is_admin)
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)  # ✅ Correctly fetch the book
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()  # ✅ Save the updated book correctly
            return redirect('view_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})


# ❌ Delete a book (Admin only)
@login_required
@user_passes_test(is_admin)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('view_books')  # ✅ Redirect after deleting
    return render(request, 'books/book_confirm_delete.html', {'book': book})


# ✅✅✅ API VIEWS ✅✅✅

# 📚 API: List all books (GET) and Create a book (POST)
class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer


# 📖 API: Retrieve, Update, or Delete a book
class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
