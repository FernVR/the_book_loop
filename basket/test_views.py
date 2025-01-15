from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from bookstore.models import Book
from user_profile.models import WishList

class BasketViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create a test book
        self.book = Book.objects.create(title="Test Book", author="Author", price=10.99)
        
        # Create a wishlist for the test user
        self.wishlist = WishList.objects.create(user=self.user)
        self.wishlist.books.add(self.book)
        
        self.basket_url = reverse('view_basket')
        self.add_to_basket_url = reverse('add_to_basket', args=[self.book.id])
        self.remove_from_basket_url = reverse('remove_from_basket', args=[self.book.id])

    def test_view_basket(self):
        """Test if basket page loads successfully."""
        response = self.client.get(self.basket_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')

    def test_add_to_basket(self):
        """Test adding a book to the basket."""
        self.client.login(username='testuser', password='password')
        session = self.client.session
        session['basket'] = {}
        session.save()

        response = self.client.post(self.add_to_basket_url)

        # Check if the book was added to the basket
        session = self.client.session
        self.assertIn(str(self.book.id), session['basket'])
        self.assertEqual(session['basket'][str(self.book.id)], 1)

        # Check if the book was removed from the wishlist
        self.assertFalse(self.wishlist.books.filter(id=self.book.id).exists())

        # Check redirection
        self.assertRedirects(response, self.basket_url)


    def test_remove_from_basket(self):
        """Test removing a book from the basket."""
        session = self.client.session
        session['basket'] = {str(self.book.id): 1}
        session.save()

        response = self.client.post(self.remove_from_basket_url)

        # Check if the book was removed from the basket
        session = self.client.session
        self.assertNotIn(str(self.book.id), session['basket'])

        # Check redirection
        self.assertRedirects(response, self.basket_url)
