from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
      BaseUserManager,PermissionsMixin)


class any_user(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    password= models.PasswordField(max_length=100,blank=True, null=True)
