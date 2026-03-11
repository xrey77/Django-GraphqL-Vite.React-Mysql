import graphene
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from graphql import GraphQLError
from accounts.models import UserModel
from .types import UserModelType 

class RegisterUser(graphene.ObjectType):
    user = graphene.Field(UserModelType)
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
        if UserModel.objects.filter(email=email).exists():
            raise GraphQLError("Email Address already taken.")
        
        if UserModel.objects.filter(username=username).exists():
            raise GraphQLError("Username already taken.")

        user = UserModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
            mobile=mobile,
            username=username
        )
        user.set_password(password)
        user.save()

        return RegisterUser(
            user=user, 
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
# {
#   "firstName": "Winnie",
#   "lastName": "Arceo-Gragasin",
#   "email": "winnie@yahoo.com",
#   "mobile": "1234567890",
#   "username": "Winnie",
#   "password": "rey"
# }


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
                # token = get_token(user)
                token, created = Token.objects.get_or_create(user=user)
                return LoginMutation(
                    user=user, 
                    token=token.key, 
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