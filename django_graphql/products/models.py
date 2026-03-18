from django.db import models
from categories.models import Categories

class Product(models.Model):
    category        = models.CharField(max_length=50, blank=True)
    descriptions    = models.CharField(max_length=100, unique=True)
    qty             = models.IntegerField(db_default=0)
    unit            = models.CharField(max_length=10, blank=True)
    costprice       = models.DecimalField(max_digits=10, decimal_places=2, db_default=0.00) 
    sellprice       = models.DecimalField(max_digits=10, decimal_places=2, db_default=0.00) 
    saleprice       = models.DecimalField(max_digits=10, decimal_places=2, db_default=0.00) 
    productpicture  = models.TextField(max_length=215, blank=True, null=True)
    alertstocks     = models.IntegerField(db_default=0)
    criticalstocks  = models.IntegerField(db_default=0)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True) 

    category_rel = models.ForeignKey(
        Categories, 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name="products"
    )

    class Meta:
        db_table = 'products'     
