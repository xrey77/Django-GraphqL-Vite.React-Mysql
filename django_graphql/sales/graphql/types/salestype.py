from graphene_django import DjangoObjectType
from sales.models import Sales

class SalesModelType(DjangoObjectType):
    class Meta:
        model = Sales
        fields = (
            "id", "salesamount", "salesdate", 
        )
