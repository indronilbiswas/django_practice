from django.db import models

# Create your models here.
# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField()
