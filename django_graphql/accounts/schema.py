#accounts schema
import graphene
from graphene_django import DjangoObjectType
from typing import List, Optional
from accounts.models import User
from .graphql.queries.users_query import UsersQuery
from .graphql.queries.userid_query import UserIdQuery
from .graphql.mutations.register_resolver import RegisterMutation
from .graphql.mutations.login_resolver import LoginMutation
from .graphql.mutations.updateProfile_resolver import UpdateProfileMutation
from .graphql.mutations.updatePassword_resolver import UpdatePasswordMutation
from .graphql.mutations.activatemfa_resolver import ActivateMfaMutation
from .graphql.mutations.uploadpic_resolver import UploadPictureMutation

from .graphql.types.userType import UserModelType

class Query(graphene.ObjectType):    
    getuser_id = graphene.Field(UserIdQuery)
    users_query = graphene.Field(lambda: UsersQuery) 

    def resolve_getuser_id(root, info):
        return User.objects.first()

    def resolve_users_query(root, info):
        return UsersQuery()


class Mutation(graphene.ObjectType):
    user_mutation = RegisterMutation.Field()
    login_mutation = LoginMutation.Field()
    update_mutation = UpdateProfileMutation.Field()
    update_password = UpdatePasswordMutation.Field()
    activate_mfa = ActivateMfaMutation.Field()
    upload_picture = UploadPictureMutation.Field()

schema = graphene.Schema(
    query=Query, 
    mutation=Mutation
)
