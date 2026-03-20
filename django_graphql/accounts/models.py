from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import URLValidator
from role.models import Role

class User(AbstractUser):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)    
    email = models.EmailField(max_length=100, unique=True)    
    mobile = models.CharField(max_length=50, blank=True, null=True)    
    username = models.CharField(max_length=100, unique=True, db_collation="utf8mb4_bin")        
    userpicture = models.CharField(max_length=100, blank=True, db_default='pix.png')
    is_blocked = models.BooleanField(default=False)   
    is_activated = models.BooleanField(default=True)   
    mailtoken = models.IntegerField(db_default=0)
    secretkey = models.CharField(max_length=100, blank=True, null=True)    
    qrcodeurl = models.TextField(validators=[URLValidator()], blank=True,null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)     

    role = models.ForeignKey(
        Role, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="accounts"
    )
    
    class Meta:
        db_table = 'accounts'     

