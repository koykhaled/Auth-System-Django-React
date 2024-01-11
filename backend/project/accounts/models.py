from django.db import models

from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager

# Create your models here.


class UserAccountManager(BaseUserManager):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError('User must have email address')
        
        email = self.normalize_email(email) # transform email [Khaled@gmail.com] into [khaled@gmail.com]
        
        user = self.model(email=email,name=name)
        
        user.set_password(password) # for hashing password
        
        user.save()
        
        return user


class UserAccount(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=255)
    
    email = models.EmailField(max_length=255,unique=True)
    
    is_active = models.BooleanField(default=False)
    
    is_staff = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email