from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
