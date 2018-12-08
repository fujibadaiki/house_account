from django.db import models


from django.contrib.auth.models import AbstractBaseUser
from account.manegers import PersonManager

class Person(AbstractBaseUser):  #1
    objects = PersonManager()  # 2

    identifier = models.CharField(max_length=64, unique=True, blank=False)  # 3
    name = models.CharField(max_length=128)
    email = models.EmailField()

    is_active = models.BooleanField(default=True)  # 必要です！

    USERNAME_FIELD = 'identifier'  # 4


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=12)

class HouseAccount(models.Model):
    name = models.CharField(max_length=12)
    administrator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

class AccessManager(models.Model):
    ALLOW = 1
    DENY = 0
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    house = models.ForeignKey('HouseAccount', on_delete=models.SET_NULL, null=True)
    permission = models.IntegerField(editable=False)

class Buy(models.Model):
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    house = models.ForeignKey('HouseAccount', on_delete=models.SET_NULL, null=True)
    things = models.CharField(max_length=128)
    cost = models.IntegerField()
    buy_at = models.DateTimeField()

