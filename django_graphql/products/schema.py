#products.schema
import graphene
from graphene_django import DjangoObjectType
from products.graphql.queries.productlist import ProductsList
from products.graphql.queries.getproducts import GetProducts

class Query(graphene.ObjectType):    
    page_products = graphene.Field(ProductsList)
    products = graphene.Field(GetProducts)

    def resolve_page_products(root, info):
        return ProductsList()

    def resolve_products(root, info):
        return GetProducts()

schema = graphene.Schema(
    query=Query
)

