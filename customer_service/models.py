from django.db import models

# Create your models here.

class CustomerSupport(models.Model):
    """
    """

    full_name = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(max_length=255, null=True, blank=False)
    message = models.TextField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Message: ' {self.message} ' by {self.full_name}"