import graphene
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from graphql import GraphQLError
from accounts.graphql.types.userType import UserModelType 
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()

class UpadatePasswordResponse(graphene.ObjectType):
    message = graphene.String()

class UpdatePasswordMutation(graphene.Mutation):
    class Arguments:
        new_password = graphene.String(required=True)        

    user = graphene.Field(UserModelType)
    message = graphene.String()

    def mutate(self, info, new_password):
        user = info.context.user

        if not user.is_authenticated:
            raise Exception("Authentication required")

        if not user.is_active:
            raise Exception("This account is inactive.")

        user.set_password(new_password)
        user.save()

        return UpdatePasswordMutation(
            message="You changed your password successfully.")

class Mutation(graphene.ObjectType):
    update_password = UpdatePasswordMutation.Field()

# ============REQUEST=========
# mutation UpdatePassword(
#   $newPassword: String!) {
#   updatePassword(
#     newPassword: $newPassword) {
#       message
#     }  
# }

# =======VARIABLES===========
# {
#   "newPassword": "1",
# }