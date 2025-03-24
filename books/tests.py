# from django.test import TestCase
# from django.urls import reverse
# from books.models import Book


# class BookModelTest(TestCase):
#     def setUp(self):
#         self.book = Book.objects.create(
#             title="Test Book",
#             author="Test Author",
#             description="Test Description",
#             published_date="2023-01-01",
#             isbn_number="1234567890123"
#         )

#     def test_book_str(self):
#         self.assertEqual(str(self.book), "Test Book")


# class BookViewTest(TestCase):
#     def setUp(self):
#         self.book = Book.objects.create(
#             title="Test Book",
#             author="Test Author",
#             description="Test Description",
#             published_date="2023-01-01",
#             isbn_number="1234567890123"
#         )

#     def test_view_books(self):
#         url = reverse('view_books')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "Test Book")

#     def test_add_book(self):
#         url = reverse('add_book')
#         data = {
#             'title': 'New Book',
#             'author': 'New Author',
#             'description': 'New Description',
#             'published_date': '2023-05-10',
#             'isbn_number': '9876543210123',
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, 302)  # ✅ Redirect after success
#         self.assertEqual(Book.objects.count(), 2)  # ✅ 2 books should now exist

#     def test_update_book(self):
#         url = reverse('update_book', args=[self.book.pk])
#         updated_data = {
#             'title': 'Updated Book',
#             'author': 'Updated Author',
#             'description': 'Updated Description',
#             'published_date': '2023-06-01',
#             'isbn_number': '1234567890123',
#         }
#         response = self.client.post(url, updated_data)
#         self.assertEqual(response.status_code, 302)  # ✅ Check for redirect
#         updated_book = Book.objects.get(pk=self.book.pk)
#         self.assertEqual(updated_book.title, 'Updated Book')  # ✅ Check title update

#     def test_delete_book(self):
#         url = reverse('delete_book', args=[self.book.pk])
#         response = self.client.post(url)
#         self.assertEqual(response.status_code, 302)  # ✅ Check for redirect
#         self.assertEqual(Book.objects.count(), 0)  # ✅ No books should be left after delete
