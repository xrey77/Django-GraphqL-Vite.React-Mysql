from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)    
    email = models.EmailField(max_length=100, unique=True)    
    mobile = models.CharField(max_length=50, blank=True, null=True)    
    username = models.CharField(max_length=100, unique=True)        
    userpicture = models.CharField(max_length=100, blank=True, default='pix.png')
    is_blocked = models.BooleanField(default=False)   
    is_activated = models.BooleanField(default=True)   
    mailtoken = models.IntegerField(default=0)
    secretkey = models.CharField(max_length=70, blank=True, null=True)    
    qrcodeurl = models.URLField(max_length=200, blank=True, null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)     
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
