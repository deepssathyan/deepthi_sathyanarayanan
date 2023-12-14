from django.db import models
from django.utils import timezone

# Create your models here. 
# Note that I have used an uppercase letter for class name

class Contact(models.Model):
  name = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  notes = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)  # Add created_at field