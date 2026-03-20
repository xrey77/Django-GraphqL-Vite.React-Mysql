#products.schema
import graphene
from graphene_django import DjangoObjectType
from products.graphql.queries.productlist import ProductsList
from products.graphql.queries.productsearch import SearchProduct
from products.graphql.queries.getproducts import GetProducts
from products.graphql.queries.products_categories import ProductsGroups
from categories.models import Categories

# from products.graphql.types.productsCategoryType import CategoryType

class Query(graphene.ObjectType):    
    page_products = graphene.Field(ProductsList)
    products = graphene.Field(GetProducts)
    search_products = graphene.Field(SearchProduct)
    products_category = graphene.List(ProductsGroups) 

    def resolve_page_products(root, info):
        return ProductsList()

    def resolve_search_products(root, info):
        return SearchProduct()

    def resolve_products(root, info):
        return GetProducts()

    def resolve_products_category(root, info):
        return Categories.objects.all()

schema = graphene.Schema(
    query=Query
)

