from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class UserAccount(models.Model):

    user = models.OneToOneField('account.User', on_delete=models.CASCADE)