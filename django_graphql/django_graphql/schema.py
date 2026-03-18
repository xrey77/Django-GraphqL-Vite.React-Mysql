#django_graphql.schema
import graphene
import accounts.schema
import products.schema
import sales.schema

class Query(accounts.schema.Query, products.schema.Query, sales.schema.Query, graphene.ObjectType):
    pass

class Mutation(accounts.schema.Mutation,  graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)


