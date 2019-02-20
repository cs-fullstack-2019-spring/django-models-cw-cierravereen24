from django.db import models


# Create your models here.

# classes of variables, represent different records in database
class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)


class Account(models.Model):
    userName = models.CharField(max_length=45)
    realName = models.CharField(max_length=100)
    accountNumber = models.IntegerField()
    balance = models.IntegerField()
