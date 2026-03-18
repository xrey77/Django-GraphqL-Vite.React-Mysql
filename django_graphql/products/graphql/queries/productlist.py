import graphene
from products.graphql.types.productType import ProductModelType
from products.models import Product

class ProductsList(graphene.ObjectType):
    products_list = graphene.List(ProductModelType)

    def resolve_products_list(root, info):                     
        return Product.objects.all()


# =====REQUEST======
# query ProductsList{
#   pageProducts{
#     productsList{    
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