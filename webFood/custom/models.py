from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from config import settings
# Create your models here.


class Staff(AbstractUser):
    username = models.CharField('username',
                                max_length=150,
                                unique=True,
                                help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                error_messages={
                                    'unique': "A user with that username already exists.",
                                }
                                )
    first_name = models.CharField('first name', max_length=30, blank=True, null=False)
    last_name = models.CharField('last name', max_length=150, blank=True, null=False)
    email = models.EmailField('email', blank=True, unique=True)
    password = models.CharField('password', max_length=200,
                                help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')
    date_joined = models.DateTimeField('date joined', default=timezone.now())
    position = models.CharField('position', max_length=200, blank=True)
    user_auth = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        # model = 'Staff'
        # fields = ('username', 'first_name', 'last_name',
        #           'email', 'password', 'date_joined',
        #           'position')
        verbose_name = 'Staff'
        abstract = True


