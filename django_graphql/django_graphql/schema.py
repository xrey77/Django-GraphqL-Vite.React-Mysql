#django_graphql.schema
import graphene
import accounts.schema
import products.schema
import sales.schema

import graphql_jwt

class Query(accounts.schema.Query, products.schema.Query, sales.schema.Query, graphene.ObjectType):
    pass

class Mutation(accounts.schema.Mutation,  graphene.ObjectType):    
    pass

    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


