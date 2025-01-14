from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Book(models.Model):
    CONDITION_CHOICES = [
        ('like-new', 'Like New'),
        ('good', 'Good'),
        ('fair', 'Fair'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    date_published = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    condition = models.CharField(
        max_length=10, choices=CONDITION_CHOICES, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    cover_image = CloudinaryField('image', default='placeholder')
    stock = models.PositiveIntegerField(default=0)
    in_stock = models.BooleanField(default=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        self.in_stock = self.stock > 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer"
    )
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="book_reviewed"
    )
    review = models.TextField()
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review: ' {self.review} ' by {self.author}"
