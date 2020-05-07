from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from config import settings
# Create your models here.


class MyExUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, password, **extra_fields):
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(email=email, username=username, password=password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user


class ExUser(AbstractUser):
    email = models.EmailField(blank=True, null=True, max_length=255, unique=True)
    username = models.CharField(blank=True, null=True, max_length=255, unique=False)
    positive = models.CharField(blank=True, null=True, max_length=255)

    objects = MyExUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'tbl_exuser'

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email





