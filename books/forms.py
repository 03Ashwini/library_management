from django import forms
from .models import Book

# Form to add or update books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn_number']
