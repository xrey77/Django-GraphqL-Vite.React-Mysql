import graphene
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from graphql import GraphQLError
from accounts.graphql.types.userType import UserModelType 
from graphql_jwt.shortcuts import get_token

class LoginMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserModelType)
    token = graphene.String()
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, username, password):
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                token = get_token(user) 
                return LoginMutation(
                    user=user, 
                    token=token, 
                    message="You have logged-in successfully."
                )
            else:
                raise Exception("Please activate your account first.")
        else:
            raise Exception("Invalid username or password.")

class Mutation(graphene.ObjectType):
    login = LoginMutation.Field()

# ========REQUEST======
# mutation UserLogin($username: String!, $password: String!) {
#   loginMutation(username: $username, password: $password) {
#     user {
#       id
#       firstName
#       lastName      
#       email
#       mobile
#       username
#       isActivated
#       isBlocked
#       userpicture
#       mailtoken
#       qrcodeurl
#     }
#     token
#     message
#   }
# }

# ==========VARIABLES===========
# {
#   "username": "Rey",
#   "password":"rey"
# }