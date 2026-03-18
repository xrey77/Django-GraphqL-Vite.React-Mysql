#sales.schema
import graphene
from graphene_django import DjangoObjectType
from sales.graphql.queries.sales_query import SalesQuery

class Query(graphene.ObjectType):    
    get_sales = graphene.Field(SalesQuery)

    def resolve_get_sales(root, info):
        return SalesQuery()

schema = graphene.Schema(
    query=Query
)

