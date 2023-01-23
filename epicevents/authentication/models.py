from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser):
    ROLE_CHOICES = [
        ('commercial', 'Commercial'),
        ('support', 'Support'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(db_index=True, unique=True, max_length=250)
    role = models.CharField(choices=ROLE_CHOICES, max_length=20)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    objects = UserManager()

    