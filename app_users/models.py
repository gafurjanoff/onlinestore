from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import MyUserManager as UserManager


class User(AbstractUser):
    first_name = models.CharField(('First name'), max_length=100)
    last_name = models.CharField('Last name', max_length=100)
    username = models.CharField('Username', max_length=100, null=True, blank=True)
    email = models.EmailField('Email', max_length=100, unique=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def get_fullname(self):
        return f"{self.first_name} {self.last_name}"

    def set_fullname(self, value):
        names = value.split()
        self.first_name, self.last_name = names[0], " ".join(names[1:])

    fullname = property(get_fullname, set_fullname)
