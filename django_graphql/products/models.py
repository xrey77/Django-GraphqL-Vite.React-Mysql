from django.db import models

class ProuductModel(models.Model):
    category        = models.CharField(max_length=50, blank=True)
    descriptions    = models.EmailField(max_length=100, unique=True)
    qty             = models.IntegerField(default=0)
    unit            = models.CharField(max_length=10, blank=True)
    costprice       = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    sellprice       = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    saleprice       = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    productpicture  = models.TextField(max_length=215, blank=True, null=True)
    alertstocks     = models.IntegerField(default=0)
    criticalstocks  = models.IntegerField(default=0)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True) 