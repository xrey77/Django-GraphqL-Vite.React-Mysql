from django.db import models

class Sales(models.Model):
    salesamount = models.DecimalField(max_digits=10, decimal_places=2, db_default=0.00) 
    salesdate = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        db_table = 'sales'