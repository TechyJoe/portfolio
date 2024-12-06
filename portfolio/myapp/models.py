from django.db import models

# Create your models here.
class  Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    content= models.TextField(max_length=400)
    number = models.CharField(max_length=15, unique=True)

