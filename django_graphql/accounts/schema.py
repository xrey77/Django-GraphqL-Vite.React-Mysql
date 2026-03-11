import graphene
from graphene_django import DjangoObjectType
from typing import List, Optional
from accounts.models import UserModel
from .graphql.queries import UserQuery
from .graphql.mutations import RegisterMutation, LoginMutation
from .graphql.types import UserModelType

class Query(graphene.ObjectType):    
    getuser_id = graphene.Field(UserModelType, id=graphene.ID())
    user_query = graphene.Field(lambda: UserQuery) 

    def resolve_getuser_id(root, info, id):
        return UserModel.objects.filter(pk=id).first()

    def resolve_user_query(root, info):
        return UserQuery()

class Mutation(graphene.ObjectType):
    user_mutation = RegisterMutation.Field()
    login_mutation = LoginMutation.Field()

schema = graphene.Schema(
    query=Query, 
    mutation=Mutation
)
