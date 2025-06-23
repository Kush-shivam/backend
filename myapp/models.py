from django.db import models

# Create your models here.
class ContactDetails(models.Model):
          name=models.CharField(max_length=100)
          phoneno=models.CharField(max_length=13)
          email=models.EmailField()
          messege=models.TextField() 