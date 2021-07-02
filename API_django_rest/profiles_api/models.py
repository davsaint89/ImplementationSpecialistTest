from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """manager para perfiles"""
    def create_user(self, email, name, password=None):
        """Nuevo usuario"""
        if not email:
            raise ValueError('Usuario debe tener e-mail.')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Modelo base de datos para usuarios en el sistema """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    object = UserProfileManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Obtener nomber usuario"""
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        """ returnar cadena representando usuario"""
        return self.email

