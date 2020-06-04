from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils import timezone
from django.db.models.signals import pre_save

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
        user.is_staff=True
        user.is_superuser = True
        user.save()
        return user



class Profile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=25, unique=True)
    aboutme = models.CharField(max_length=140,blank=True, null=True)
    
    GENDER_CHOICES = (
    ('U','Undefined'),
    ('F','Female'),
    ('M','Male')
                    )
    gender=models.CharField(max_length=20,choices=GENDER_CHOICES)
    avatar = models.ImageField(upload_to='avatars/',blank=True)
    birthday = models.DateField(blank=True,null=True)
    last_online=models.DateTimeField(blank=True,null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS =["email",]
    
    def __str__(self):
        return "@{}".format(self.username)
    
    def is_online(self):
        if self.last_online==timezone.now:
            return True
    
    def post_save_avatar(self,sender, *args, **kwargs):
        if not self.avatar:
            if self.gender == 'M':
                self.avatar="avatars/male.svg"
            
            elif self.gender=='F':
                self.avatar='avatars/female.svg'

            else:
                instance.image = "avatars/default.svg"
            print(self.gender)
            pre_save.connect(post_save_avatar, sender=Profile)
            
    
    
    
    


    
    
    
      

            
    

    
