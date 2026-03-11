from django.db import models
from django.utils import timezone

class SalesModel(models.Model):
    salesamount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 
    saledate = models.DateTimeField(auto_now_add=False, null=True)
