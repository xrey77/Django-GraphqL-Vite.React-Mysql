import graphene
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from graphql import GraphQLError
from accounts.models import User
from accounts.graphql.types.userType import UserModelType 

class RegisterUser(graphene.ObjectType):
    message = graphene.String()

class RegisterMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        mobile = graphene.String(required=True)
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserModelType)
    message = graphene.String()

    def mutate(self, info, first_name, last_name, email, mobile, username, password):
        if User.objects.filter(email=email).exists():
            raise GraphQLError("Email Address already taken.")
        
        if User.objects.filter(username=username).exists():
            raise GraphQLError("Username already taken.")

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile=mobile,
            username=username,
            role_id=1
        )
        
        user.set_password(password)
        user.save()

        return RegisterUser(
            message="You have registered successfully, please login now."
        )

class Mutation(graphene.ObjectType):
    register_user = RegisterMutation.Field()




# ============CREATE USER - REQUEST=========
# mutation RegisterUser(
#   $firstName: String!, 
#   $lastName: String!, 
#   $email: String!, 
#   $mobile: String!, 
#   $username: String!, 
#   $password: String!
# ) {
#   userMutation(
#     firstName: $firstName, 
#     lastName: $lastName, 
#     email: $email, 
#     mobile: $mobile, 
#     username: $username, 
#     password: $password
#   ) {
#     message
#     user {
#       id
#       username
#       email
#     }
#   }
# }


# =======VARIABLES===========
{
  "firstName": "Winnie",
  "lastName": "Arceo-Gragasin",
  "email": "winnie@yahoo.com",
  "mobile": "1234567890",
  "username": "Winnie",
  "password": "rey"
}
