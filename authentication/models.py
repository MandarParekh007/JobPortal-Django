from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self,email,first_name,password=None):
        if not email:
            raise ValueError('Email Must Be Set')
        
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email



