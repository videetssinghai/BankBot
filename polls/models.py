from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    FirstName = models.CharField(max_length=10)
    LastName = models.CharField(max_length=10)
    Email = models.CharField(max_length=30,unique = True)
    Password = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now = True, auto_now_add = False)
    timestamp = models.DateTimeField(auto_now = False, auto_now_add=True)

    def __str__(self):
        return self.Email


class Accounts(models.Model):
    Email = models.ForeignKey(User,on_delete=models.CASCADE)
    Balance = models.IntegerField








