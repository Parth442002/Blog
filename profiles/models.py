from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.utils import timezone
from django.db.models.signals import pre_save,post_save

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
    avatar= models.ImageField(upload_to='avatars/',blank=True)
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
    '''
    def set_avatar(instance):
        gender = instance.gender
        if gender == 'Male':
            avatar = 'avatars/male.svg'
        elif gender=='Female':
            avatar = 'avatars/female.svg'
        else:
            avatar='avatars/default.svg'
        return avatar
    
    def pre_save_avatar(instance, *args, **kwargs):
        if not instance.avatar:
            instance.avatar = set_avatar(instance)
    
    pre_save.connect(pre_save_avatar, sender=Profile)
    '''
    class Meta():
        ordering = ['-date_joined']

    
            
    
    
    
    


    
    
    
      

            
    

    
