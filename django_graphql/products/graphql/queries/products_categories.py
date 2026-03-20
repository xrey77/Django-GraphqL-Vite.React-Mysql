import graphene
from products.graphql.types.productType import ProductModelType
from products.models import Product
from categories.models import Categories

class ProductsGroups(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    products = graphene.List(ProductModelType)

    def resolve_products(root, info):
        return Product.objects.filter(category_rel=root)

# ======REQUEST================
# query {
#   productsCategory {
#     name 
#     products {
#       id
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
