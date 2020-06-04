from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError("ENTER AN EMAIL BUDDY")
        if not username:
            raise ValueError("I KNOW YOU HAVE A NAME")
        if not password:
            raise ValueError("PASSWORD?!?!?!? HELLO??")
        
        user = self.model(
             email = self.normalize_email(email),
             username = username)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, username, password):
        user=self.create_user(email, username, password)
        user.is_staff()
        user.is_superuser = True
        user.save()
        return user

class Profile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25, unique=True)
    aboutme = models.CharField(max_length=140),
    avatar = models.ImageField(blank=True, null=True,upload_to='avatars/')
    birthday = models.DateField(blank=True)
    last_online=models.DateTimeField()
    date_joined = models.DateTimeField(default=timezone.now)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS =["email",]
    
    def __str__(self):
        return "@{}".format(self.username)
    

    