from graphene_django import DjangoObjectType
from products.models import Product

class ProductModelType(DjangoObjectType):
    class Meta:
        model = Product
        fields = (
            "id", "category", "descriptions", "qty", "unit", 
            "costprice", "sellprice", "saleprice", "productpicture", 
            "alertstocks", "criticalstocks"
        )
