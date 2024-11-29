from django.db import models

# Create your models here.

class TestImage(models.Model):
    image = models.ImageField(upload_to='test_images/')
