from django.db import models
from django.contrib.auth.models import (BaseUserManager,AbstractBaseUser)
from django.contrib.auth import get_user_model
# Create your models here.

class StudentManager(BaseUserManager):
    use_in_migrations = True

    def create_student(self,*args):

        username,email,password = args

        employee = self.create(
           username=username,
           email = email,
           password =password,
        )
        

class CreateUser(AbstractBaseUser):
    last_login = models.DateField(auto_now=True)
    username = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    objects = StudentManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
