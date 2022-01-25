from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """mange user profiles"""

    def create_user(self,email,name,password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('User must have  an email address')

        email=self.normalize_email(email)
        user=self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)


        return user


    def create_super_user(self,email,name,password):
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user




class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model user for creating db table"""
    email=models.EmailField(max_length=225,unique=True)
    name=models.CharField(max_length=225)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELD=['name']

    def get_full_name(self):
        """retrieve full name"""
        return self.name

    def get_short_name(self):
        """retrieve short name"""
        return self.name

    def __str__(self):
        """used to return string representation of user objext"""
        return self.email
