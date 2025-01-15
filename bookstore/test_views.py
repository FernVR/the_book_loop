from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from bookstore.models import Book, Review
from django.core.files.uploadedfile import SimpleUploadedFile

class BookstoreViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.superuser = User.objects.create_superuser(username="admin", password="password")
        
        # Create a sample book
        self.book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="A test book.",
            price=10.99,
            stock=5,
            condition="good",
        )
        # URLs for testing
        self.bookstore_url = reverse("bookstore:bookstore")
        self.book_detail_url = reverse("bookstore:book_detail", args=[self.book.id])
        self.add_book_url = reverse("bookstore:add_book")
        self.edit_book_url = reverse("bookstore:edit_book", args=[self.book.id])
        self.delete_review_url = lambda review_id: reverse("bookstore:delete_review", args=[review_id])

    def test_book_detail_view(self):
        """Test the book detail view and adding a review."""
        self.client.login(username="testuser", password="password")
        
        # Test GET request
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)
        
        # Test POST request (add review)
        review_data = {"review": "Great book!", "rating": 5.0}
        response = self.client.post(self.book_detail_url, data=review_data)
        self.assertEqual(response.status_code, 302)  # Redirect after posting
        
        # Check the review was created
        self.assertTrue(Review.objects.filter(book=self.book, author=self.user).exists())


    def test_edit_book_view(self):
        """Test editing a book as a superuser."""
        self.client.login(username="admin", password="password")
        
        # Updated book data
        updated_data = {
            "title": "Updated Book",
            "author": self.book.author,
            "description": "An updated description.",
            "price": 12.99,
            "stock": 15,
            "condition": "fair",
        }
        response = self.client.post(self.edit_book_url, data=updated_data)
        self.assertEqual(response.status_code, 302)  # Redirect after editing
        
        # Check the book was updated
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")
        self.assertEqual(self.book.description, "An updated description.")

    def test_delete_review_view(self):
        """Test deleting a review."""
        self.client.login(username="testuser", password="password")
        
        # Create a review
        review = Review.objects.create(
            book=self.book,
            author=self.user,
            review="This is a review.",
            rating=4.5,
        )
        delete_url = self.delete_review_url(review.id)
        
        # Test deleting the review
        response = self.client.post(delete_url)
        self.assertEqual(response.status_code, 302)  # Redirect after deleting
        
        # Check the review was deleted
        self.assertFalse(Review.objects.filter(id=review.id).exists())
