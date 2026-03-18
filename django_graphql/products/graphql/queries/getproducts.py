import graphene
from products.graphql.types.productType import ProductModelType
from products.models import Product

class GetProducts(graphene.ObjectType):
    reports = graphene.List(ProductModelType)

    def resolve_reports(root, info):                     
        return Product.objects.all()


# =====REQUEST======
# query GetProducts{
#   products{
#     reports {
#       id
#       category
#       descriptions
#       qty
#       unit
#       costprice
#       sellprice
#       saleprice
#       productpicture
#       alertstocks
#       criticalstocks      
#     }
#   }
# }