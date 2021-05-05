from django.db import models
# from django.contrib.auth.models import permissionsMixin
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):
    def _creat_user(self, username, email, is_active,is_staff, is_superuser ,**extra_fields):
        now =timezone.now()

        if not username:
            raise ValueError("The given username is not valid")
        email = self.normalize_email(email)
        user = self.models(username=username, email=email, is_active=is_active, is_superuser=is_superuser,date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self,username,email, password, **extra_fields):
        return self._create_user(username, email,password,is_active=True, is_superuser=False **extra_fields)

    def create_superuser(self,username,email, password, **extra_fields):
        return self.create_user(usernamae, email, password, is_active=True, is_staff=True, is_superuser=True, **extra_fields)

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email= models.EmailField(max_length=250, unique=True)
    username= models.CharField(max_length=30, unique=True)
    first_name=models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number =models.CharField(max_length=20)
    avarta = models.ImageField()
    boi= models.TextField()
    is_active=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=True)
    birth_date=models.DateTimeField(blank=True, null=True)
    date_joined=models.DateTimeField(timezone.now(), null=True)

    objects =UserManager()

    USERNAME_FIELD='username'
    REQUIRED_FIELD=['email']


